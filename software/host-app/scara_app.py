# scara  ....
import math
from re import U
import time
from scara_serial import SCARA_Serial

# SCARA机械臂控制类，其父类为SCARA_Serial
#  
#          
class SCARA_APP(SCARA_Serial):
    
    def __init__(self, adr=254, fn=0xD1):
        super().__init__(adr, fn)

        self.pos_j1 = 0             # 关节位置(步进电机脉冲数）
        self.pos_j2 = 0
        self.pos_j3 = 0
        self.pos_j4 = 0
        
        self.pos_j1_max = 300       # 关节的最大位置(步进电机脉冲数）
        self.pos_j1_max = 300       
        self.pos_j1_max = 300       
        self.pos_j1_max = 300       
        
        self.bigarm = 170
        self.smallarm = 170 
        self.clock = 6000   # 单片机定时器时钟参数 /1000
        self.theta0 = 0.0    # z轴
        self.theta1 = 0.0    # 大臂
        self.theta2 = 0.0    # 小臂
        self.theta3 = 0.0    # 末端
        self.left_right = 1  # 左右手定义标志
        self.MAXv = 0.18     #额定速度
        self.stride_angle = 0.225/8  #电机步距角
        self.x00 = 175.0
        self.y00 = 45.0
        self.z00 = 0.0 
        self.x0 = 175.0
        self.y0 = 45.0
        self.z0 = 0.0
        self.ms_ = 30         # 加减速的时间段
        self.left_right = 1    
        self.pntfloat1 = 0
        self.pntfloat2 = 0 
        self.pntfloat3 = 0
        self.pntfloat4 = 0

    # 机械臂位置计数器清零
    def pos_reset(self):
        self.pos_j1 = 0
        self.pos_j2 = 0
        self.pos_j3 = 0
        self.pos_j4 = 0
        
    
    # ????
    def find_first_nonzero_index(self, pulse_cnt):
        for i in range(4):
            if pulse_cnt[i] != 0:
                #print(i)
                return i
        return None  # 如果数组中所有元素都是零，则返回 None
   
    # point to point
    def point_to_point(self,startX,startY,endX,endY):
        theta_start = [0.0, 0.0, 0.0, 0.0]
        theta_end   = [0.0, 0.0, 0.0, 0.0]

        self.inverseKinematics(startX, startY)
        theta_start[0] = 0.0
        theta_start[1] = self.theta1 * 180 / (4 * math.atan(1))
        theta_start[2] = self.theta2 * 180 / (4 * math.atan(1))
        theta_start[3] = self.theta3 * 180 / (4 * math.atan(1))
        self.inverseKinematics(endX,endY)
        theta_end[0] = 0.0
        theta_end[1] = self.theta1 * 180 / (4 * math.atan(1))
        theta_end[2] = self.theta2 * 180 / (4 * math.atan(1))
        theta_end[3] = self.theta3 * 180 / (4 * math.atan(1))
        
        #for i in range(4):
            #if((theta_end[i] - theta_start[i]) * 16.0 / 16 / self.stride_angle)
        
        pulse_cnt0 = 0
        pulse_cnt1 = round((theta_end[1] - theta_start[1]) * 60.0 / 16 / self.stride_angle+self.pntfloat2)
        #self.pntfloat2 = ((theta_end[1] - theta_start[1]) * 60.0 / 16 / self.stride_angle+self.pntfloat2)-pulse_cnt1
        pulse_cnt2 = round((theta_end[2] - theta_start[2]) * 60.0 / 16 / self.stride_angle+self.pntfloat3)
        #self.pntfloat3 = ((theta_end[2] - theta_start[2]) * 60.0 / 16 / self.stride_angle+self.pntfloat3)-pulse_cnt2
        pulse_cnt3 = round((theta_end[3] - theta_start[3]) * 48.0 / 16 / self.stride_angle+self.pntfloat4)
        #self.pntfloat4 = ((theta_end[3] - theta_start[3]) * 60.0 / 16 / self.stride_angle+self.pntfloat4)-pulse_cnt3
        pulse_cnt = [pulse_cnt0, pulse_cnt1, pulse_cnt2, pulse_cnt3]
        #run_time = int(self.motor_rt(pulse_cnt))
        pulse_cnt_re = [pulse_cnt0, pulse_cnt1, pulse_cnt2, pulse_cnt3]
        return pulse_cnt_re

    # 逆解
    def inverseKinematics(self, x, y):
        C3 = ((x-62) ** 2 + y ** 2 - self.bigarm ** 2 - self.smallarm ** 2) / (2 * self.bigarm * self.smallarm)
        k1 = ((x - 62) ** 2 + y ** 2 + self.bigarm ** 2 - self.smallarm ** 2) / (2 * self.bigarm)
        k2 = k1 / math.sqrt((x - 62) ** 2 + y ** 2)
        #if y >= 0:  # 上三角
        #    self.theta2 = math.acos(C3)
        #    self.theta1 = 4 * math.atan(1) / 2 - math.atan2(x - 77, y) - math.acos(k2)
        #else:  # 下三角
        #    self.theta2 = -math.acos(C3)
        #    self.theta1 = 4 * math.atan(1) / 2 - math.atan2(x - 77, y) + math.acos(k2)
        if self.left_right == 1:
            self.theta2 = -math.acos(C3)
            self.theta1 = 4 * math.atan(1) / 2 - math.atan2(x - 77, y) + math.acos(k2)
        if self.left_right == 0:
            self.theta2 = math.acos(C3)
            self.theta1 = 4 * math.atan(1) / 2 - math.atan2(x - 77, y) - math.acos(k2)

    # 求运行时间
    def motor_rt(self, pulse_cnt):
        pcnt = [0, 0, 0, 0]
    
        for i in range(4):
            if pulse_cnt[i] < 0:
                pcnt[i] = -pulse_cnt[i]
            else:
                pcnt[i] = pulse_cnt[i]

        i_not0 = self.find_first_nonzero_index(pulse_cnt)
        if  i_not0  is not  None:
            pnt_max = pcnt[i_not0] 
            for i in range(0, 4):
                if pcnt[i] == 0:
                    pnt_max = pnt_max
                else: 
                    if pcnt[i] >= pnt_max:
                        pnt_max = pcnt[i]
    
            t = (3 * pnt_max * self.stride_angle) / ( 2 * self.MAXv )
            print(t)
        else: t = 100
        return t
    
    def movel1(self, start_x, start_y, end_x, end_y):
        startx = start_x
        starty = start_y
        endx = end_x
        endy = end_y
        pulse_p = self.point_to_point(startx,starty,endx,endy)
        dis = math.sqrt((endy-starty) ** 2 + (endx-startx) ** 2)
        steps = int(dis)+1
        deltaX = (endx-startx)/(steps-1)
        deltaY = (endy-starty)/(steps-1)
        currentx = startx
        currenty = starty
        arr=[0,0,0,0]
        pen=[0,0,0,0]
        for i in range(steps-1):
            pulse_cnt  = self.point_to_point( currentx, currenty, currentx + deltaX, currenty + deltaY)
            i_not0 = self.find_first_nonzero_index(pulse_cnt)
            if  i_not0  is not  None:
                for i in range(4):
                    if (pulse_cnt[i] != 0):
                        arr[i] = int(50 * self.clock / abs(pulse_cnt[i]))
                        pen[i] = 1 
                if arr[1]>60000 or arr[2]>60000:
                    if arr[1]>60000:
                        pulse_mid=pulse_cnt[2]
                        pulse_cnt[2]=pulse_cnt[1]
                        pulse_cnt[0]=pulse_cnt[3]=pulse_cnt[1]
                        arr[1]=arr[2]
                        arr[0]=arr[3]=arr[2]
                        pen[1]=pen[2]=1
                        pen[0]=pen[3]=0
                        self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                        print('添加命令 - ',arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])    
                        
                        pulse_cnt[2]=pulse_mid-pulse_cnt[2]
                        pulse_cnt[1]=pulse_cnt[2]
                        pulse_cnt[0]=pulse_cnt[3]=pulse_cnt[2]
                        pen[2]=1
                        pen[0]=pen[1]=pen[3]=0
                        self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                        print('添加命令 - ',arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])    
                    else:
                        pulse_mid=pulse_cnt[1]
                        pulse_cnt[1]=pulse_cnt[2]
                        arr[2]=arr[1]
                        pulse_cnt[0]=pulse_cnt[3]=pulse_cnt[2]
                        arr[0]=arr[3]=arr[1]
                        pen[1]=pen[2]=1
                        pen[0]=pen[3]=0
                        self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                        print('添加命令 - ',arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])    
                        
                        pulse_cnt[1]=pulse_mid-pulse_cnt[1]
                        pulse_cnt[2]=pulse_cnt[1]
                        pulse_cnt[0]=pulse_cnt[3]=pulse_cnt[1]
                        pen[1]=1
                        pen[0]=pen[2]=pen[3]=0
                        self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                        print('添加命令 - ',arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])    
                else:
                    for i in range(4):
                        if (pulse_cnt[i] == 0):
                            arr[i] = arr[i_not0]
                            pulse_cnt[i] = pulse_cnt[i_not0]
                            pen[i] = 0 
                    self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                    print('添加命令 - ',arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])    
                currentx = currentx + deltaX
                currenty = currenty + deltaY
                print(currentx,currenty)
        print('命令缓冲区中命令数量 = ', self.cmd_queue.qsize())
        self.x0 = endx
        self.y0 = endy


    # 直线运动
    def movel(self, start_x, start_y, end_x, end_y):
        
        startx = start_x
        starty = start_y
        endx = end_x
        endy = end_y
        self.pntfloat1 = 0
        self.pntfloat2 = 0
        self.pntfloat3 = 0
        self.pntfloat4 = 0
        arr_1=[]
        arr_2=[]
        pnt_1 = []
        pnt_2 = []
        run_time = 0
        pulse_p = self.point_to_point(startx,starty,endx,endy)
        #print("目标脉冲数：" )
        print(pulse_p[0],pulse_p[1],pulse_p[2],pulse_p[3])
        self.pntfloat1 = 0
        self.pntfloat2 = 0
        self.pntfloat3 = 0
        self.pntfloat4 = 0
        dis = math.sqrt((endy-starty) ** 2 + (endx-startx) ** 2)
        #run_timep = self.motor_rt(pulse_p)*200/dis
        
        
        if dis<2:
            self.movep(startx,starty,endx,endy)
        else:
            #print ( dis)
            #steps = int(dis/4 + 1)  #插值步数/插值点空隙
            #print (steps)
            #run_timep = self.motor_rt(pulse_p)*500/dis 
            k=1
            if dis>=50: k=3
            elif 40<=dis<=50: k=4
            elif 20<=dis<40: k=5
            elif 10<=dis<20: k=5
            elif 5<=dis<10: k=10
            else : k=30
            run_timep = round(self.motor_rt(pulse_p)*200/dis/30)*30
            steps = int(dis + 1)
            #steps = int(run_timep/30 + 1)  #插值步数/插值点空隙
            #if steps < int(dis/4 + 1) :
            #    steps = int(dis/4 + 1)
            #if steps > 2*int(dis + 1):
            #    steps = 2*int(dis + 1)
            #if run_timep/(steps-1) >30  :
            #    run_timep = (steps-1) * 30
            #print(run_timep)
            #print(steps)
            #print(run_timep/(steps-1))
            deltaX = (endx-startx)
            deltaY = (endy-starty)                                                                                                      
            dis_acc = dis/6
            rt_acc = run_timep/4
            dis_acc_one = dis_acc/dis
            rt_acc_one = rt_acc/run_timep
            a_one = 2*dis_acc_one/rt_acc_one**2
            currentx = startx
            currenty = starty
            pulse_l   = [0,0,0,0]
            pulse_pay = [0,0,0,0]
            arr = [0, 0, 0, 0]
            pen = [0, 0, 0, 0]
            us = 0
            ue = 1
            ps = 0
            pe = 1
            vs = 0
            ve = 0
            as1 = 0
            ae = 0
            a0 = -(2*pe*us**5 - 2*ps*ue**5 - 10*pe*ue*us**4 + 10*ps*ue**4*us - 2*ue*us**5*ve
                + 2*ue**5*us*vs + ae*ue**2*us**5 - 2*ae*ue**3*us**4 + ae*ue**4*us**3 - as1*ue**3*us**4
                + 2*as1*ue**4*us**3 - as1*ue**5*us**2 + 20*pe*ue**2*us**3 - 20*ps*ue**3*us**2 + 10*ue**2*us**4*ve
                - 8*ue**3*us**3*ve + 8*ue**3*us**3*vs - 10*ue**4*us**2*vs)/(2*(ue - us)**5)
            a1 = (2*ue**5*vs - 2*us**5*ve + 2*ae*ue*us**5 - 2*as1*ue**5*us + 10*ue*us**4*ve
                - 10*ue**4*us*vs - ae*ue**2*us**4 - 4*ae*ue**3*us**3 + 3*ae*ue**4*us**2 - 3*as1*ue**2*us**4
                + 4*as1*ue**3*us**3 + as1*ue**4*us**2 + 60*pe*ue**2*us**2 - 60*ps*ue**2*us**2 + 16*ue**2*us**3*ve
                - 24*ue**3*us**2*ve + 24*ue**2*us**3*vs - 16*ue**3*us**2*vs)/(2*(ue - us)**5)
            a2 = -(ae*us**5 - as1*ue**5 + 4*ae*ue*us**4 + 3*ae*ue**4*us - 3*as1*ue*us**4 - 4*as1*ue**4*us
                + 60*pe*ue*us**2 + 60*pe*ue**2*us - 60*ps*ue*us**2 - 60*ps*ue**2*us + 36*ue*us**3*ve
                - 24*ue**3*us*ve + 24*ue*us**3*vs - 36*ue**3*us*vs - 8*ae*ue**2*us**3 + 8*as1*ue**3*us**2
                - 12*ue**2*us**2*ve + 12*ue**2*us**2*vs)/(2*(ue - us)**5)
            a3 = (ae*ue**4 + 3*ae*us**4 - 3*as1*ue**4 - as1*us**4 + 20*pe*ue**2 + 20*pe*us**2 - 20*ps*ue**2
                - 20*ps*us**2 - 8*ue**3*ve - 12*ue**3*vs + 12*us**3*ve + 8*us**3*vs + 4*ae*ue**3*us - 4*as1*ue*us**3
                + 28*ue*us**2*ve - 32*ue**2*us*ve + 32*ue*us**2*vs - 28*ue**2*us*vs - 8*ae*ue**2*us**2
                + 8*as1*ue**2*us**2 + 80*pe*ue*us - 80*ps*ue*us)/(2*(ue - us)**5)
            a4 = -(30*pe*ue + 30*pe*us - 30*ps*ue - 30*ps*us + 2*ae*ue**3 + 3*ae*us**3 - 3*as1*ue**3
                - 2*as1*us**3 - 14*ue**2*ve - 16*ue**2*vs + 16*us**2*ve + 14*us**2*vs - 4*ae*ue*us**2
                - ae*ue**2*us + as1*ue*us**2 + 4*as1*ue**2*us - 2*ue*us*ve + 2*ue*us*vs)/(2*(ue - us)**5)
            a5 = (12*pe - 12*ps - 6*ue*ve - 6*ue*vs + 6*us*ve + 6*us*vs + ae*ue**2 + ae*us**2
                - as1*ue**2 - as1*us**2 - 2*ae*ue*us + 2*as1*ue*us)/(2*(ue - us)**5)
            for i in range(1,steps+1): 
                
                
                us = 0
                ue = 1
                ps = 0
                pe = 1
                vs = 0
                ve = 0
                
                #a0 = -(pe*us**3 - ps*ue**3 - 3*pe*ue*us**2 + 3*ps*ue**2*us - ue*us**3*ve
                #    + ue**3*us*vs + ue**2*us**2*ve - ue**2*us**2*vs)/(ue - us)**3
                #a1 = (ue**3*vs - us**3*ve - ue*us**2*ve + 2*ue**2*us*ve - 2*ue*us**2*vs
                #    + ue**2*us*vs - 6*pe*ue*us + 6*ps*ue*us)/(ue - us)**3
                #a2 = (3*pe*ue + 3*pe*us - 3*ps*ue - 3*ps*us - ue**2*ve - 2*ue**2*vs
                #    + 2*us**2*ve + us**2*vs - ue*us*ve + ue*us*vs)/(ue - us)**3
                #a3 = -(2*pe - 2*ps - ue*ve - ue*vs + us*ve + us*vs)/(ue - us)**3
                #lamud  = a0 + a1*(i/steps) + a2*(i/steps)**2 + a3*(i/steps)**3

                
                    
                    

                
                #lamud=  a0 + a1*(i/steps) + a2*(i/steps)**2 + a3*(i/steps)**3 + a4*(i/steps)**4 + a5*(i/steps)**5
                
                if (i/steps) <= (rt_acc_one):
                    lamud = 0.5*(a_one)*(i/steps)*(i/steps)
                elif (rt_acc_one)<(i/steps)<=(1-rt_acc_one):
                    lamud = 0.5*(a_one)*(rt_acc_one)*(rt_acc_one)+(a_one)*(rt_acc_one)*(i/steps-(rt_acc_one))
                else:
                    lamud = 0.5*(a_one)*(rt_acc_one)*(rt_acc_one)+(a_one)*(rt_acc_one)*(i/steps-(rt_acc_one))-0.5*(a_one)*(i/steps-(1-rt_acc_one))*(i/steps-(1-rt_acc_one))
                
                #print('i:')
                #print(i)
                #print('time归一:') 
                #print( i/steps)
                #print('lamud:' )
                #print(lamud)
                #print('当前坐标:')
                #print(currentx, currenty)
                pulse_cnt  = self.point_to_point( currentx, currenty, startx + deltaX*lamud, starty + deltaY*lamud)
                for i in range(4):
                    pulse_l[i]=pulse_l[i]+pulse_cnt[i]
                    #print(pulse_l[i])
                i_not0 = self.find_first_nonzero_index(pulse_cnt)
                if  i_not0  is not  None:
                    for i in range(4):
                        if (pulse_cnt[i] != 0):
                            arr[i] = int(run_timep/(steps-1) * self.clock / abs(pulse_cnt[i])/3)
                            pen[i] = 1
                    for i in range(4):
                        if (pulse_cnt[i] == 0):
                            arr[i] = arr[i_not0]
                            pulse_cnt[i] = pulse_cnt[i_not0]
                            pen[i] = 0   
                    self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                    print('添加命令 - ',arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])
                    arr_1.append(arr[1])
                    arr_2.append(arr[2])
                    pnt_1.append(pulse_cnt[1])
                    pnt_2.append(pulse_cnt[2])
                    currentx = startx + deltaX*lamud
                    currenty = starty + deltaY*lamud
                    #print ('插值后坐标:')
                    #print (currentx,currenty)
                    #time.sleep((run_timep/(steps-1))/2000)
            #print ('实际脉冲:')
            #print(arr_1)
            #print(arr_2)
            #print(pnt_1)
            #print(pnt_2)
            #self.pointdraw(arr_1)
            #self.pointdraw(pnt_1)
            #self.pointdraw(arr_2)
            #self.pointdraw(pnt_2)
            #print (pulse_l[0],pulse_l[1],pulse_l[2],pulse_l[3])
            for i in range(4):
                pulse_pay[i] = pulse_p[i] - pulse_l[i]
            i_not0 = self.find_first_nonzero_index(pulse_pay)
            if  i_not0  is not  None:
                for i in range(4):
                    if (pulse_pay[i] != 0):
                        arr[i] = int(10 * self.clock / abs(pulse_pay[i]))
                        pen[i] = 1
                for i in range(4):
                    if (pulse_pay[i] == 0):
                        arr[i] = arr[i_not0]
                        pulse_pay[i] = pulse_pay[i_not0]
                        pen[i] = 0
                self.cmd_queue_put((arr[0], pulse_pay[0], pen[0], arr[1], pulse_pay[1], pen[1], arr[2], pulse_pay[2], pen[2], arr[3], pulse_pay[3], pen[3]))  # send command
                print('添加命令 - ',arr[0], pulse_pay[0], pen[0], arr[1], pulse_pay[1], pen[1], arr[2], pulse_pay[2], pen[2], arr[3], pulse_pay[3], pen[3])
        #time.sleep(run_timep/1000)
        print('命令缓冲区中命令数量 = ', self.cmd_queue.qsize())
        #self.cmd_queue_sync()
        self.x0 = endx
        self.y0 = endy    

            
    
    # 点到点的快速运动
    def movep(self, start_x, start_y, end_x, end_y):
        startx = start_x
        starty = start_y
        endx = end_x
        endy = end_y
        pcnt = [0, 0, 0, 0]
        Vmax = [0.0, 0.0, 0.0, 0.0]
        acc  = [0.0, 0.0, 0.0, 0.0]
        arr_1= []
        arr_2= []
        arr_3= []
        arr_4= []
        pnt_1= []
        pnt_2= []
        pnt_3= []
        pnt_4= []
        pen_1= []
        pen_2= []
        pen_3= []
        pen_4= []
        arr = [0,0,0,0]
        pnt = [0,0,0,0]
        pen = [0, 0, 0, 0]
        pnt_sum = [0, 0, 0, 0]
        pnt_ave= [0, 0, 0, 0]
        t_ave =  [0, 0, 0, 0]
        arr_ave= [0,0,0,0]
        pen_ave = [0,0,0,0]
        rv = True
        dis = math.sqrt((endy-starty) ** 2 + (endx-startx) ** 2)
        self.inverseKinematics(startx,starty)
        # theta0_now  = 0.0
        theta1_now  = self.theta1
        theta2_now  = self.theta2
        theta3_now  = self.theta3
        self.inverseKinematics(endx,endy)
        pulse_cnt0 = 0
        pulse_cnt1 = round((self.theta1 * 180 / (4 * math.atan(1)) - theta1_now * 180 / (4 * math.atan(1))) * 60.0 / 16 / self.stride_angle)
        pulse_cnt2 = round((self.theta2 * 180 / (4 * math.atan(1)) - theta2_now * 180 / (4 * math.atan(1))) * 60.0 / 16 / self.stride_angle)
        pulse_cnt3 = round((self.theta3 * 180 / (4 * math.atan(1)) - theta3_now * 180 / (4 * math.atan(1))) * 48.0 / 16 / self.stride_angle)
        pulse_cnt = [pulse_cnt0, pulse_cnt1, pulse_cnt2, pulse_cnt3]
        print(pulse_cnt[0],pulse_cnt[1],pulse_cnt[2],pulse_cnt[3])
        for i in range(4):
            if pulse_cnt[i] < 0:
                pcnt[i] = -pulse_cnt[i]
            else:
                pcnt[i] = pulse_cnt[i]
        i_not0 = self.find_first_nonzero_index(pulse_cnt)
        if  i_not0  is not  None:          #脉冲数全为0不执行
            K = 1
            if 10 < dis <= 40: K = 2
            if dis <= 10 : K = 10
            if dis <= 5  :  K = 20
            run_time = int(self.motor_rt(pulse_cnt))*K    # speed  
            acc_t = int((run_time / 4 / self.ms_)) * self.ms_   
            if acc_t>0:                    #加速时间没有self.ms_，不加减速
                for i in range(4):
                    Vmax[i] = float(pcnt[i]) * self.stride_angle / float(run_time - acc_t)
                    acc[i] = Vmax[i] / acc_t
                n = int(acc_t / self.ms_)

                for i in range(n):
                    for q in range(4):
                        if pulse_cnt[q]>0: 
                            pen[q] = 1
                            arr[q] = (self.stride_angle * self.clock) / (self.ms_/2 * acc[q] * (2 * i + 1))
                            pnt[q] = int((self.ms_ * self.ms_/2 * acc[q] * (2 * i + 1)) / self.stride_angle)
                            if pnt[q]>0: arr[q] = int(self.ms_ / pnt[q]*self.clock)
                            else:
                                pen[q] = 0
                                pnt[q] = 3
                                arr[q] = int(self.clock * self.ms_/pnt[q])
                                     
                        if pulse_cnt[q]<0: 
                            pen[q] = 1
                            arr[q] = (self.stride_angle * self.clock) / (self.ms_ * acc[q] * (2 * i + 1))
                            pnt[q] = int((self.ms_ * self.ms_/2 * acc[q] * (2 * i + 1)) / self.stride_angle)
                            if pnt[q]>0: 
                                arr[q] = int(self.ms_ / pnt[q]*self.clock)
                                pnt[q] = -pnt[q]
                            else:
                                pen[q] = 0
                                pnt[q] = 3
                                arr[q] = int(self.clock * self.ms_/pnt[q])
                                      
                        if pulse_cnt[q]==0:
                            pen[q] = 0
                            pnt[q] = 3
                            arr[q] = int(self.clock * self.ms_/pnt[q])
                    if arr[0]>60000 or arr[1]>60000 or arr[2]>60000 or arr[3]>60000:
                        for i in range(4):
                            arr[i]=int(arr[i]/3)             
                    self.cmd_queue_put((arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3]))  # send command
                    print('添加命令 - ', arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3])
                    #while True:
                    #    if rv is True:
                    #        break
                    #    rv = self.all_motor_run((arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3]))  # send command
                    arr_1.append(arr[0])
                    arr_2.append(arr[1])
                    arr_3.append(arr[2])
                    arr_4.append(arr[3])
                    pnt_1.append(pnt[0])
                    pnt_2.append(pnt[1])
                    pnt_3.append(pnt[2])
                    pnt_4.append(pnt[3])
                    pen_1.append(pen[0])
                    pen_2.append(pen[1])
                    pen_3.append(pen[2])
                    pen_4.append(pen[3])
                    for w in range(4):
                        pnt_sum[w] = pnt_sum[w] + abs(pnt[w]*pen[w])
                    #time.sleep(self.ms_/2000)
                for i in range(4):
                    pnt_ave[i] = pcnt[i]-2*pnt_sum[i]
                    t_ave[i] = run_time - n * self.ms_*2                
                i_not0 = self.find_first_nonzero_index(pnt_ave)
                if  i_not0  is not  None:
                    for i in range(4):
                        if (pulse_cnt[i] != 0):
                            if(pulse_cnt[i]>0):
                                arr_ave[i] = int(t_ave[i]/pnt_ave[i]*self.clock)
                                pen_ave[i] = 1
                            if(pulse_cnt[i]<0):
                                arr_ave[i] = int(t_ave[i]/pnt_ave[i]*self.clock)
                                pen_ave[i] = 1
                                pnt_ave[i] = -pnt_ave[i]
                    for i in range(4):
                        if (pulse_cnt[i] == 0):
                            arr_ave[i] = arr_ave[i_not0]
                            pnt_ave[i] = pnt_ave[i_not0]
                            pen_ave[i] = 0
                if arr_ave[0]>60000 or arr_ave[1]>60000 or arr_ave[2]>60000 or arr_ave[3]>60000:
                        for i in range(4):
                            arr_ave[i]=int(arr_ave[i]/3) 
                self.cmd_queue_put((arr_ave[0], pnt_ave[0], pen_ave[0], arr_ave[1], pnt_ave[1], pen_ave[1], arr_ave[2], pnt_ave[2], pen_ave[2], arr_ave[3], pnt_ave[3], pen_ave[3]))  # send command
                print('添加命令 - ', arr_ave[0], pnt_ave[0], pen_ave[0], arr_ave[1], pnt_ave[1], pen_ave[1], arr_ave[2], pnt_ave[2], pen_ave[2], arr_ave[3], pnt_ave[3], pen_ave[3])
                #self.pointdraw(arr_2)
                #self.pointdraw(pnt_2)
                #while True:
                #    if rv is True:
                #       break
                #    rv = self.all_motor_run((arr_ave[0], pnt_ave[0], pen_ave[0], arr_ave[1], pnt_ave[1], pen_ave[1], arr_ave[2], pnt_ave[2], pen_ave[2], arr_ave[3], pnt_ave[3], pen_ave[3]))  # send command
                #time.sleep(t_ave[0]/2000)
                for i in range(n):
                    self.cmd_queue_put((arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i]))  # send command
                    print('添加命令 - ', arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i])
                    #while True:
                    #    if rv is True:
                    #        break
                    #    rv = self.all_motor_run((arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i]))  # send command
                    #time.sleep(self.ms_/2000)            
            else:
                i_not0 = self.find_first_nonzero_index(pcnt)
                if  i_not0  is not  None:
                    for i in range(4):
                        if (pcnt[i] != 0):
                                arr[i] = int(run_time/pcnt[i]*self.clock)
                                pen[i] = 1
                    for i in range(4):
                        if (pulse_cnt[i] == 0):
                            arr[i] = arr[i_not0]
                            pulse_cnt[i] = pulse_cnt[i_not0]
                            pen[i] = 0
                    self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                    print('添加命令 - ', arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])
                    #while True:
                    #    if rv is True:
                    #        break
                    #    rv = self.all_motor_run((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                    #time.sleep(run_time/2000)    
        print('命令缓冲区中命令数量 = ', self.cmd_queue.qsize())
        #self.cmd_queue_sync()
        self.x0 = endx
        self.y0 = endy    


    def movep1(self, start_x, start_y, end_x, end_y):
        startx = start_x
        starty = start_y
        endx = end_x
        endy = end_y
        pcnt = [0, 0, 0, 0]
        Vmax = [0.0, 0.0, 0.0, 0.0]
        acc  = [0.0, 0.0, 0.0, 0.0]
        arr_1= []
        arr_2= []
        arr_3= []
        arr_4= []
        pnt_1= []
        pnt_2= []
        pnt_3= []
        pnt_4= []
        pen_1= []
        pen_2= []
        pen_3= []
        pen_4= []
        arr = [0,0,0,0]
        pnt = [0,0,0,0]
        pen = [0, 0, 0, 0]
        pnt_sum = [0, 0, 0, 0]
        pnt_ave= [0, 0, 0, 0]
        t_ave =  [0, 0, 0, 0]
        arr_ave= [0,0,0,0]
        pen_ave = [0,0,0,0]
        rv = True
        dis = math.sqrt((endy-starty) ** 2 + (endx-startx) ** 2)
        self.inverseKinematics(startx,starty)
        # theta0_now  = 0.0
        theta1_now  = self.theta1
        theta2_now  = self.theta2
        theta3_now  = self.theta3
        self.inverseKinematics(endx,endy)
        pulse_cnt0 = 0
        pulse_cnt1 = round((self.theta1 * 180 / (4 * math.atan(1)) - theta1_now * 180 / (4 * math.atan(1))) * 60.0 / 16 / self.stride_angle)
        pulse_cnt2 = round((self.theta2 * 180 / (4 * math.atan(1)) - theta2_now * 180 / (4 * math.atan(1))) * 60.0 / 16 / self.stride_angle)
        pulse_cnt3 = round((self.theta3 * 180 / (4 * math.atan(1)) - theta3_now * 180 / (4 * math.atan(1))) * 48.0 / 16 / self.stride_angle)
        pulse_cnt = [pulse_cnt0, pulse_cnt1, pulse_cnt2, pulse_cnt3]
        print(pulse_cnt[0],pulse_cnt[1],pulse_cnt[2],pulse_cnt[3])
        for i in range(4):
            if pulse_cnt[i] < 0:
                pcnt[i] = -pulse_cnt[i]
            else:
                pcnt[i] = pulse_cnt[i]
        i_not0 = self.find_first_nonzero_index(pulse_cnt)
        if  i_not0  is not  None:          #脉冲数全为0不执行
            K = 1
            if 10 < dis <= 40: K = 2
            if dis <= 10 : K = 4
            if dis <= 5  :  K = 20
            run_time = int(self.motor_rt(pulse_cnt))*K    # speed  
            acc_t = int((run_time / 3 / self.ms_)) * self.ms_   
            if acc_t>0:                    #加速时间没有self.ms_，不加减速
                for i in range(4):
                    Vmax[i] = float(pcnt[i]) * self.stride_angle / float(run_time - acc_t)
                    acc[i] = Vmax[i] / acc_t
                n = int(acc_t / self.ms_)

                for i in range(n):
                    for q in range(4):
                        if pulse_cnt[q]>0: 
                            pen[q] = 1
                            arr[q] = (self.stride_angle * self.clock) / (self.ms_/2 * acc[q] * (2 * i + 1))
                            pnt[q] = int((self.ms_ * self.ms_/2 * acc[q] * (2 * i + 1)) / self.stride_angle)
                            if pnt[q]>0: arr[q] = int(self.ms_ / pnt[q]*self.clock)
                            else:
                                pen[q] = 0
                                arr[q] = self.clock * self.ms_
                                pnt[q] = 1     
                        if pulse_cnt[q]<0: 
                            pen[q] = 1
                            arr[q] = (self.stride_angle * self.clock) / (self.ms_/2 * acc[q] * (2 * i + 1))
                            pnt[q] = int((self.ms_ * self.ms_/2 * acc[q] * (2 * i + 1)) / self.stride_angle)
                            if pnt[q]>0: 
                                arr[q] = int(self.ms_ / pnt[q]*self.clock)
                                pnt[q] = -pnt[q]
                            else:
                                pen[q] = 0
                                arr[q] = self.clock * self.ms_
                                pnt[q] = 1      
                        if pulse_cnt[q]==0:
                            pen[q] = 0
                            arr[q] = self.clock * self.ms_
                            pnt[q] = 1      
                    self.cmd_queue_put((arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3]))  # send command
                    print('添加命令 - ', arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3])
                    #while True:
                    #    if rv is True:
                    #        break
                    #    rv = self.all_motor_run((arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3]))  # send command
                    arr_1.append(arr[0])
                    arr_2.append(arr[1])
                    arr_3.append(arr[2])
                    arr_4.append(arr[3])
                    pnt_1.append(pnt[0])
                    pnt_2.append(pnt[1])
                    pnt_3.append(pnt[2])
                    pnt_4.append(pnt[3])
                    pen_1.append(pen[0])
                    pen_2.append(pen[1])
                    pen_3.append(pen[2])
                    pen_4.append(pen[3])
                    for w in range(4):
                        pnt_sum[w] = pnt_sum[w] + abs(pnt[w]*pen[w])
                    #time.sleep(self.ms_/2000)
                for i in range(4):
                    pnt_ave[i] = pcnt[i]-2*pnt_sum[i]
                    t_ave[i] = run_time - n * self.ms_*2                
                i_not0 = self.find_first_nonzero_index(pnt_ave)
                if  i_not0  is not  None:
                    for i in range(4):
                        if (pulse_cnt[i] != 0):
                            if(pulse_cnt[i]>0):
                                arr_ave[i] = int(t_ave[i]/pnt_ave[i]*self.clock)
                                pen_ave[i] = 1
                            if(pulse_cnt[i]<0):
                                arr_ave[i] = int(t_ave[i]/pnt_ave[i]*self.clock)
                                pen_ave[i] = 1
                                pnt_ave[i] = -pnt_ave[i]
                    for i in range(4):
                        if (pulse_cnt[i] == 0):
                            arr_ave[i] = arr_ave[i_not0]
                            pnt_ave[i] = pnt_ave[i_not0]
                            pen_ave[i] = 0
                self.cmd_queue_put((arr_ave[0], pnt_ave[0], pen_ave[0], arr_ave[1], pnt_ave[1], pen_ave[1], arr_ave[2], pnt_ave[2], pen_ave[2], arr_ave[3], pnt_ave[3], pen_ave[3]))  # send command
                print('添加命令 - ', arr_ave[0], pnt_ave[0], pen_ave[0], arr_ave[1], pnt_ave[1], pen_ave[1], arr_ave[2], pnt_ave[2], pen_ave[2], arr_ave[3], pnt_ave[3], pen_ave[3])
                #self.pointdraw(arr_2)
                #self.pointdraw(pnt_2)
                #while True:
                #    if rv is True:
                #       break
                #    rv = self.all_motor_run((arr_ave[0], pnt_ave[0], pen_ave[0], arr_ave[1], pnt_ave[1], pen_ave[1], arr_ave[2], pnt_ave[2], pen_ave[2], arr_ave[3], pnt_ave[3], pen_ave[3]))  # send command
                #time.sleep(t_ave[0]/2000)
                for i in range(n):
                    self.cmd_queue_put((arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i]))  # send command
                    print('添加命令 - ', arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i])
                    #while True:
                    #    if rv is True:
                    #        break
                    #    rv = self.all_motor_run((arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i]))  # send command
                    #time.sleep(self.ms_/2000)            
            else:
                i_not0 = self.find_first_nonzero_index(pcnt)
                if  i_not0  is not  None:
                    for i in range(4):
                        if (pcnt[i] != 0):
                                arr[i] = int(run_time/pcnt[i]*self.clock)
                                pen[i] = 1
                    for i in range(4):
                        if (pulse_cnt[i] == 0):
                            arr[i] = arr[i_not0]
                            pulse_cnt[i] = pulse_cnt[i_not0]
                            pen[i] = 0
                    self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                    print('添加命令 - ', arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])
                    #while True:
                    #    if rv is True:
                    #        break
                    #    rv = self.all_motor_run((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                    #time.sleep(run_time/2000)    
        print('命令缓冲区中命令数量 = ', self.cmd_queue.qsize())
        self.x0 = endx
        self.y0 = endy


    def movez(self, start_z, end_z):
        self.ms_=int(self.ms_/3)
        startz = start_z
        endz = end_z
        pulse_cnt0 = int((endz-startz)/10 * 360 / self.stride_angle)
        pcnt = [0, 0, 0, 0]
        Vmax = [0.0, 0.0, 0.0, 0.0]
        acc  = [0.0, 0.0, 0.0, 0.0]
        arr_1=[]
        arr_2=[]
        arr_3=[]
        arr_4=[]
        pnt_1=[]
        pnt_2=[]
        pnt_3=[]
        pnt_4=[]
        pen_1=[]
        pen_2=[]
        pen_3=[]
        pen_4=[]
        arr = [0,0,0,0]
        pnt = [0,0,0,0]
        pen = [0, 0, 0, 0]
        pnt_sum = [0, 0, 0, 0]
        pnt_ave=[0, 0, 0, 0]
        t_ave = [0, 0, 0, 0]
        arr_ave= [0,0,0,0]
        pen_ave = [0,0,0,0]
        pulse_cnt = [pulse_cnt0, 0, 0, 0]
        k = 10
        #print (pulse_cnt[0],pulse_cnt[1],pulse_cnt[2],pulse_cnt[3])
        for i in range(4):
            if pulse_cnt[i] < 0:
                pcnt[i] = -pulse_cnt[i]
            else:
                pcnt[i] = pulse_cnt[i]
        run_time = int(self.motor_rt(pulse_cnt))/2   # speed
        acc_t = int((run_time / 4 /(  self.ms_))) * ( self.ms_)
        if acc_t>0:
            for i in range(4):
                Vmax[i] = float(pcnt[i]) * self.stride_angle / float(run_time - acc_t)
                acc[i] = Vmax[i] / acc_t
            n = int(acc_t /(self.ms_))

            for i in range(n):
                for q in range(4):
                    if pulse_cnt[q]>0: 
                        pen[q] = 1
                        arr[q] = (self.stride_angle * self.clock) / (self.ms_/2 * acc[q] * (2 * i + 1))
                        pnt[q] = int((self.ms_ * self.ms_/2 * acc[q] * (2 * i + 1)) / self.stride_angle)
                        if pnt[q]>0: arr[q] = int(self.ms_ / pnt[q]*self.clock)
                        else:
                            pen[q] = 0
                            arr[q] = int(self.clock*self.ms_)
                            pnt[q] = 1     
                    if pulse_cnt[q]<0: 
                        pen[q] = 1
                        arr[q] = (self.stride_angle * self.clock) / (self.ms_/2 * acc[q] * (2 * i + 1))
                        pnt[q] = int((self.ms_ * self.ms_/2 * acc[q] * (2 * i + 1)) / self.stride_angle)
                        if pnt[q]>0: 
                            arr[q] = int(self.ms_ / pnt[q]*self.clock)
                            pnt[q] = -pnt[q]
                        else:
                            pen[q] = 0
                            arr[q] = int(self.clock*self.ms_)
                            pnt[q] = 1      
                    if pulse_cnt[q]==0:
                        pen[q] = 0
                        arr[q] = int(self.clock * self.ms_)
                        pnt[q] = 1      
                self.cmd_queue_put((arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3]))  # send command
                print('添加命令 - ', arr[0], pnt[0], pen[0], arr[1], pnt[1], pen[1], arr[2], pnt[2], pen[2], arr[3], pnt[3], pen[3])
                arr_1.append(arr[0])
                arr_2.append(arr[1])
                arr_3.append(arr[2])
                arr_4.append(arr[3])
                pnt_1.append(pnt[0])
                pnt_2.append(pnt[1])
                pnt_3.append(pnt[2])
                pnt_4.append(pnt[3])
                pen_1.append(pen[0])
                pen_2.append(pen[1])
                pen_3.append(pen[2])
                pen_4.append(pen[3])
                for w in range(4):
                    pnt_sum[w] = pnt_sum[w] + abs(pnt[w]*pen[w])

            for i in range(4):
                pnt_ave[i] = pcnt[i]-2*pnt_sum[i]
                t_ave[i] = run_time - n*self.ms_*2                
            i_not0 = self.find_first_nonzero_index(pnt_ave)
            if  i_not0  is not  None:
                for i in range(4):
                    if (pulse_cnt[i] != 0):
                        if(pulse_cnt[i]>0):
                            arr_ave[i] = int(t_ave[i]/pnt_ave[i]*self.clock)
                            pen_ave[i] = 1
                        if(pulse_cnt[i]<0):
                            arr_ave[i] = int(t_ave[i]/pnt_ave[i]*self.clock)
                            pen_ave[i] = 1
                            pnt_ave[i] = -pnt_ave[i]
                for i in range(4):
                    if (pulse_cnt[i] == 0):
                        arr_ave[i] = arr_ave[i_not0]
                        pnt_ave[i] = pnt_ave[i_not0]
                        pen_ave[i] = 0
            a = int(abs(pnt_ave[0]) / 30000)
            if pnt_ave[0] >=0:
                for i in range(a):
                    self.cmd_queue_put((arr_ave[0], 30000, pen_ave[0], arr_ave[1], 30000, pen_ave[1], arr_ave[2], 30000, pen_ave[2], arr_ave[3], 30000, pen_ave[3]))  # send command
                    print('添加命令 - ', arr_ave[0], 30000, pen_ave[0], arr_ave[1], 30000, pen_ave[1], arr_ave[2], 30000, pen_ave[2], arr_ave[3], 30000, pen_ave[3])
                self.cmd_queue_put((arr_ave[0], pnt_ave[0]-a*30000, pen_ave[0], arr_ave[1], pnt_ave[0]-a*30000, pen_ave[1], arr_ave[2], pnt_ave[0]-a*30000, pen_ave[2], arr_ave[3], pnt_ave[0]-a*30000, pen_ave[3]))  # send command
                print('添加命令 - ', arr_ave[0], pnt_ave[0]-a*30000, pen_ave[0], arr_ave[1], pnt_ave[0]-a*30000, pen_ave[1], arr_ave[2], pnt_ave[0]-a*30000, pen_ave[2], arr_ave[3], pnt_ave[0]-a*30000, pen_ave[3])
            else:
                for i in range(a):
                    self.cmd_queue_put((arr_ave[0], -30000, pen_ave[0], arr_ave[1], 30000, pen_ave[1], arr_ave[2], 30000, pen_ave[2], arr_ave[3], 30000, pen_ave[3]))  # send command
                    print('添加命令 - ', arr_ave[0], -30000, pen_ave[0], arr_ave[1], 30000, pen_ave[1], arr_ave[2], 30000, pen_ave[2], arr_ave[3], 30000, pen_ave[3])
                self.cmd_queue_put((arr_ave[0], pnt_ave[0]-a*(-30000), pen_ave[0], arr_ave[1], pnt_ave[0]-a*(-30000), pen_ave[1], arr_ave[2], pnt_ave[0]-a*(-30000), pen_ave[2], arr_ave[3], pnt_ave[0]-a*(-30000), pen_ave[3]))  # send command
                print('添加命令 - ', arr_ave[0], pnt_ave[0]-a*(-30000), pen_ave[0], arr_ave[1], pnt_ave[0]-a*(-30000), pen_ave[1], arr_ave[2], pnt_ave[0]-a*(-30000), pen_ave[2], arr_ave[3], pnt_ave[0]-a*(-30000), pen_ave[3])
            for i in range(n):
                self.cmd_queue_put((arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i]))  # send command
                print('添加命令 - ', arr_1[n-1-i], pnt_1[n-1-i], pen_1[n-1-i], arr_2[n-1-i], pnt_2[n-1-i], pen_2[n-1-i], arr_3[n-1-i], pnt_3[n-1-i], pen_3[n-1-i], arr_4[n-1-i], pnt_4[n-1-i], pen_4[n-1-i])
        else:
            i_not0 = self.find_first_nonzero_index(pcnt)
            if  i_not0  is not  None:
                for i in range(4):
                    if (pcnt[i] != 0):
                            arr[i] = int(run_time/pcnt[i]*self.clock)
                            pen[i] = 1
                for i in range(4):
                    if (pulse_cnt[i] == 0):
                        arr[i] = arr[i_not0]
                        pulse_cnt[i] = pulse_cnt[i_not0]
                        pen[i] = 0
                self.cmd_queue_put((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                print('添加命令 - ', arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])
        self.z0 = endz
        print('命令缓冲区中命令数量 = ', self.cmd_queue.qsize())
        self.ms_=int(self.ms_*3)

    def parse_gcode(self,path):
    # 打开 GCode 文件进行读取
        with open(path, 'rb') as file:
            # 逐行读取文件内容
            for line in file:
                # 去除行末的换行符并按空格分割行内容
                tokens = line.strip().split()
                #print (tokens)
                # 遍历行中的每个单词
                for token in tokens:
                    #print(token)
                    # 检查是否为 G 指令
                    if token.startswith(b'G'):
                        # 提取指令类型和坐标信息
                        g_type = token[1:]  # 提取 G 指令类型
                        coordinates = []    # 用于存储坐标信息的列表
                        # 遍历剩余的单词，提取坐标信息
                        for sub_token in tokens[1:]:
                            #print(sub_token)
                            #print(sub_token[0])  x = 88
                            if sub_token.startswith(b'X'):
                                # 提取坐标值并添加到列表中
                                #print("sub_token starts with 'X'")
                                coordinates.append(float(sub_token[1:].decode()))
                            if sub_token.startswith(b'Y'):
                                # 提取坐标值并添加到列表中
                                #print("sub_token starts with 'Y'")
                                coordinates.append(float(sub_token[1:].decode()))
                            if sub_token.startswith(b'Z'):
                                # 提取坐标值并添加到列表中
                                #print("sub_token starts with 'Z'")
                                coordinates.append(float(sub_token[1:].decode()))
                            if sub_token.startswith(b'P'):
                                # 提取坐标值并添加到列表中
                                #print("sub_token starts with 'P'")
                                coordinates.append(float(sub_token[1:].decode()))
                        # 输出 G 指令类型和坐标信息
                '''if int(g_type) == 0 :
                #    self.movep(self.x0,self.y0,(coordinates[1]+20)*10+160,(coordinates[0]-18)*10)
                    self.movep(self.x0,self.y0,coordinates[1]+160,coordinates[0])
                #    print(coordinates[1],coordinates[0])
                if int(g_type) == 1 :
                #    self.movel(self.x0,self.y0,(coordinates[1]+20)*10+160,(coordinates[0]-18)*10)
                    self.movel1(self.x0,self.y0,coordinates[1]+160,coordinates[0])
                #    print(coordinates[1],coordinates[0])
                if int(g_type) == 2 :
                    self.movez(self.z0,coordinates[0])
                if int(g_type) == 4 :
                    time.sleep(coordinates[0]/1000)'''
                if int(g_type) == 0 :
                    self.movep(self.x0,self.y0,coordinates[0],coordinates[1])
                if int(g_type) == 1 :
                    self.movel1(self.x0,self.y0,coordinates[0],coordinates[1])
                if int(g_type) == 2 :
                    self.movez(self.z0,coordinates[0])
                if int(g_type) == 4 :
                    self.cmd_queue_sync()

    # 广播启动
    def braodcast_start(self, pulse_cnt1, pulse_cnt2, pulse_cnt3, pulse_cnt4, run_time):
        arr1 = int(run_time * self.clock / abs(pulse_cnt1))
        arr2 = int(run_time * self.clock / abs(pulse_cnt2))
        arr3 = int(run_time * self.clock / abs(pulse_cnt3))
        arr4 = int(run_time * self.clock / abs(pulse_cnt4))
        pen = 1
        self.all_motor_run((arr1, pulse_cnt1, pen, arr2, pulse_cnt2, pen, arr3, pulse_cnt3, pen, arr4, pulse_cnt4, pen))  # send command

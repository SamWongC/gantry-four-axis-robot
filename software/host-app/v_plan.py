from cmath import sqrt
from time import time


class v_plan():

    arr0 = 2160000     #w0=0.005 °/ms
    arrN = 30000       #wmax=0.36 °/ms
    arr_acceleration = 5325 #额定arr加速度，第401个脉冲达到最大速度
    
    class bigblock:
        def __init__(self, arr0, arrn, acc_pnt, ave_pnt, dec_pnt):
            self.arr0 = arr0
            self.arrn = arrn
            self.acc_pnt = acc_pnt
            self.ave_pnt = ave_pnt
            self.dec_pnt = dec_pnt


    def movel_clicked(self,start_x,start_y,end_x,end_y):
        startx = start_x
        starty = start_y
        endx = end_x
        endy = end_y
        dis  = sqrt((endy-starty) ** 2 + (endx-startx) ** 2)
        steps = int(dis /2 + 1)
        deltaX = (endx-startx)/float(steps-1)
        deltaY = (endy-starty)/float(steps-1)                                                                                                       

        currentx = startx
        currenty = starty

        for i in range(0, steps-1):
            pulse_cnt  = self.point_to_point(self, currentx, currenty, currentx + deltaX, currenty + deltaY)
            arr = [0, 0, 0, 0]
            pen = [0, 0, 0, 0]
            i_not0 = self.find_first_nonzero_index(pulse_cnt)
            if  i_not0  is not  None:
                for i in range(4):
                    if (pulse_cnt[i] != 0):
                        arr[i] = int(pulse_cnt[4] * self.clock / abs(pulse_cnt[i]))
                        pen[i] = 1
                for i in range(4):
                    if (pulse_cnt[i] == 0):
                        arr[i] = arr[i_not0]
                        pulse_cnt[i] = pulse_cnt[i_not0]
                        pen[i] = 0
                currentx += deltaX
                currenty += deltaY    
                print(arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3])
                #self.serial.all_motor_run((arr[0], pulse_cnt[0], pen[0], arr[1], pulse_cnt[1], pen[1], arr[2], pulse_cnt[2], pen[2], arr[3], pulse_cnt[3], pen[3]))  # send command
                time.sleep(0.001)
        self.x = endx
        self.y = endy


    
    def parse_gcode():
    # 打开 GCode 文件进行读取
        with open("C://Users//马添源//Desktop//333.txt", 'rb') as file:
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
                if int(g_type) == 0 or int(g_type) == 1:
                    print(int(g_type),coordinates[0],coordinates[1])
                if int(g_type) == 2 or int(g_type) == 4:
                    print(int(g_type),coordinates[0])

    
    
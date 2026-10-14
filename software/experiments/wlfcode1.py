from scara_serial import  SCARA_Serial    

robot = SCARA_Serial( 254,  0xD1)   

robot.get_ports()    

robot.open_port('/dev/ttyACM0')   

#z axis up
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))


#move to the position of @GUI 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2000, 32, 1, 6400, -10, 1,1000, 64, 0))

#1st step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 6400, -10, 1,1000, 64, 0))
arr = 250
pcnt =   -256    
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, 12, 1, 5333, 12, 1,1000, 64, 0))

#2nd step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4923, -13, 1,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4000, -16, 1, 12000, 5, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3200, 20, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 6400, 10, 1, 9143, 7, 1,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 6400, -10, 1, 9143, -7, 1,1000, 64, 0))

#4th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 6400, 10, 1, 10667, -6, 1,1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 32000, -2, 1,1000, 64, 0))

#5th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, -18, 1, 1000, 64, 0,1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 6400, -10, 1,1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 1000, 64, 0,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, -12, 1, 12800, 5, 1, 1000, 64, 0))

#6th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, 12, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 12800, 5, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1,1000, 64, 0))

#7th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0,1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 7111, -9, 1,1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, -3, 1, 1000, 64, 0,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))


#move to the position of @GE1 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2667, -24, 1, 1000, 64, 0, 1000, 64, 0))

#1st step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4923, -13, 1,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 32000, 2, 1, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, 9, 1, 12800, -5, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2133, -30, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, -3, 1, 5333, -12, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4923, 13, 1, 12800, 5, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 9143, -7, 1, 21333, -3, 1, 1000, 64, 0))

#5th step
arr = 250
pcnt =   256
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 10667, -6, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 5333, 12, 1,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, -12, 1, 12800, -5, 1, 1000, 64, 0))

#6th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, 9, 1, 4267, -15, 1, 1000, 64, 0))
arr = 250
pcnt =   -256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))

#7th step
arr = 250
pcnt =   256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, 12, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, 11, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, -12, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, -11, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256    
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to the position of @YAN 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, -17, 1, 4267, -10, 1, 1000, 64, 0))

#1st step
arr = 250
pcnt =   256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 3556, -18, 1, 1000, 64, 0))
arr = 250
pcnt =   -256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 4000, 16, 1, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256    
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, 3, 1, 21333, -3, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, 3, 1, 64000, -1, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256     
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, -11, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256    
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256    
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, 11, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, -3, 1, 64000, -1, 1, 1000, 64, 0))

#5th step
arr = 250
pcnt =   256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 12800, -5, 1, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))

#6th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 3556, 18, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4923, 13, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 12800, 5, 1, 21333, 3, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to the position of @GE2 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2286, -28, 1, 2462, -26, 1, 1000, 64, 0))

#1st step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4923, -13, 1,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 32000, 2, 1, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, 9, 1, 12800, -5, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2133, -30, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, -3, 1, 5333, -12, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4923, 13, 1, 12800, 5, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 9143, -7, 1, 21333, -3, 1, 1000, 64, 0))

#5th step
arr = 250
pcnt =   256
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 10667, -6, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 5333, 12, 1,1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, -12, 1, 12800, -5, 1, 1000, 64, 0))

#6th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, 9, 1, 4267, -15, 1, 1000, 64, 0))
arr = 250
pcnt =   -256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))

#7th step
arr = 250
pcnt =   256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, 12, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, 11, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, -12, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, -11, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256    
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))


#move to the position of @GONG 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2560, 25, 1, 508, 126, 1, 1000, 64, 0))

#1st step
arr = 250
pcnt =   256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, -12, 1, 1000, 64, 0))
arr = 250
pcnt =   -256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, 3, 1, 64000, -1, 1, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4000, -16, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2560, 25, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, -3, 1, 32000, 2, 1, 1000, 64, 0))    
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 2667, 24, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4923, -13, 1, 6400, -10, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, -11, 1, 10667, 6, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3368, 19, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, 11, 1, 10667, -6, 1, 1000, 64, 0))

#5th step
arr = 250
pcnt =   256   
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4923, -13, 1, 10667, -6, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2560, -25, 1, 1000, 64, 0, 1000, 64, 0)) 
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to the position of @FU 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 2462, -26, 1, 1000, 64, 0))

#1st step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3048, 21, 1, 6400, 10, 1, 1000, 64, 0)) 
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2783, -23, 1, 1000, 64, 0, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 3200, -20, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, -9, 1, 12800, 5, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4923, 13, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, 12, 1, 9143, -7, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3048, 21, 1, 4923, -13, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to the position of @DAO 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1939, -33, 1, 10667, -6, 1,  1000, 64, 0))

#1st step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5818, -11, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 10667, 6, 1, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, 9, 1, 9143, 7, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4267, -15, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 32000, -2, 1, 64000, 1, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 12800, 5, 1, 21333, -3, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 32000, -2, 1, 7111, 9, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 3556, 18, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, -11, 1, 12800, 5, 1, 1000, 64, 0))

#5th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 6400, -10, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 10667, 6, 1, 1000, 64, 0, 1000, 64, 0))

#6th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 9143, 7, 1, 7111, 9, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 3556, -18, 1, 1000, 64, 0))

#7th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, 3, 1, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2000, -32, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 9143, 7, 1, 9143, 7, 1, 1000, 64, 0))

#8th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, 12, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to the position of @JIA 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 2560, -25, 1, 2560, -25, 1, 1000, 64, 0))

#1st step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 32000, 2, 1, 32000, -2, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 32000, 2, 1, 6400, 10, 1, 1000, 64, 0))

#2nd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 12800, 5, 1, 32000, 2, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 32000, -2, 1, 32000, -2, 1, 1000, 64, 0))

#3rd step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 2783, -23, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 32000, 2, 1, 32000, 2, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 21333, 3, 1, 1000, 64, 0))

#4th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 4267, 15, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#5th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4923, 13, 1, 7111, 9, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 6400, -10, 1, 8000, -8, 1, 1000, 64, 0))

#6th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 21333, 3, 1, 10667, -6, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4267, 15, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 7111, 9, 1, 10667, 6, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256  
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 10667, -6, 1, 1000, 64, 0, 1000, 64, 0))

#7th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 4267, -15, 1, 6400, -10, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 9143, 7, 1, 1000, 64, 0, 1000, 64, 0))

#8th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5818, 11, 1, 8000, 8, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 9143, -7, 1, 4267, -15, 1, 1000, 64, 0))

#8th step
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, 8, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 1000, 64, 0, 1000, 64, 0))


#move to the numbers
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1280, 50, 1, 582, 110, 1, 1000, 64, 0))

#student number 1
#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, -4, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#6
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 6400, -10, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#3
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to the student number2
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 889, 72, 1, 1000, 64, 0))

#student number 2
#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, -4, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#8
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#3
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to student number3
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, 12, 1, 889, 72, 1, 1000, 64, 0))

#student number 3
#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, -4, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, -12, 1, 1000, 64, 0))

#5
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#8
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 5333, -12, 1, 1000, 64, 0))

#6
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to student number4
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 889, 72, 1, 1000, 64, 0))

#student number 4
#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, -4, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#7
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, -4, 1, 1000, 64, 0))

#8
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#8
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move to student number5
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 5333, 12, 1, 889, 72, 1, 1000, 64, 0))

#student number 5
#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 16000, -4, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#2
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 8000, -8, 1, 1000, 64, 0))

#1
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 10667, -6, 1, 1000, 64, 0))

#8
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#0
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, 4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, -8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

#move 
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 8000, -8, 1, 1000, 64, 0))

#4
arr = 250
pcnt =   256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, 4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 1000, 64, 0, 16000, -4, 1, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 16000, -4, 1, 1000, 64, 0, 1000, 64, 0))
for i in range(200):
    robot.cmd_queue_put((1000, 64, 0, 8000, 8, 1, 1000, 64, 0, 1000, 64, 0))
arr = 250
pcnt =   -256 
for i in range(200):
    robot.cmd_queue_put((arr, pcnt, 1, arr, pcnt, 0, arr, pcnt, 0,arr, pcnt, 0))

robot.cmd_queue_sync()

robot.cmd_run_start()
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
import pandas as pd
import time

libr_office = "coordRead.xlsx"
df = pd.read_excel(libr_office)


length = len(df) - 1







x_coord = df.iloc[0,0]
y_coord = df.iloc[0,1]
z_coord = df.iloc[0,2]




mySpeed = 20



mc = MyCobot('/dev/ttyAMA0',115200)
mc.power_on()



initilization_angle = [0, -25, -90, 30, 90, 90]



mc.send_angles(initilization_angle, mySpeed)


while 1:
            if mc.is_moving() == 0:
                break 

time.sleep(1) 
#time.sleep(5)                
read = mc.get_coords()
time.sleep(2)

vyska = 100

help_coord = [read[0], read[1], vyska ,read[3], read[4],read[5]] 
#help_coord = [264.1, -88.2, 90, -177.71, 0.26, -90.16]
mc.send_coords(help_coord, 20, 1)


while 1:
            if mc.is_moving() == 0:
                break 




print(read)




for i in range(4):
                
    x_coord = df.iloc[i,0]
    y_coord = df.iloc[i,1]
    z_coord = df.iloc[i,2]
    
    

    read_coord = [read[0] + x_coord, read[1] + y_coord, vyska ,read[3], read[4],read[5]]
    print(i,read_coord)
    mc.send_coords(read_coord, 5, 0)
    
    time.sleep(5)
    
    





















"""
for i in range(5):
pickup_angle = [-45, 52, 0, 0]

#dropoff_angle = [45, 47, 0, 0]


count = 0
mc.send_angles(initilization_angle, mySpeed)

"""


"""




for i in range(6):
    
    dropoff_angle = [45, 52 + (i * -12), 0 , 0]    
  
    while 1:
            if mc.is_moving() == 0:
                break    
    

    mc.send_angles(pickup_angle, mySpeed)       
    while 1:
            if mc.is_moving() == 0:
                break
    time.sleep(1) 
    pickUpPos = mc.get_coords()    
    GPIO.output(20,GPIO.LOW)
    time.sleep(1)
        
       
    while 1:
        if mc.is_moving() == 0:
            break   

    mc.send_angles(initilization_angle, mySpeed)    

             
    while 1:
        if mc.is_moving() == 0:
            break   

    #mc.send_coord(Coord.Y.value, pickUpPos[1] * -1 ,20)
    
    mc.send_coords([pickUpPos[0],pickUpPos[1] * -1, pickUpPos[2] + (i * 25),pickUpPos[3]],20,1)

    while 1:
        if mc.is_moving() == 0:
            break   

        
    time.sleep(1)
    GPIO.output(20,GPIO.HIGH)
    time.sleep(1)
    
    while 1:
        if mc.is_moving() == 0:
            break 
    
    mc.send_coords([pickUpPos[0],pickUpPos[1] * -1, pickUpPos[2] + (i * 25)+10,pickUpPos[3]],20,1)
                
    while 1:
        if mc.is_moving() == 0:
            break   
                 
    mc.send_angles(initilization_angle, mySpeed)

ActualCoords = mc.get_angles()

print(ActualCoords)



time.sleep(3)
"""




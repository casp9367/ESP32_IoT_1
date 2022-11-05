from machine import Pin,ADC, I2C
from time import sleep
from imu import MPU6050
import tm1637
import _thread

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)

tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

tm.number(0)

def faldcount():
    fald1 = False

    x2 = False

    faldCounter = 0
        
    while True:
        # reading values
        acceleration = imu.accel
        gyroscope = imu.gyro  
        print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
               "z: ", round(acceleration.z,2))

        print ("gyroscope x: ", round(gyroscope.x,2), " y:", round(gyroscope.y,2),
               "z: ", round(gyroscope.z,2))

    # data interpretation (accelerometer)

        

        if abs(acceleration.x) > 0.4:
            if (acceleration.x > 0):
                print("The x axis points upwards")
                
            else:
                print("The x axis points downwards")

        if abs(acceleration.y) > 0.4:
            if (acceleration.y > 0):
                print("The y axis points upwards")
            else:
                print("The y axis points downwards")

        if abs(acceleration.z) > 0.4:
            if (acceleration.z > 0):
                print("The z axis points upwards")
                fald1 = False
            else:
                print("The z axis points downwards")
                fald1 = True
                
                
        if ((fald1 == True) and (x2 == False)):
            faldCounter = faldCounter + 1
            x2 = True
#             print("her")
            tm.number(faldCounter)
            
        if fald1 == 0:
            x2 = False
#             print("nu her")
            
        print(faldCounter)
    # data interpretation (gyroscope)

        if abs(gyroscope.x) > 20:
            print("Rotation around the x axis")

        if abs(gyroscope.y) > 20:
            print("Rotation around the y axis")

        if abs(gyroscope.z) > 20:
            print("Rotation around the z axis")
        
        sleep(0.1)
        
_thread.start_new_thread(faldcount,())
import matplotlib.pyplot as plt
import serial
import time

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
time.sleep(3)

    
x = []
y = []
i = 0
while 1:
    
        
        x.append(i)
        arduinooutput = ser.readline().decode().split('\r\n')[0]
        y.append(float(arduinooutput))
        plt.plot(x,y)
        # conditional statements can be commented out if wanted to keep plot stable
        if i < 10:
            #plt.xlim(0,10) # way to keeps all data
            pass # way where old data is dropped
        else:
            #plt.xlim(i-10,i+1) # way to keep all data
            x.pop(0) #way where old data is dropped
            y.pop(0) #way where old data is dropped
        plt.ylim(80,100) # if moving plot is done, so y limit isn't constantly changed, can be changed to see arduino output range
        plt.show()
        i += 1
        plt.pause(0.0001)
        


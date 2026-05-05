#!/usr/bin/python
import serial
import re
import sys
import subprocess

port = '/dev/ttyUSB0'
baud = 57600
timeout = 60
retry = 3
meter = serial.Serial(port, baud, timeout=timeout)
#print(meter)
while True:

        data = meter.readline().decode("ascii").strip() #readline reads a string terminated by \n
        #print(data)

        try:
                watts_ex = re.compile('<watts>([0-9]+)</watts>')
                temp_ex = re.compile('<tmpr>([\ ]?[0-9\.]+)</tmpr>') # when temperature is less than 10, currentcost adds a space before the number
                time_ex = re.compile('<time>([0-9\.\:]+)</time>')

                watts = str(int(watts_ex.findall(data)[0])) # cast to and from int to strip leading zeros
                temp = temp_ex.findall(data)[0] # remove that extra space
                time = time_ex.findall(data)[0]

                #print(watts)
                #print(temp)
                #print(time)
                subprocess.run(['./current.sh', watts, temp])
        except:
                #sys.stderr.write("Could not get details from device\n")
                pass
#               meter.close()
#       sys.exit()
#print(watts)
meter.close()

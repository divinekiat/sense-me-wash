import serial
import csv
import time

with open('data.csv','r') as f:
    reader=csv.reader(f)
    init_values=list(reader)
    init_values=init_values[0]
    init_values=list(map(int, init_values))
print(init_values)

try:
    arduino=serial.Serial("COM8", timeout=1, baudrate=9600)
except:
    print('Problem connecting with port')
    
count=0

while True:
    rawdata=str(arduino.readline())
    cleandata=rawdata[2:len(rawdata)-5]
    
    if count==50:
        cleandata_list=cleandata.split(",")
        combined_data=[]
        combined_data.append(int(cleandata_list[0])+init_values[0])
        combined_data.append(int(cleandata_list[1])+init_values[1])
        combined_data.append(int(cleandata_list[2])+init_values[2])
        to_print=str(combined_data[0])+","+str(combined_data[1])+","+str(combined_data[2])
        file=open('data.csv',mode='w')
        file.write(to_print)
        file.close()
        print(to_print)
        count=0
    count+=1
    
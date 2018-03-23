import serial
import csv

with open('data.csv','r') as f:
    reader=csv.reader(f)
    init_values=list(reader)
    init_values=init_values[0]
    init_values=list(map(int, init_values))
print(init_values)

try:
    arduino=serial.Serial("COM7", timeout=1, baudrate=9600)
except:
    print('Problem connecting with port')
    
count=0

while True:
    rawdata=str(arduino.readline())
    cleandata=rawdata[2:7]
    if count==50:
        cleandata_list=cleandata.split(",")
        cleandata_list=list(map(int,cleandata_list))
        combined_data=[str(sum(x)) for x in zip(cleandata_list, init_values)]
        combined_data=str(combined_data)
        to_print=combined_data[2]+","+combined_data[7]+","+combined_data[12]
        print(to_print)
        file=open('data.csv',mode='w')
        file.write(to_print)
        file.close()
        print(to_print)
        count=0
    count+=1
    
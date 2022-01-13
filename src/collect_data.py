import serial
import csv
from time import perf_counter 
import codecs


arduino_port = "/dev/cu.usbmodem14101"
baud = 230400
fileName = "one_sensor_with_cables_test_1ms_rest_realtime.csv"

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port : " + arduino_port)
data = []

#let's count ourselves since I do not know how much time the Arduino takes to read and print
try: 
    tic2 = perf_counter()
    while True: 
        #display the data to the terminal, one sensor
        # tic = perf_counter()
        # getData = ser.readline()
        # toc = perf_counter()
        # print(toc-tic)
        # # #datum = int(getData.decode())*(5/1023)*1000 #convert into mV
        # datum = int(getData.decode())
        # row = [datum, time] 
        # data.append(row)
        
        
        # # #time = time + 10
        # # print(datum)

        #multiple sensors


        getData = ser.readline()
        getData = getData.decode()[:-2]
        # values = getData.decode()[:-2] #Il faut checker les caractères caca
        # values = values.split(',')
        # for value in values:
        #     value = int(value)*(5/1023)*1000 #to convert into mV
        #print(values)
        #data.append((ser.readline()).decode()[:-2])
        data.append(getData)
        
except KeyboardInterrupt:
    toc2 = perf_counter()
    print("Data collection complete !")
    print(toc2-tic2)
    
with open(fileName, "w") as csvfile:
    #header = ['Potential [mV]', 'Time [ms]']
    header = ['Potential 1 [mV]', 'Potential 2 [mV]', 'Potential 3 [mV]', 'Potential 4 [mV]', 'Potential 5 [mV]', "Potential 6 [mV]", 'Time [us]']
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    for i in data:
        i = i.split(',')
        for value in i[:-1]:
            value = int(value)*(5/1023)*1000 #to convert into mV
        csv_writer.writerow(i)
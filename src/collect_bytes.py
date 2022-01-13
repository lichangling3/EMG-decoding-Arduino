import serial
import csv
from time import perf_counter 
import numpy as np

arduino_port = "/dev/cu.usbmodem14101"
baud = 230400
# fileName = "one_sensor_with_cables_test3_contraction.csv"
fileName = "test_withoutlsl.csv"

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port : " + arduino_port)
bytesArray = []
data = []

#let's count ourselves since I do not know how much time the Arduino takes to read and print
try: 
    tic2 = perf_counter()
    while True: 
        #display the data to the terminal, one sensor
        datum = ser.read(16) #type of datum is bytes which is a sequence of single bytes
        bytesArray.append(datum)
        
except KeyboardInterrupt:
    toc2 = perf_counter()
    print("Data collection complete !")
    print(toc2-tic2)

#Read the bytes
for datum in bytesArray:
    datum = list(datum)
    valeur1 = int.from_bytes(datum[:2], byteorder = 'big')
    valeur2 = int.from_bytes(datum[2:4], byteorder = 'big')
    valeur3 = int.from_bytes(datum[4:6], byteorder = 'big')
    valeur4 = int.from_bytes(datum[6:8], byteorder = 'big')
    valeur5 = int.from_bytes(datum[8:10], byteorder = 'big')
    valeur6 = int.from_bytes(datum[10:12], byteorder = 'big')
    temps = int.from_bytes(datum[12:16], byteorder = 'big')

    data.append([valeur1, valeur2, valeur3, valeur4, valeur5, valeur6, temps])

with open(fileName, "w") as csvfile:
    header = ['Potential 1 [mV]', 'Potential 2 [mV]', 'Potential 3 [mV]', 'Potential 4 [mV]', 'Potential 5 [mV]', "Potential 6 [mV]", "Times [us]"]
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    for i in data:
        for value in i[:-1]:
            value = value*(5/1023)*1000 #to convert into mV
        csv_writer.writerow(i)

# np.savetxt("student.csv",data, delimiter =" ",  fmt ='% s') 
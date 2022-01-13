import serial
import time

arduino_port = "/dev/cu.usbmodem14101"
baud = 230400

ser = serial.Serial(arduino_port, baud, timeout = 3)
print("Connected to Arduino port : " + arduino_port)

try: 
    while True: 
        T_a = time.time_ns()
        # ser.write(b'\x00\x00\x00\x00\x00\x16\x00/\x007\x00>\x00\x08\x7f\xd8')
        ser.write("hellohellohelloo".encode())
        
        test = ser.read(16).decode()
        T_b = time.time_ns()
        print((T_b - T_a)/2)
except KeyboardInterrupt:
    print("Data collection complete !")

import serial
from pylsl import StreamInfo, StreamOutlet

baud = 230400

#Ask the user the Arduino port
while True:
    arduino_port = input("Indicate the Arduino port that you can find in Arduino IDE > Tools : ")
    if "COM" in arduino_port or "/dev/" in arduino_port:
        try:
            ser = serial.Serial(arduino_port, baud)
            break
        except serial.serialutil.SerialException:
            print('Invalid. Either the Arduino is not connected or the port is false. It should be like "COMx" on Windows or "/dev/xxx.." on Mac or Linux.')
    else:
        print('Wrong port. It should be like "COMx" on Windows or "/dev/xxx.." on Mac or Linux.')

valid_options = ['raw', 'sig', 'both']
#The user can choose between raw EMG data, EMG envelope or both to send in the streams
while True:
    choice = input("Please indicate if you want the raw signal, the EMG envelope (sig) or both : raw/sig/both ? ")
    if choice in valid_options:
        break
    else:
        print('Not a valid option. Valid options are: ', ",".join(valid_options))

nb_ch = 6
#only one stream will be created if the user chose raw of 
if choice == "raw" or choice == "sig":
    name_stream = 'Myoware_' + choice
    info = StreamInfo(name=name_stream, type='EMG', nominal_srate = 1000, channel_count=nb_ch, channel_format='double64')
    outlet = StreamOutlet(info)
    print("Sending data in the stream " + name_stream + "...")
    if choice == "raw":
        try:
            while True: 
                datum = ser.read(24) #type(datum) = bytes
                datum = list(datum)
                raw_values = [int.from_bytes(datum[i*2:(i+1)*2], byteorder = 'big')*(5/1023) for i in range(6)]
                outlet.push_sample(raw_values)
        except KeyboardInterrupt:
            print("Data collection complete !")
    else:
        try:
            while True: 
                datum = ser.read(24) #type(datum) = bytes
                datum = list(datum)
                sig_values = [int.from_bytes(datum[(i+6)*2:(i+7)*2], byteorder = 'big')*(5/1023) for i in range(6)]
                outlet.push_sample(sig_values)
        except KeyboardInterrupt:
            print("Data collection complete !")
else:
    info_raw = StreamInfo(name='Myoware_raw', type='EMG', nominal_srate = 1000, channel_count=nb_ch, channel_format='double64')
    outlet_raw = StreamOutlet(info_raw)

    info_sig = StreamInfo(name='Myoware_sig', type='EMG', nominal_srate = 1000, channel_count=nb_ch, channel_format='double64')
    outlet_sig = StreamOutlet(info_sig)
    print("Sending data in the streams Myoware_raw and Myoware_sig...")
    try:
        while True: 
            datum = ser.read(24) #type(datum) = bytes
            datum = list(datum)
            raw_values = [int.from_bytes(datum[i*2:(i+1)*2], byteorder = 'big')*(5/1023) for i in range(6)]
            sig_values = [int.from_bytes(datum[(i+6)*2:(i+7)*2], byteorder = 'big')*(5/1023) for i in range(6)]
            outlet_raw.push_sample(raw_values)
            outlet_sig.push_sample(sig_values)
    except KeyboardInterrupt:
        print("Data collection complete !")

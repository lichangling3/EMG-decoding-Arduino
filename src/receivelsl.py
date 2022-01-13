from pylsl import StreamInlet, resolve_streams
import csv
import time
import numpy as np

#Mtn on va voir si j'arrive à choper les bons data
info_inlets = resolve_streams(wait_time=1.0)

#info_inlets[0] car il y a seulement un unique stream ouvert par moi-même
inlet = StreamInlet(info_inlets[0])
data = []
# T2 = []
T3 = []

print('Found:',[inlet.name() for inlet in info_inlets])

try:
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        # sample, timestamp = inlet.pull_sample()
        chunk, timestamps = inlet.pull_chunk(max_samples = 2000)
        T3.append(time.time())
        # T2.append(timestamps) #in seconds
        # data.append(sample) #in seconds       
        # T2.extend(timestamps)
        data.extend(chunk)                                                                                    
except KeyboardInterrupt:
    print("perdu stream")

np.savetxt("test_lsl.csv", data, delimiter =", ", fmt ='% s') 

# fileName = "test_lsl.csv"
# with open(fileName, "w") as csvfile:
#     header = ['Potential 1 [mV]', 'Potential 2 [mV]', 'Potential 3 [mV]', 'Potential 4 [mV]', 'Potential 5 [mV]', "Potential 6 [mV]", 'Time [us]']
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(data)

# np.savetxt("T2_lsl.csv",T2, delimiter =", ") 

# fileName = "T2_lsl.csv"
# with open(fileName, "w") as csvfile:
#     header = ['T2']
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(header)
#     for j in T2:
#         csv_writer.writerow(j)

np.savetxt("T3_lsl.csv",T3, delimiter =", ") 

# fileName = "T3_lsl.csv"
# with open(fileName, "w") as csvfile:
#     header = ['T3']
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(header)
#     for g in T3:
#         csv_writer.writerow(g)

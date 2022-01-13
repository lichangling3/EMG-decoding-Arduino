from scipy.signal import butter, lfilter, filtfilt
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import pandas as pd

#Bandpass Butterworth filter

# def butter_bandpass(lowcut, highcut, fss, order=5):
#     nyq = 0.5 * fs
#     low = lowcut / nyq
#     high = highcut / nyq
#     b, a = butter(order, [low, high], btype='bandpass', analog = False, fs = fss)
#     return b, a

# def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
#     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

# Other BPF
def bandPassFilter(signal, fs = 1000, lowcut = 15, highcut = 500):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    order = 1
    b, a = butter(order, [low, high], btype='bandpass', analog = False, fs = fs)
    outputSignal = filtfilt(b, a, signal, axis = 0) 

    return(outputSignal)

# Sample rate and desired cutoff frequencies (in Hz).
# fs = 1000
# lowcut = 15
# highcut = 500

# Filter a noisy signal.
file_name = "one_sensor_with_cables_test_1ms_rest_realtime.csv"
df = pd.read_csv(file_name)
x = df["Potential 1 [mV]"]
t = df["Time [us]"]

#T = 0.001 #every 1000ms we have a sample
#nsamples = len(x)
#t = np.linspace(0, T, nsamples, endpoint=False)
# t = np.linspace(0, T*nsamples, nsamples, endpoint = False)
plt.plot(t, x, label='Noisy signal')

#y = butter_bandpass_filter(x, lowcut, highcut, fs, order=3)
plt.plot(t, bandPassFilter(x), label='Filtered signal')
plt.xlabel('time (seconds)')
plt.grid(True)
plt.axis('tight')
plt.legend(loc='upper left')

plt.show()


from scipy.signal import butter, iirnotch, filtfilt, freqz
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import pandas as pd
from math import sqrt

def bandPassFilter(signal, fs = 1000, lowcut = 15, highcut = 495, order = 2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandpass', analog = False)
    outputSignal = filtfilt(b, a, signal) 

    return(outputSignal)

def NotchFilter(signal, fs = 1000.0, f0 = 50.0, Q = 30.0):
    # Design notch filter
    b_notch, a_notch = iirnotch(f0, Q, fs)

    # Compute magnitude response of the designed filter
    freq, h = freqz(b_notch, a_notch, fs=fs)

    outputNotch = filtfilt(b_notch, a_notch, signal)

    return(outputNotch)

# The noisy signal.
file_name = "one_sensor_with_cables_test_1ms_contraction.csv"
df = pd.read_csv(file_name)
x = df["Potential 1 [mV]"]
t = df["Time [us]"]

#rectify signal ?
#x = [sqrt(x**2) for x in df["Potential 1 [mV]"]]

plt.plot(t, x, label='Noisy signal')

#Filter Notch then BPF

notched = NotchFilter(x)
filtered_x = bandPassFilter(notched)
filtered_x = [sqrt(x**2) for x in filtered_x]

plt.plot(t, filtered_x, label='Filtered signal')
plt.xlabel('time (seconds)')
plt.grid(True)
plt.axis('tight')
plt.legend(loc='upper left')

plt.show()
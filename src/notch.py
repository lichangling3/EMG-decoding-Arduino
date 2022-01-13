from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd

# Notch filter, le pic est à 50Hz

#Defining the specifications of the IIR Bandpass Notch-Filter

fs = 1000.0  # Sample frequency (Hz)
f0 = 50.0  # Frequency to be removed from signal (Hz)
Q = 30.0  # Quality factor

# Design notch filter
b_notch, a_notch = signal.iirnotch(f0, Q, fs)

# Compute magnitude response of the designed filter
freq, h = signal.freqz(b_notch, a_notch, fs=fs)

# Apply notch filter to the noisy signal using signal.filtfilt 
file_name = "one_sensor_with_cables_test_1ms_rest_realtime.csv"
df = pd.read_csv(file_name)
x = df["Potential 1 [mV]"]
t = df["Time [us]"]

outputSignal = signal.filtfilt(b_notch, a_notch, x) 

# Plot
plt.plot(t, x, label='Noisy signal')

plt.plot(t, outputSignal, label='Filtered signal (Hz)')
plt.xlabel('time (seconds)')
plt.grid(True)
plt.axis('tight')
plt.legend(loc='upper left')
plt.show()
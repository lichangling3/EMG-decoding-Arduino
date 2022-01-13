import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, iirnotch, filtfilt, freqz
from get_SNR import get_SNR

def NotchFilter(f0, signal, fs = 1000.0, Q = 30.0):
    # Design notch filter
    b_notch, a_notch = iirnotch(f0, Q, fs)

    # Compute magnitude response of the designed filter
    #freq, h = freqz(b_notch, a_notch, fs=fs)

    outputNotch = filtfilt(b_notch, a_notch, signal)

    return(outputNotch)

#J'ai placé x>0.5 complètement arbitrairement, psk y avait plusieurs points qui formaient le pix de 50 Hz.. Bien sûr 0.5 c'est au-dessus des autres points ne faisant pas partie du pic
#To find the highest peak and the peaks around 50 Hz. The highest peak is then used to remove the harmonics
def NotchPeak(x_freq, Y_freq):
    pic_notch = [x for x in Y_freq if x > 0.5]
    peaks = []
    for peak in pic_notch:
        index_notch = np.where(Y_freq == peak)
        peaks.append(x_freq[index_notch])
    peak50 = x_freq[np.where(Y_freq == max(pic_notch))]
    return(peak50, peaks)

def bandPassFilter(signal, fs = 1000, lowcut = 15, highcut = 495, order = 2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandpass', analog = False)
    outputSignal = filtfilt(b, a, signal) 

    return(outputSignal)

def plotSpectrum(file_name, Fs, subtitle):
    """
    Plots a Single-Sided Amplitude Spectrum of y(t)
    """
    df = pd.read_csv(file_name)
    y = df["Potential 4 [mV]"]

    N = len(y) # length of the signal
    # k = np.arange(N)
    # T = N/Fs
    T = 1.0/Fs
    xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
    # frq = k/T # two sides frequency range
    # frq = frq[range(int(N/2))] # one side frequency range
    #frq = np.linspace(0.0, 1.0/(2.0*T), int(N/2))

    # Y = np.fft.fft(y)/N # fft computing and normalization
    # Y = Y[range(int(N/2))]
    Y = np.fft.fft(y)
    
    Y_freq = 2.0/N * np.abs(Y[0:int(N/2)])[1:]
    x_freq = xf[1:]
    peak50, f0_peak = NotchPeak(x_freq, Y_freq)
    # print(f0_peak)
    print(peak50)
    
    for i in range(1,10) :
        y = NotchFilter(signal = y, f0 = peak50*i)
    for peaks in f0_peak:
        y = NotchFilter(signal = y, f0 = peaks)

    y = bandPassFilter(y)
    print("Both filters :")
    get_SNR(y, 7600000, raw = True)

    Y = np.fft.fft(y)
    Y_freq = 2.0/N * np.abs(Y[0:int(N/2)])[1:]

    # #plot normal and frequency spectrum
    # fig, axs = plt.subplots(3)
    # fig.suptitle(subtitle)
    # axs[0].plot(df["Time [us]"], df["Potential 5 [mV]"], label = "Raw signal")
    # axs[0].set_xlabel("Time [us]")
    # axs[0].set_ylabel("Potential [mV]")
    # axs[0].legend()

    # axs[1].plot(df["Time [us]"], y, label = "BPF 15-495 + Notch at 50 filters")
    # axs[1].set_xlabel("Time [us]")
    # axs[1].set_ylabel("Potential [mV]")
    # axs[1].legend()

    # #axs[1].plot(frq[1:],np.abs(Y)[1:],'r') # plotting the spectrum

    # axs[2].plot(x_freq, Y_freq, 'r')
    # axs[2].set_xlabel('Freq (Hz)')
    # axs[2].set_ylabel('|Y(freq)|')
    # fig.tight_layout()

    #We rectify the raw signal
    y = [np.sqrt(x**2) for x in y]

    fig, axs = plt.subplots(2)
    subtitle = "Default and raw filtered signals with cables"
    fig.suptitle(subtitle)
    axs[0].plot(df["Time [us]"], y, label = "BPF 15-495 and Notch filters applied to the rectified signal")
    axs[0].set_xlabel("Time [us]")
    axs[0].set_ylabel("Potential [mV]")
    axs[0].legend()

    # axs[1].plot(df["Time [us]"], df["Potential 1 [mV]"], label = "Default output")
    # axs[1].set_xlabel("Time [us]")
    # axs[1].set_ylabel("Potential [mV]")
    # axs[1].legend()

    axs[1].plot(x_freq, Y_freq, 'r', label = "Frequency spectrum of the filtered raw signal")
    axs[1].set_xlabel('Freq (Hz)')
    axs[1].set_ylabel('|Y(freq)|')
    axs[1].legend()
    fig.tight_layout()

    # plt.plot(df["Time [us]"], y, label = "BPF 15-495 applied to raw signal")
    # plt.plot(df["Time [us]"], df["Potential 1 [mV]"], label = "Default output")
    # plt.title("Both signals taken at the same time")
    # plt.xlabel("Time [us]")
    # plt.ylabel("Potential [mV]")
    # plt.legend()
    plt.show()
    
    #plt.plot(frq[1:],np.abs(Y)[1:],'r') # plotting the spectrum

#Fss = 100.0  # sampling rate, 10ms in Arduino
Fss = 1000 #sampling rate, 1ms in Arduino

file = "one_sensor_with_cables_test3_contraction.csv"
name = "Raw signal, with cables, 1 contraction"
plotSpectrum(file_name = file, Fs = Fss, subtitle = name)
import pandas as pd
import numpy as np

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

file = "one_sensor_with_cables_test_1ms_contraction.csv"
df = pd.read_csv(file)
snr = signaltonoise(df["Potential 1 [mV]"])
print(snr)

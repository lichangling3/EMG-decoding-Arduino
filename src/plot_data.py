import pandas as pd
import matplotlib.pyplot as plt
from numpy import sqrt

df = pd.read_csv("test_withoutlsl.csv")
# df.plot( x = "Time [ms]", y = "Potential [mV]", kind = 'line', legend = False)
# plt.title("Raw signal, with cables, at rest")
# plt.ylabel("Potential [mV]")
# plt.show()

time = df["Time [us]"]

# fig, axs = plt.subplots(6)
# fig.suptitle("5 captors on forearm")
# axs[0].plot(time, df['Potential 1 [mV]'])
# axs[1].plot(time, df['Potential 2 [mV]'])
# axs[2].plot(time, df['Potential 3 [mV]'])
# axs[3].plot(time, df['Potential 4 [mV]'])
# axs[4].plot(time, df['Potential 5 [mV]'])
# axs[5].plot(time, df['Potential 6 [mV]'])
# plt.xlabel("Temps  [us]")
# plt.ylabel("Potential [mV]")
# fig.tight_layout()
# plt.show()

plt.plot(time, df['Potential 1 [mV]'], label = "Potential 1 [mV]")
plt.plot(time, df['Potential 2 [mV]'], label = "Potential 2 [mV]")
plt.plot(time, df['Potential 3 [mV]'], label = "Potential 3 [mV]")
plt.plot(time, df['Potential 4 [mV]'], label = "Potential 4 [mV]")
plt.plot(time, df['Potential 5 [mV]'], label = "Potential 5 [mV]")
plt.plot(time, df['Potential 6 [mV]'], label = "Potential 6 [mV]")

# plt.plot(time, data, label = "Raw signal")
#plt.title("4 sensors with cables, one without. All fingers move one by one")
# plt.title("Both signals taken at the same time")
plt.xlabel("Time [us]")
plt.ylabel("Potential [mV]")
plt.legend()
plt.show()


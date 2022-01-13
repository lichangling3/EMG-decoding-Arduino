import pandas as pd
import numpy as np
import time

#SNR for data with rest at start and then 1 long contraction
def get_SNR(data, end_rest, raw=False):
    end_index = int(end_rest/1000)

    if raw == True:
        #We apply RMS, i.e, rectified sEMG data in order to define SN ratio
        data = [np.sqrt(x**2) for x in data]
        mean_r = np.mean(data[:end_index])
        # max_rest_value = max([x**2 for x in data[:end_index]]
        print(mean_r)
        

        mean_c = np.mean(data[end_index:]) #On s'assure de prendre que les valeurs de contraction
        print(mean_c)
        
    else:
        mean_r = np.mean(data[:end_index])
        # max_rest_value = max(data[:end_index])
        print(mean_r)

        # mean_c = np.mean([x for x in data if x - max_rest_value > 0]) #On s'assure de prendre que les valeurs de contraction
        mean_c = np.mean(data[end_index:])
        print(mean_c)

    SNR = mean_c/mean_r
    print(SNR)

#Default output with potential 1, raw output with potential 5 for one_sensor_with_cables_test2_contraction.csv  4300000
#Raw one is Potential 4 for one_sensor_with_cables_test3_contraction.csv 7600000
file_name = "one_sensor_with_cables_test2_contraction.csv"
df = pd.read_csv(file_name)
end_rest = 4300000

get_SNR(df["Potential 5 [mV]"], end_rest, raw = False)
print(time.time())
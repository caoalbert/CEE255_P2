import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel
from statsmodels.stats.multicomp import pairwise_tukeyhsd


df = pd.read_csv("task2.csv")
time = df['time'].unique()
time = [i[0:4] for i in time]



name = {'s1':'100% Bottleneck',
        's2':'105% Bottleneck',
        's3':'110% Bottleneck',
        's4':'115% Bottleneck',
        's5':'120% Bottleneck'}
col = {'s1':'#90c9e6',
       's2':'#219ebc',
       's3':'#023047',
       's4':'#ffb703',
       's5':'#fb8402'}
ylabel = np.array([["Delay (sec/mi)", "Density (veh/mi)"],
                ["Flow (veh/hr)", "Harmonic Speed (mph)"]])
title = np.array([["Variation in Delay", "Variation in Density"],
                ["Variation in Flow", "Variation in Speed"]])
    
fig, ax = plt.subplots(2,2)
for i in df['sample'].unique():
    ax[0,0].plot(time, df[df['sample'] == i]['delay_time'], color = col[i], label = name[i], linewidth = 2)
    ax[0,1].plot(time, df[df['sample'] == i]['density'], color = col[i], linewidth = 2)
    ax[1,0].plot(time, df[df['sample'] == i]['flow'], color = col[i], linewidth = 2)
    ax[1,1].plot(time, df[df['sample'] == i]['harmonic_speed'], color = col[i], linewidth = 2)

for j in range(2):
    for k in range(2):
        ax[j,k].set_xlabel("Time")
        ax[j,k].set_ylabel(ylabel[j,k])
        ax[j,k].set_title(title[j,k])   
plt.figlegend(loc = "right")
plt.show()



# Paired T-Test
number_of_tests = 1+2+3+4
alpha = 0.05/number_of_tests
samples = df['sample'].unique()
for a in range(5):
    while(a < 4):
        results = ttest_rel(df[df["sample"] == samples[a]]['delay_time'], df[df["sample"] == samples[a+1]]['delay_time'])
        print(round(results[0],2), round(results[1],7))
        
        if results[1] < alpha:
            print("rejected")
        else:
            print("not rejected")
        print("\n")
        a += 1
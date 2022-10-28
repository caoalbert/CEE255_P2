import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Our bottleneck
detector_speed = pd.read_csv("detector_speed.csv")
detector_speed = detector_speed.rename(columns={'Unnamed: 0' : "position"})

ylabel = detector_speed.columns[1:].tolist()
ylabel = [i.split(" ", 1)[1] for i in ylabel]
ylabel.reverse()
xlabel = detector_speed['position'].tolist()
xlabel = [xlabel[i][0:4] for i in range(len(xlabel))]


speed_matrix = np.array(detector_speed.iloc[:,1:]).transpose()
fig1, ax1 = plt.subplots(figsize = (8,8))
mat = ax1.matshow(speed_matrix, interpolation = 'none')
fig1.colorbar(mat, orientation = "horizontal", label = "Speed (mph)")
ax1.set_title("Bottleneck Detection")
ax1.set_xticks([i for i in range(len(xlabel))], labels = xlabel)
ax1.set_yticks([i for i in range(len(ylabel))], labels = ylabel)
ax1.set_ylabel("Post-Mile")
ax1.set_xlabel("Time")
plt.show()

# Original data
detector_speed_original = pd.read_csv("detector_speed_original.csv")
detector_speed_original = detector_speed_original.rename(columns={'Unnamed: 0' : "position"})

ylabel = detector_speed_original.columns[1:].tolist()
ylabel = [i.split(" ", 1)[1] for i in ylabel]
ylabel.reverse()
xlabel = detector_speed_original['position'].tolist()
xlabel = [xlabel[i][0:5] for i in range(len(xlabel))]

speed_matrix_original = np.array(detector_speed_original.iloc[:,1:]).transpose()
fig2, ax2 = plt.subplots(figsize = (10,10))
mat2 = ax2.matshow(speed_matrix_original, interpolation = 'none')
fig2.colorbar(mat2, label = "Speed (mph)")
ax2.set_title("Bottleneck Detection - Original")
ax2.set_xticks([i for i in range(len(xlabel))], labels = xlabel)
ax2.set_yticks([i for i in range(len(ylabel))], labels = ylabel)
ax2.set_xlabel("Time")
ax2.set_ylabel("Post-Mile")
plt.show()
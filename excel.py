import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


Fs, signal = wavfile.read("Xe.wav")
n = np.arange(len(signal))
with open("Xe1_Output_mono.csv", newline='') as f_xe:
    reader = csv.reader(f_xe)
    count = -1
    x = []
    for row in reader:
        count = count + 1
        x = np.append(x, row[1])
    x = np.delete(x, 0)
    x = x.astype(np.int)
    plt.plot(x)
    plt.xlabel("Trục thời gian n")
    plt.ylabel("Trục biên độ")
    plt.title("Vẽ Xe.csv")
    plt.grid()
    plt.show()


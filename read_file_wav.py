import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

Fs, signal = wavfile.read("Xe.wav")
n = np.arange(len(signal))
t = n / Fs * 1000
plt.plot(t, signal)
plt.xlabel("Thời gian theo ms")
plt.ylabel("Biên độ")
plt.title("Tín hiệu âm thanh Xe.wav")
plt.grid()
plt.show()


from scipy.io import wavfile
import pandas as pd


Fs, signal = wavfile.read("Xe.wav")
wavData = pd.DataFrame(signal)

if len(wavData.columns) == 2:

    wavData.columns = ['R', 'L']
    stereo_R = pd.DataFrame(wavData['R'])
    stereo_L = pd.DataFrame(wavData['L'])

    stereo_R.to_csv("Xe1_Output_stereo_R.csv", mode='w')
    stereo_L.to_csv("Xe1_Output_stereo_L.csv", mode='w')

    print('Save is done ')

elif len(wavData.columns) == 1:

    wavData.columns = ['M']

    wavData.to_csv("Xe1_Output_mono.csv", mode='w')


else:

    wavData.to_csv( "Xe1_Output_multi_channel.csv", mode='w')

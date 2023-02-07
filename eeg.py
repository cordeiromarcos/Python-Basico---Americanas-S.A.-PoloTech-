import numpy as np

def process_EEG_signal(matriz):
    media=(matriz-np.mean(matriz))
    return media

x=np.random.randn(64,512)

x_processado=process_EEG_signal(x)

print(x)
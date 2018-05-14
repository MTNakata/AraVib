import numpy as np
from scipy import fftpack

def displacement_to_difference(displacement_array):
    displacement_array_copy = displacement_array.copy()
    dif_array = displacement_array_copy - np.roll(displacement_array_copy, -1)
    dif_array = dif_array[:-1]
    start_point = np.min(np.where(dif_array == np.max(dif_array)))
    return dif_array, start_point

def transform_hanning(displacement_array, start_point):
    hanningWindow = np.concatenate([np.zeros(start_point),np.hanning(240), np.zeros(720-start_point-240)])
    displacement_array2 = displacement_array - np.mean(displacement_array[start_point:])
    displacement_array_hanning = displacement_array2 * hanningWindow
    return displacement_array_hanning

def displacement_to_major_freq(displacement_array,fps=240):
    time_step = 1/fps
    freq = fftpack.fftfreq(displacement_array.size,d=time_step)
    fft = fftpack.fft(displacement_array)
    pidxs = np.where(freq > 0)
    freqs = freq[pidxs]
    power = np.abs(fft)[pidxs]
    freqs2 = freqs[np.where(freqs > 2)]
    power2 = power[np.where(freqs > 2)]
    major_freq = freqs2[np.where(power2 >= max(power2))]
    return freqs, power, major_freq
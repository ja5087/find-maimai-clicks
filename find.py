import numpy as np
import math
import scipy.io.wavfile
from scipy import signal
import scipy.io.wavfile
import sys




def get_sound_signal(filename):
    """
    Obtains a single channel sound and its sample rate from a path to a wavfile
    Returns a 2-tuple of song signal and sample rate (usually 44100)
    """

    sample_rate, song_raw_signal = scipy.io.wavfile.read(filename)

    # Get single channel
    song_signal = song_raw_signal[:,0]
    return (song_signal, sample_rate)


def compute_energy(f, t, Z, compF = lambda x: x):
    """
    Computes discrete time-energies from SciPy's STFT
    
    f = array of n freqencies
    t = array of m times
    Z = n*m array arranged by frequency then by time
    
    """
    absZ = np.abs(Z)
    output = []
    for i in range(len(t)):
        total = 0 
        for y in range(len(Z)):
            total += compF(absZ[y][i])
        output.append(total)
    return np.asarray(output)

def find_click_peaks(energy):
    peaks, _= signal.find_peaks(energy, prominence=1000)
    return peaks

if len(sys.argv) < 2:
    print("Insufficient arguments")
    sys.exit(0)

song = get_sound_signal(sys.argv[1])[0]
fft_width = 1000
f, t, Zxx = signal.stft(song, 44100, nperseg=fft_width)
energy = compute_energy(f, t, Zxx, lambda x: math.sqrt(x))
peaks = find_click_peaks(energy)


timecodes = peaks * fft_width / 44100 / 2


click = np.zeros_like(song)

for i in (peaks * fft_width / 2):
    click[math.floor(i)] = 1
scipy.io.wavfile.write("correl.wav", 44100, click.astype(float)/2)

with open('timecodes.txt', 'w') as f:
    for item in timecodes:
        f.write("%s\n" % item)
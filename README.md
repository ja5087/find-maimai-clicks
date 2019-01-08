# Find Maimai Clicks

Maimai is an arcade rhythm game that looks like this:

The program I wrote attempts to extract the timecodes of the various circle notes sounded by clicks from recorded gameplay (in WAV format) using an energy-based approach. There is both a Python script that will do so plus an iPython notebook (soon) that helps to tune various parameters. 

Currently it doesn't work too well with high note density samples found in maps such as World Vanquisher MAS. 

The detection works best with a high-quality ChartRef such as [https://www.youtube.com/watch?v=Z7ou_mT01Bo](https://www.youtube.com/watch?v=Z7ou_mT01Bo). Regular videos may work but peak-finding under such noisy conditions is slightly more difficult and error-prone.

## Requirements and Launching

1. Either ```python -m pip install --user numpy scipy matplotlib ipython jupyter``` or use a distribution such as [Anaconda](https://www.anaconda.com/)
2. For Notebook: launch iPython with ```jupyter notebook```
3. For script: ```python find.py filenamehere.wav```

## Approach

The approach I've taken is inspired by [this paper](https://www.ee.columbia.edu/~dpwe/papers/Laro01-swing.pdf).

1. Perform a short-time fourier transform on the wav signal to transform it into the frequency domain
2. Compute energy of each sample by summing the squares of all frequency terms
3. Find peaks using SciPy's ```find_peaks``` function with manually adjusted prominence

## TODO

1. Make intelligent guesses of various parameters such as STFT segment width and prominence based on song characteristics e.g. bpm which is known
2. Improve detection with better filtering such as summing only specific frequency ranges





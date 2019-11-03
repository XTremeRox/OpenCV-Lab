#!/usr/bin/python3
#Program to generate randomint 1D array and display fourier transform
import numpy as np
n = np.random.randint(255, size=100)
print(np.fft.fft(n))

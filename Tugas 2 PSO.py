# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:45:51 2023

@author: M. Akbar Miftahuzaman
"""

#Signal yang digunakan;  
signal1 = [1, 3, 5, 7]
signal2 = [0.5, 0.5, 0.5]

#Convulution tanpa menggunakan numpy
def convolution(arr1, arr2):
    m, n = len(arr1), len(arr2)
    result = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            result[i + j] += arr1[i] * arr2[j]

    return result

#Validasi convulusi menggunakan numpy
import numpy as np
np.convolve(signal1,signal2)

result = convolution(signal1, signal2)
Convulution_validation = np.convolve(signal1,signal2)

print("Nama: M. Akbar Miftahuzaman")
print("NRP: 5009211004")
print ("Convulution result:", np.convolve(signal1, signal2))
print("Result of convolution:", result)
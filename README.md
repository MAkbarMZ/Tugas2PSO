# Tugas2PSO
 Tugas 2 PSO 
Di tugas ini penugasan berupa pengimplementasian convulusi dari 2 dimensional signal dalam bentuk array, untuk melakukan tersebut digunakan kodingan sebagai berikut: 

#Signal yang digunakan yang akan dikonvulusikan, bisa diubah sesuai dengan keinignan;  
signal1 = [1, 3, 5, 7]
signal2 = [0.5, 0.5, 0.5]

#Operasi Convulution tanpa menggunakan numpy
def convolution(arr1, arr2):    ]
    m, n = len(arr1), len(arr2) ] -> Digunakan untuk mendefisinikan bagaimana convulusi bergerak, setiap kali operasi dijalankan, maka ruang perpotongan antara signal 1                                     2 berkurang  
    result = [0] * (m + n - 1)  ]

    for i in range(m):                          ]
        for j in range(n):                      ] --> Digunakan untuk bagaimana operasi convlusi dijalnkan dimana nilai yang perpotongan akan dikalian
            result[i + j] += arr1[i] * arr2[j]  ]

    return result

#Validasi convulusi menggunakan numpy 
import numpy as np
np.convolve(signal1,signal2)

#Menjalankan operasi convulusi dengan menggunakan signal 1 dan signal 2 sebagai input
result = convolution(signal1, signal2)

#Operasi Convulusi dengan menggunakan modul np
Convulution_validation = np.convolve(signal1,signal2)

#Hasild dari seluruh operasi diprint untuk diperlihatkan hasilnya
print("Nama: M. Akbar Miftahuzaman")
print("NRP: 5009211004")
print ("Convulution result:", np.convolve(signal1, signal2))
print("Result of convolution:", result)

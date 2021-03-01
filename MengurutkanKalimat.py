# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:49:49 2021

@author: anjas amar pradana
@lisensi: sumber terbuka
@aliansi: universitas dian nuswantoro
"""

#Mendapatkan input dari pengguna
kalimatku = input("Masukan kalimatmu: ")

#Memecah string menjadi daftar kata
kataku = [kalimat.lower() for kalimat in kalimatku.split()]

#Daftar urutan kalimat
kataku.sort()

#Menampilkan kalimat yang diurutkan
print("Kalimat yang di urutkan adalah:")
for kalimat in kataku:
   print(kalimat)
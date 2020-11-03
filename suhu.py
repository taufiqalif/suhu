#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:43:15 2020

@author: taufiq
"""
#input awal

print("=============")
print("Mengukur suhu")
print("=============")

a = input("masukan suhu awal: ")
b = input("masukan satuan tujuan: ")
c = a[len(a)-1]
d = float(a[:len(a)-1])

if (c=="C"):
    if (b=="C"):
        y = d
    elif (b=="F"):
        y = 9/5 * d + 32
    elif (b=="R"):
        y = 4/5 * d
    elif (b=="K"):
        y = d-273
elif (c=="F"):
    if (b=="C"):
        y = (d-32)*5/9
    elif (b=="F"):
        y = d
    elif (b=="R"):
        y = 4/5 * (d-32)
    elif (b=="K"):
        y = 9/5 (d-273) +32
elif (c=="R"):
    if (b=="C"):
        y = 4/5 * d
    elif (b=="F"):
        y = 4/9 (d-32)
    elif (b=="R"):
        y = d
    elif (b=="K"):
        y = 4/5 (d-273)
elif (c=="K"):
    if (b=="C"):
        y = d + 273
    elif (b=="F"):
        y = 5/9 (d-32) +273
    elif (b=="R"):
        y = 5/4 * d + 273
    elif (b=="K"):
        y = d



print(d,"",c,"=",y,"",b)
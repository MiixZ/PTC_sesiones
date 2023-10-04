#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:39:40 2023

@author: aulas
"""

import math

print("Introduzca el cateto 1.")

cat1 = float(input())

print("Introduzca el cateto 2.")

cat2 = float(input())

hipotenusa = math.sqrt(cat1**2 + cat2**2)

print(f"La hipotenusa es: {hipotenusa:.2f}")
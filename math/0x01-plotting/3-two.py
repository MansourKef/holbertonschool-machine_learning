#!/usr/bin/env python3
"""
3-two.py
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

line1, = plt.plot(x, y1,'r--')
line2, = plt.plot(x, y2, 'g')
plt.legend([line1, (line1, line2)], ["C-14", "Ra-226"])
plt.title("Exponential Decay of Radioactive Elements")
plt.xlabel('Time (years)')
plt.xlim(0,  20000)
plt.ylabel('Fraction Remaining')
plt.ylim(0,  1)
plt.show()

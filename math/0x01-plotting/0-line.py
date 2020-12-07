#!/usr/bin/env python3
"""
0-line.py
"""
import numpy as np
import matplotlib.pyplot as plt


y = np.arange(0, 11) ** 3
plt.plot(y, color='red')
plt.xlim(0, 10)
plt.show()

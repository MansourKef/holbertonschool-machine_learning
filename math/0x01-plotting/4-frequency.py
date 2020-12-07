#!/usr/bin/env python3
"""
4-frequency.py
"""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
plt.hist(student_grades, bins=6, range= (40, 100), edgecolor= 'black', linewidth= 1.2)
plt.title("Project A")
plt.xlabel('Grades')
plt.xlim(0,  100)
plt.ylabel('Number of Students')
plt.ylim(0,  30)
plt.show()

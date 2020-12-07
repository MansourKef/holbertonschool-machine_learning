#!/usr/bin/env python3
"""
5-all_in_one.py
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)


gs = gridspec.GridSpec(3, 2)
fig = plt.figure()
fig.suptitle('All in One')
ax = plt.subplot(gs[0, 0])
ax.plot(y0, color='red')
plt.xlim(0, 10)

ax = plt.subplot(gs[0, 1])
ax.plot(x1, y1, '.', color='magenta')
plt.title("Men's Height vs Weight", size= 'x-small')
plt.xlabel('Height (in)', size= 'x-small')
plt.ylabel('Weight (lbs)', size= 'x-small')

ax = plt.subplot(gs[1, 0])
ax.plot(x2, y2)
plt.title("Exponential Decay of C-14", size= 'x-small')
plt.xlabel('Time (years)', size= 'x-small')
plt.xlim(0, 28650)
plt.ylabel('Fraction Remaining', size= 'x-small')
plt.yscale('log')

ax = plt.subplot(gs[1, 1])
line1, = ax.plot(x3, y31,'r--')
line2, = ax.plot(x3, y32, 'g')
plt.legend([line1, (line1, line2)], ["C-14", "Ra-226"])
plt.title("Exponential Decay of Radioactive Elements", size= 'x-small')
plt.xlabel('Time (years)', size= 'x-small')
plt.xlim(0,  20000)
plt.ylabel('Fraction Remaining', size= 'x-small')
plt.ylim(0,  1)

ax = plt.subplot(gs[2, :])
ax.hist(student_grades, bins=6, range= (40, 100), edgecolor= 'black', linewidth= 1.2)
plt.title("Project A", size= 'x-small')
plt.xlabel('Grades', size= 'x-small')
plt.xlim(0,  100)
plt.ylabel('Number of Students', size= 'x-small')
plt.ylim(0,  30)

plt.tight_layout()
plt.show()

#!/usr/bin/env python3
"""
6-bars.py
"""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
plt.subplots()
columns = ('Farrah', 'Fred', 'Felicia')
rows = ('apples', 'bananas', 'oranges', 'peaches')
colors = ('red', 'yellow', '#ff8000', '#ffe5b4')
index = np.zeros(3)
bar_width = 0.5
for i, eachfruit in enumerate(fruit):
    plt.bar(
        lumns,
        eachfruit,
        bar_width,
        bottom=index,
        label=rows[i],
        color=colors[i]
    )
    index += eachfruit
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.title('Number of Fruit per Person')
    plt.legend()
    plt.show()

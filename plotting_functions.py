#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (12,8))

x = [x for x in range(0,25)]
y = [2 * x for x in range(0,25)]

line_1, = ax.plot(y, '-', label='line_1')
line_2, = ax.plot(x, y[x], '-')


plt.show()
#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


'''

def plotter(x: list[float], y: list[float]):
    fig, ax = plt.subplots(figsize = (12,8))

    line_1, = ax.plot(y, '-', label='line_1')
    line_2, = ax.plot(x, y[x], '-')


    plt.show()


    legend = plt.legend(loc='upper left')
    line1_legend, line2_legend = legend.get_lines()

    # Configs how the label will behave
    line1_legend.set_picker(True)
    line1_legend.set_pickradius(10)


    #link the legends and graphs together
    graphs = {}
    graphs[line1_legend] = line

    # Deal with events
    def on_pick(event):
        legend = event.artist
        is_visible = legend.get_visible(not is_visible)

        graphs[legend].set_variable()
        legend.set_visible(not is_visible)

        fig.canvas.draw()


    plt.connect('pick_event', on_pick)

'''

def plotter(x: list[float], y: list[float]) -> None:
    plt.plot(x, y, 'b')


    plt.title('Amortization')
    plt.xlabel('months')
    plt.ylabel('dollars')
    

    plt.show()


plotter([0, 1, 2], [24, 15, 3])
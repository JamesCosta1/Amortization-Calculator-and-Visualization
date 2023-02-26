#! /usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons


def plotter() -> None:
    x = range(0, 25)
    y1 = [10] * 25
    y2 = [20] * 25
    y3 = [30] * 25
    y4 = [40] * 25
    y5 = [50] * 25

    # balances
    # total_interest_paid
    # total_principal_paid
    # monthly_interest_paid
    # monthly_principal_paid

    fig, ax = plt.subplots()
    p1, = ax.plot(x ,y1, color='teal', label='Balance')
    p2, = ax.plot(x, y2, color='darkturquoise', label='Total Interest Paid')
    p3, = ax.plot(x, y3, color='mediumpurple', label='Total Principal Paid')
    p4, = ax.plot(x, y4, color='mediumturquoise',label='Interest Paid per Month')
    p5, = ax.plot(x, y5, color='mediumorchid', label='Principal Paid per Month')

    plots = [p1, p2, p3, p4, p5]
    plt.axis([-2.5, 30, 0, 60])
    plt.subplots_adjust(left=0.25, bottom=0.1, right=0.95, top=0.95)


    # Generate CheckButton widget

    labels = ['teal', 'darkturquise', 'mediumpurple', 'mediumturquoise', 'mediumorchid']
    # Set only the balances, monthly interest paid, and monthly principal paid to visible on startup
    activated = [True, False, False, True, True]

    # Define the area size of the legend
    ax_check_button = plt.axes([0.03, 0.4, 0.15, 0.15])
    check_box = CheckButtons(ax_check_button, labels, activated)

    def set_visible(label):
        '''
        Connects the checkbox object with the on click signal.
        '''
        
        index = labels.index(label)
        plots[index].set_visible(not plots[index].get_visible())
        plt.draw()

    check_box.on_clicked(set_visible)
    plt.show()



if __name__ == '__main__':
    plotter()
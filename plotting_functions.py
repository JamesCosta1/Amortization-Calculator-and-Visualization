#! /usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import amortization_functons as af


def plotter(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid) -> None:
    
    
    x = range(len(balances))

    # y1 = [10] * 25
    # y2 = [20] * 25
    # y3 = [30] * 25
    # y4 = [40] * 25
    # y5 = [50] * 25

    # balances
    # total_interest_paid
    # total_principal_paid
    # monthly_interest_paid
    # monthly_principal_paid

    fig, ax = plt.subplots()
    balances_plot, = ax.plot(x, balances, color='teal', label='Balance')
    total_interest_plot, = ax.plot(x, total_interest_paid, color='darkturquoise', label='Total Interest Paid')
    total_principal_plot, = ax.plot(x, total_principal_paid, color='mediumpurple', label='Total Principal Paid')
    monthly_interest_plot, = ax.plot(x, monthly_interest_paid, color='mediumturquoise',label='Interest Paid per Month')
    monthly_principal_plot, = ax.plot(x, monthly_principal_paid, color='mediumorchid', label='Principal Paid per Month')

    plots = [balances_plot, total_interest_plot, total_principal_plot, monthly_interest_plot, monthly_principal_plot]

    # Set the dimentions of the axes. x[-1] is the length of each list. Since the highest point will be the first element
    # of balances, I made the y max height just a bit more than that
    plt.axis([-3, (x[-1] + 10), -3, (balances[0] + 10)])
    plt.subplots_adjust(left=0.25, bottom=0.1, right=0.95, top=0.95)


    # Generate CheckButton widget

    labels = ['Remaining Balance', 'Total Interest Paid', 'Total Principal Paid', 'Monthly Interest Paid', 'Monthly Principal Paid']
    # Set all plots to visible on startup
    activated = [True, True, True, True, True]

    # Define the area size of the legend
    ax_for_check_button = plt.axes([0.03, 0.4, 0.15, 0.15])
    check_box = CheckButtons(ax_for_check_button, labels, activated)

    def set_visible(label):
        '''Connects the checkbox object with the on click signal.'''
        
        index = labels.index(label)
        plots[index].set_visible(not plots[index].get_visible())
        plt.draw()

    check_box.on_clicked(set_visible)
    plt.show()



if __name__ == '__main__':
    balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = af.amortizatize(5_000, 0.05, 219.36)
    plotter(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid)
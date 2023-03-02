#! /usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons


def display_data(balances,
                 total_interest_paid,
                 total_principal_paid,
                 monthly_interest_paid,
                 monthly_principal_paid) -> None:

    '''
    Displays on a monthly basis (1) remaining balance, (2) total interest paid, (3) total principal paid, (3) monthly interest paid, and 
    (3) monthly principal paid. 
    '''

    # Insert $ in front and a comma every three didgets
    pd.options.display.float_format = '${:,.2f}'.format

    # Allows for much more data to be displayed.
    pd.set_option('display.max_rows', 601)

    data = {
        'Remaining Balance': balances,
        'Total Interest Paid': total_interest_paid,
        'Total Principal Paid': total_principal_paid,
        'Monthly Interest Paid': monthly_interest_paid,
        'Monthly Principal Paid': monthly_principal_paid
        }

    df = pd.DataFrame(data)

    # Name the index column 'Month' instead of being unnamed by default
    df.index.name = 'Month'
 
    print(df)



def plotter(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid) -> None:
    '''
    Plots each set of values on a single plot in a new window and gives togglable display capabilities to the user for each plot.

    Args:
        balances (list[float]):               The amount of money still owed each month
        total_interest_paid (list[float]):    The amount of interest paid thus far
        total_principal_paid (list[float]):   The amount of principal paid thus far
        monthly_interest_paid (list[float]):  The amount of funds used to pay interest each month
        monthly_principal_paid (list[float]): The amount of funds used to pay interest each month
    '''

    months = range(len(balances))

    _, ax = plt.subplots()
    balances_plot, = ax.plot(months, balances, color='teal', label='Balance')
    total_interest_plot, = ax.plot(months, total_interest_paid, color='darkturquoise', label='Total Interest Paid')
    total_principal_plot, = ax.plot(months, total_principal_paid, color='mediumseagreen', label='Total Principal Paid')
    monthly_interest_plot, = ax.plot(months, monthly_interest_paid, color='mediumturquoise',label='Interest Paid per Month')
    monthly_principal_plot, = ax.plot(months, monthly_principal_paid, color='springgreen', label='Principal Paid per Month')

    plots = [balances_plot, total_interest_plot, total_principal_plot, monthly_interest_plot, monthly_principal_plot]

    # TODO: MAKE THE BUTTONS/LEGEND COLORED
    def determine_higest_point(balances, total_interest_paid):
        '''
        Finds the largest value among all lists (balances and total_interest_paid are the only two contenders among the
        five lits) so the y-axis can be determined by this value.
        '''
        if balances[0] > total_interest_paid[-1]:
            largest_y_val = balances[0]

        else:
            largest_y_val = total_interest_paid[-1]

        return largest_y_val
    
    total_number_of_months = months[-1]
    largest_y_val = determine_higest_point(balances, total_interest_paid)

    # Use a ratio of the domain and range of the set of plots to better fit the graphs in the window
    plt.axis([0, (total_number_of_months * 1.1), 0, (largest_y_val * 1.1)])
    plt.subplots_adjust(left=0.25, bottom=0.10, right=0.95, top=0.95)

    plt.title('Amortization Plot')
    plt.xlabel('Number of months')
    plt.ylabel('Dollars')
    plt.grid()

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

# TODO: POTENTIALLY WRITE A DOWNLOAD TO CSV FILE OPTION THAT THE USER CAN CHOOSE
#! /usr/bin/python3

import amortization_functons as af
import exhibition_functions as ef
import user_input_functions as uf

def recieve_initial_parameters() -> tuple[float, float, int, float]: 
    """
    Aggregates the user input data and returns the the calculated values. This is an intermediate function
    in order to minimize the number of function calls in the main file.

    Returns:
        principal (float):               The total amount of money lent
        annual_interest_rate (float):    The percentage amount the owed amount will grow in a year
        number_of_months (int):          The lifetime of the loan in months
        monthly_payment_amount (float):  The amount of money paid per month
    """

    princpial = uf.read_user_principal_size()
    annual_interest_rate = uf.read_user_interest_rate_amount()
    number_of_months = uf.read_user_number_of_months()

    monthly_payment_amount = af.calculate_payment_amount(princpial, annual_interest_rate, number_of_months)
    
    print(f'\nGiven this information, your monthly payment will be ${monthly_payment_amount:,.2f}')

    return princpial, annual_interest_rate, number_of_months, monthly_payment_amount


def options_menu(principal: float, annual_interest_rate: float, number_of_months: int, monthly_payment_amount: float) -> bool:
    program_is_running = True
    while True:
        print('\nWhat would you like to do now? \n')
        print(f'1. Display the monthly schedule using your data and a monthly payment of ${monthly_payment_amount:,.2f}')
        print(f'2. View the amortization graph using a your data and a monthly payment of ${monthly_payment_amount:,.2f}')
        print('3. To back to the main menu.')
        print('0. Close the program')

        input_ = uf.read_user_int()

        if input_ == 0:
            # Return this bool so that the variable to turn off the main method does not die in this function (due to scope)
            program_is_running = False
            return program_is_running
        elif input_ == 1:
            # Grab the lists
            balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = af.amortizatize(principal,
                                                                                                                                 annual_interest_rate,
                                                                                                                                 number_of_months,
                                                                                                                                 monthly_payment_amount)                    
            # Pass the lists into the data frame
            ef.display_data(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid)

        elif input_ == 2:
            # Grab the lists
            balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = af.amortizatize(principal,
                                                                                                                                 annual_interest_rate,
                                                                                                                                 number_of_months,
                                                                                                                                 monthly_payment_amount)
            # Pass the lists into plotter
            ef.plotter(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid)

        elif input_ == 3:
            print('\nGoing back...\n')
            return program_is_running

        else:
            print("Please input a valid option.")
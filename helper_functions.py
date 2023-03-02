#! /usr/bin/python3

import amortization_functons as af
import plotting_functions as pf


# TODO: PARTITION THESE USER INPUT FUNCTIONS INTO THEIR OWN FILE. THEN RENAME IS FILE TO MENU FUNCTIONS OR SOMTHNG
def read_user_int() -> int:
    while True:
        input_ = input('')
        try:
           input_ = int(input_.strip())
           return input_

        except ValueError:
          print('Please enter a valid input.')



def read_user_float() -> float:
    while True:
        input_ = input('')
        try:
           input_ = float(input_.strip())
           return input_

        except ValueError:
          print('Please enter a valid input.')



def read_user_principal_size() -> float:
    ''' Ensures the user provides a satisfactory principal'''
    while True:
        input_ = read_user_float()
        if (1_000 <= input_ <=  5_000_000):
            princpial = round(input_, 2)
            return princpial
        print('Please provide a loan amount between 1,000 and 5,000,000.')



def read_user_interest_rate_amount() -> float:
    ''' Ensures the user provides a satisfactory annual interest rate'''
    while True:
        input_ = read_user_float()
        if (1 <= input_ <=  45):
            annual_interest_rate = round(input_, 2)
            return annual_interest_rate
        print('Please provide an annual interest rate between 1% and 45%.')



def read_user_number_of_months() -> int:
    ''' Ensures the user provides a satisfactory number of months'''
    while True:
        input_ = read_user_int()
        if (3 <= input_ <=  600):
            months = input_
            return months
        print('Please provide an annual interest rate between 1% and 45%.')


# TODO: MAKE SURE THAT USERS CANNOT PUT IN NUMBERS THAT ARE TOO BIG THAT MAKE THE PROGRAM BREAK.
# TODO: ENSURE THAT USERS CAN ONLY PLACE IN INTEREST RATES UP TO .40, BUT I AM UNDECIDED IF I AM OKAY WITH A VALUE OF ZERO.
# TODO: MOVE THE BELOW PRINT STATMENTS INTO THE READ USER FUNCTIONS ABOVE
def recieve_initial_parameters() -> tuple[float, float, int, float]: 
    print('Please enter the size of the loan between $1,000 and $5,000,000:')
    princpial = read_user_principal_size()
    
    print('Please enter the loan\'s annual interest rate (as a percent):')
    annual_interest_rate = read_user_interest_rate_amount()

    print('Please enter the lifetime of the loan (in months):')
    number_of_payments = read_user_number_of_months()

    monthly_payment_amount = af.calculate_payment_amount(princpial, annual_interest_rate, number_of_payments)
    
    print(f'\nGiven this information, your monthly payment will be ${monthly_payment_amount:.2f}')

    return princpial, annual_interest_rate, number_of_payments, monthly_payment_amount



def options_menu(principal, annual_interest_rate, monthly_payment_amount) -> bool:
    program_is_running = True
    while True:
        print('\nWhat would you like to do now? \n')
        print(f'1. Display the monthly schedule using a monthly payment of ${monthly_payment_amount:.2f}')
        print(f'2. View the amortization graph using a monthly payment of ${monthly_payment_amount:.2f}')
        print('3. To back to the main menu.')
        print('0. Close the program')

        input_ = read_user_int()

        if input_ == 0:
            # Return this bool so that the variable to turn off the main method does not die in this function (due to scope)
            program_is_running = False
            return program_is_running
        elif input_ == 1:
            # Grab the lists
            balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = af.amortizatize(principal,
                                                                                                                                 annual_interest_rate,
                                                                                                                                 monthly_payment_amount)                    
            # Pass the lists into the data frame
            af.display_data(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid)

        elif input_ == 2:
            # Grab the lists
            balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = af.amortizatize(principal,
                                                                                                                                 annual_interest_rate,
                                                                                                                                 monthly_payment_amount)
            # Pass the lists into the plotter
            pf.plotter(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid)

        elif input_ == 3:
            return program_is_running

        else:
            print("Please input a valid option.")
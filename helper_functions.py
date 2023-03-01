#! /usr/bin/python3

import amortization_functons as af
import plotting_functions as pf



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



def recieve_initial_parameters() -> tuple[float, float, int, float]: # TODO: MAKE SURE THAT USERS CANNOT PUT IN NUMBERS THAT ARE TOO BIG THAT MAKE THE PROGRAM BREAK
    print('Please enter the size of the loan (to the nearest cent):')
    princpial = read_user_float()
    
    print('Please enter the loan\'s annual interest rate (as a decimal):')
    annual_interest_rate = read_user_float()

    print('Please enter the lifetime of the loan (in months):')
    number_of_payments = read_user_int()

    monthly_payment_amount = af.calculate_payment_amount(princpial, annual_interest_rate, number_of_payments)

    print(f'Thank you. Your monthly payment will be ${monthly_payment_amount} for a total of {number_of_payments} months.')

    return princpial, annual_interest_rate, number_of_payments, monthly_payment_amount



def options_menu(principal, annual_interest_rate, monthly_payment_amount) -> None:
    while True:
        print('\nWhat would you like to do now? \n')
        print(f'1. Display the monthly schedule using a monthly payment of ${monthly_payment_amount: .2f}')
        print(f'2. View the amortization graph using a monthly payment of ${monthly_payment_amount: .2f}')
        print('3. To back to the main menu.')
        print('0. Close the program')

        input_ = read_user_int()

        if input_ == 0:
            program_is_running = False
            break
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
            break

        else:
            print("Please input a valid option.")
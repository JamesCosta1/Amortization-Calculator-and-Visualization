#! /usr/bin/python3

from os import system
import helper_functions as hf
import amortization_functons as af
from plotting_functions import plotter

def main() -> None:
    system('clear')
    program_is_running = True

    print('Welcome to this amortiztion calculator.')
    while program_is_running:
        print('Please select an option below: \n')
        print('1. Calculate a monthly payment')
        print('0. Close program')
        
        input_ = hf.read_user_int()
        if input_ == 0:
            program_is_running = False
        elif input_ == 1:
            princpial, annual_interest_rate, number_of_payments, monthly_payment_amount = hf.recieve_initial_paramaters()
            print(f'Given this information, your monthly payment will be{monthly_payment_amount:$>1}')

            while not monthly_payment_amount is None:
                print('What would you like to do now? \n')
                print(f'1. Display the monthly schedule using a monthly payment of{monthly_payment_amount:$>1}')
                print(f'2. View the amortization graph using a monthly payment of{monthly_payment_amount:$>1}')
                print('3. To back to main menu.')
                print('0. Exit')

                input_ = hf.read_user_int()

                if input_ == 0:
                    program_is_running = False
                    break
                elif input_ == 1:
                    af.monthly_exhibition(balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid)
                    pass

                elif input_ == 2:
                    # Grab the lists that need placed into the plotter.
                    balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = af.amortizatize(princpial,
                                                                                                                                         annual_interest_rate,
                                                                                                                                         number_of_payments,
                                                                                                                                         monthly_payment_amount)

                elif input_ == 3:
                    break

                else:
                    print("Please input a valid option.")

        else:
            print("Please input a valid option.")
    
    print('Thank you for using this application, have good day!')



if __name__ == '__main__':
    main()

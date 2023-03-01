#! /usr/bin/python3

from os import system
import helper_functions as hf
import amortization_functons as af

def main() -> None:
    system('clear')
    program_is_running = True

    print('Welcome to this amortiztion calculator.')
    while program_is_running:
        print('\nPlease select an option below: \n')
        print('1. Calculate a monthly payment')
        print('0. Close the program')
        
        input_ = hf.read_user_int()
        if input_ == 0:
            program_is_running = False

        elif input_ == 1:
            # Rewrite this function so that I do not need to recieve a useless variable I name named _.
            principal, annual_interest_rate, _, monthly_payment_amount = hf.recieve_initial_parameters()
            print(f'Given this information, your monthly payment will be ${monthly_payment_amount}')

            hf.options_menu(principal, annual_interest_rate, monthly_payment_amount)

        else:
            print("Please input a valid option.")
    
    print('Thank you for using this application, have good day!')



if __name__ == '__main__':
    main()

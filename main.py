#! /usr/bin/python3

from os import system
import helper_functions as hf


# TODO: GO THROUGH ALL FILES AND RENAME ALL MONTHLY STUFF TO MONTHS AMOUNT INSTEAD OF 
def main() -> None:
    system('clear')
    
    # This variable is defined due to scoping. I want to be able to close the progam when inside of the options menu.
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
            # TODO: Rewrite this function so that I do not need to recieve a useless variable I name named _.
            principal, annual_interest_rate, _, monthly_payment_amount = hf.recieve_initial_parameters()

            # This value returns false if the close program option is selected, returns true otherwise.
            program_is_running = hf.options_menu(principal, annual_interest_rate, monthly_payment_amount)

        else:
            print("Please input a valid option.")
    
    print('Thank you for using this application, have good day!')



if __name__ == '__main__':
    main()

#! /usr/bin/python3

from os import system
import menu_functions as mf
import user_input_functions as uf


def main() -> None:
    system('clear')
    
    # This variable is defined due to scoping. I want to be able to close the progam while inside of the options menu.
    program_is_running = True
    print('Welcome to this amortiztion calculator.')

    while program_is_running:
        print('\nPlease select an option below: \n')
        print('1. Calculate a monthly payment')
        print('0. Close the program')
        
        input_ = uf.read_user_int()
        if input_ == 0:
            program_is_running = False

        elif input_ == 1:
            # Call and return all the initial parameters provided by the user.
            principal, annual_interest_rate, monthly_payment_amount = mf.recieve_initial_parameters()

            # Pass these user inputs into options_menu. Then the user is asked what they would like done with this data.
            # Note that this function returns false if the close program option is selected. When they instead want to
            # just return to the main menu,true is returned.
            program_is_running = mf.options_menu(principal, annual_interest_rate, monthly_payment_amount)

        else:
            print("Please input a valid option.")
    
    print('Thank you for using this application, have good day!')



if __name__ == '__main__':
    main()

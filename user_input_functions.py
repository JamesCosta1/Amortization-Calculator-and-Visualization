#! /usr/bin/python3

def read_user_int() -> int:
    '''Ensures the user provides a int and strips away any surrounding spaces.'''
    while True:
        input_ = input('')
        try:
            # Removes any leading or tailing spaces
            input_ = input_.strip()
            input_ = int(input_)
            return input_

        except ValueError:
            print('Please enter a valid input.')


def read_user_float() -> float:
    '''Ensures the user provides a float and strips away all non-numberic characters.'''
    while True:
        input_ = input('')
        try:
            # Removes any leading or tailing spaces
            input_ = input_.strip()

            # Removes any commas
            input_ = input_.replace(',', '')

            # Removes any leading $ signs or tailing % signs in the user input
            if input_.startswith('$'):
                input_ = input_[1:]

            if input_.endswith('%'):
                input_ = input_[:-1]
    
            input_ = float(input_)
            return input_

        except ValueError:
            print('\nPlease enter a valid input.')


def read_user_principal_size() -> float:
    ''' Ensures the user provides a satisfactory principal.'''
    print('\nPlease enter the size of the loan between $1,000 and $5,000,000:')
    while True:
        input_ = read_user_float()
        if (1_000 <= input_ <=  5_000_000):
            princpial = round(input_, 2)
            return princpial
        print('\nPlease provide a value between $1,000 and $5,000,000.')


def read_user_interest_rate_amount() -> float:
    ''' Ensures the user provides a satisfactory annual interest rate.'''
    print('\nPlease enter the loan\'s annual interest rate (as a percent) bewteen 1% and 45%:')
    while True:
        input_ = read_user_float()
        if (1 <= input_ <=  45):
            annual_interest_rate = round(input_, 2)
            return annual_interest_rate
        print('\nPlease provide a value between 1% and 45%.')


def read_user_number_of_months() -> int:
    ''' Ensures the user provides a satisfactory number of months.'''
    print('\nPlease enter the lifetime of the loan (in months) between 3 and 600:')
    while True:
        input_ = read_user_int()
        if (3 <= input_ <=  600):
            number_of_months = input_
            return number_of_months
        print('\nPlease provide a value between 3 and 600.')
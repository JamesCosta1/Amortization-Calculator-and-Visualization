#! /usr/bin/python3

from time import sleep
from amortization_functons import calculate_payment_amount, amortizatize


def read_user_int(input_: any) -> int:
    while True:
        input_ = input("")
        try:
           input_ = int(input_.strip())
           return input_

        except ValueError:
          print('Please enter a valid input.')



def read_user_float(input_: any) -> float:
    while True:
        input_ = input("")
        try:
           input_ = float(input_.strip())
           return input_

        except ValueError:
          print('Please enter a valid input.')


def recieve_initial_paramaters() -> tuple(float, float, int, float):
    print('Please enter the size of the loan (to the nearest cent)')
    sleep(3)
    princpial = read_user_float()
    
    print('Please enter the loan\'s annual interest rate (as a decimal).')
    sleep(3)
    annual_interest_rate = read_user_float()

    print('Please enter the lifetime of the loan be (in months)')
    sleep(3)
    number_of_payments = read_user_int()

    monthly_payment_amount = calculate_payment_amount(princpial, annual_interest_rate, number_of_payments)

    print(f'Thank you. Your monthly payment will be ${monthly_payment_amount} for a total of{number_of_payments} months.')

    return princpial, annual_interest_rate, number_of_payments, monthly_payment_amount
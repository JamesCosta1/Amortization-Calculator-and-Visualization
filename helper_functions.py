#! /usr/bin/python3

def get_user_int(input_: any) -> int:
    while True:
        input_ = input("")
        try:
           input_ = int(input_.strip())
           return input_

        except ValueError:
          print('Please enter a valid input.')



def get_user_float(input_: any) -> float:
    while True:
        input_ = input("")
        try:
           input_ = float(input_.strip())
           return input_

        except ValueError:
          print('Please enter a valid input.')

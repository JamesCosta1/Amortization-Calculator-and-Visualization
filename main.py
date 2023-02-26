#! /usr/bin/python3

from os import system


from amortization_functons import calculate_payment_amount

def main() -> None:
    system('clear')
    program_is_running = True
    while program_is_running:
        print("Welcome to this amartiztion calculator.")
        print("Please select an option below:")
        print("1. Calculate my monthly payment")
        print("0. Close progam")
        userinput = input()



if __name__ == "__main__":
    main()

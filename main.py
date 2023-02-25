


from amortization_functons import calculate_payment_amount

def main() -> None:
    program_is_running = True
    while program_is_running:
        print("Welcome to this amartiztion calculator.")
        print("Please select an option below:")
        print("1. Calculate my monthly payment")
        print("0. Close progam")
        userinput = input()




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


if __name__ == "__main__":
    main()

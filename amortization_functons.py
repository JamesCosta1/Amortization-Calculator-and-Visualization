#! /usr/bin/python3
import numpy as np

def calculate_payment_amount(principal: float, annual_interest_rate: float, number_of_payments: int) -> float:
    '''
    Args:
        principal (float):              The total amount of money lent
        annual_interest_rate (float) :  The percentage amount the owed amount will grow in a year
        number_of_payments (int):       The total number of payments made over the life of the loan
                                        (If payments are made monthly, this is the same value as the
                                         loan's lifetime in months)


    Returns:
        Monthly payment (float)
    '''
    # Convert annual interest rate into monthly
    interest_rate = annual_interest_rate / 12
    
    numerator = interest_rate * ((1 + interest_rate) ** (number_of_payments))
    denominator = ((1 + interest_rate) ** (number_of_payments)) - 1

    monthly_payment_amount = principal * (numerator / denominator)

    return monthly_payment_amount



def amortizatize(principal: float, annual_interest_rate: float, monthly_payment_amount: float) -> tuple[list[float], list[float], list[float], list[float], list[float]]:
    remaining_balance = principal
    balances = [principal]
    total_interest_paid = [0]
    total_principal_paid = [0]
    monthly_interest_paid = [0]
    monthly_principal_paid = [0]

    interest_rate = annual_interest_rate / 12
    # multiplier = 1 + interest_rate

    while remaining_balance > 0: #TODO: Consider that a last payment might overpay slightly, so I must make this last payment exactly the
        #remaining balance of the last month.

        # Calculate the interest amount for this month
        interest_amount = remaining_balance * interest_rate
        # Calculate balance after interest
        remaining_balance *= (1 + interest_rate)
        # Make the monthly payment
        remaining_balance -= monthly_payment_amount

        # Calculate the principal paid amount for this month
        principal_amount = monthly_payment_amount - interest_amount

        # Store these new values
        balances.append(remaining_balance)

        total_interest_paid.append(total_interest_paid[-1] + interest_amount)
        
        total_principal_paid.append(total_principal_paid[-1] + principal_amount)
        
        monthly_interest_paid.append(interest_amount)
        
        monthly_principal_paid.append(principal_amount)

    # Round each element of each the list
    balances = [round(x, 2) for x in balances]
    total_interest_paid = [round(x, 2) for x in total_interest_paid]
    total_principal_paid = [round(x, 2) for x in total_principal_paid]
    monthly_interest_paid = [round(x, 2) for x in monthly_interest_paid]
    monthly_principal_paid = [round(x,2) for x in monthly_principal_paid]

    return balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid

# Testing the amortizate function:
def testing_function(): # Delete later!!!!!!

    balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid = amortizatize(5_000, 0.05, 219.36)

    

    print(f'The balances at the end of every month is:{balances}')

    print('')

    print(f'The  total interest paid thusfar is:{total_interest_paid}')

    print('')

    print(f'The total principal paid paid thusfar is:{total_principal_paid}')

    print('')

    print(f'The amount of interest paid at the end of every month is:{monthly_interest_paid}')

    print('')

    print(f'The amount of principal paid at the end of every month is:{monthly_principal_paid}')


# testing_function()
    


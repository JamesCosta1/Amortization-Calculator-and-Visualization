#! /usr/bin/python3

import pandas as pd

def calculate_payment_amount(principal: float,
                             annual_interest_rate: float,
                             number_of_payments: int) -> float:
    '''
    Calculates the monthly payment amount in order to amortizate a loan.
    
    Args:
        principal (float):              The total amount of money lent
        annual_interest_rate (float):   The percentage amount the owed amount will grow in a year
        number_of_payments (int):       The total number of payments made over the life of the loan
                                        (If payments are made monthly, this is the same value as the
                                         loan's lifetime in months)


    Returns:
        monthly_payment_amount (float)
    '''

    # Convert annual interest rate as a percent to a decimal
    annual_interest_rate /= 100

    # Convert annual interest rate to monthly
    interest_rate = annual_interest_rate / 12


    
    numerator = interest_rate * ((1 + interest_rate) ** (number_of_payments))
    denominator = ((1 + interest_rate) ** (number_of_payments)) - 1

    monthly_payment_amount = principal * (numerator / denominator)

    return monthly_payment_amount



def amortizatize(principal: float,
                 annual_interest_rate: float,
                 monthly_payment_amount: float) -> tuple[list[float],
                                                         list[float],
                                                         list[float],
                                                         list[float],
                                                         list[float]]:
    '''
    Generates lists with each subsequent element corrosponding to each month until the remaining balance becomes zero.

    Args:
        principal (float):                    The total amount of money lent
        annual_interest_rate (float) :        The percentage amount the owed amount will grow in a year
        monthly_payment_amount (float):       The amount of money paid per month


    Returns:
        balances (list[float]):               The amount of money still owed each month
        total_interest_paid (list[float]):    The amount of interest paid thus far
        total_principal_paid (list[float]):   The amount of principal paid thus far
        monthly_interest_paid (list[float]):  The amount of funds used to pay interest each month
        monthly_principal_paid (list[float]): The amount of funds used to pay interest each month
    '''

    # Initialize
    remaining_balance = principal
    balances = [principal]
    total_interest_paid = [0]
    total_principal_paid = [0]
    monthly_interest_paid = [0]
    monthly_principal_paid = [0]

    # Convert annual interest rate as a percent to a decimal
    annual_interest_rate /= 100

    # Convert annual interest rate to monthly
    interest_rate = annual_interest_rate / 12
    
    while remaining_balance > 0: #TODO: Consider that a last payment might overpay slightly, so I must make this last payment exactly the
        #remaining balance of the last month. ALSO need to think about rounding errors. Maybe concider Decimal()?

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
    # balances = [round(x, 2) for x in balances]
    # total_interest_paid = [round(x, 2) for x in total_interest_paid]
    # total_principal_paid = [round(x, 2) for x in total_principal_paid]
    # monthly_interest_paid = [round(x, 2) for x in monthly_interest_paid]
    # monthly_principal_paid = [round(x, 2) for x in monthly_principal_paid]

    return balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid



def display_data(balances,
                 total_interest_paid,
                 total_principal_paid,
                 monthly_interest_paid,
                 monthly_principal_paid) -> None:

    '''
    Displays on a monthly basis (1) remaining balance, (2) total interest paid, (3) total principal paid, (3) monthly interest paid, and 
    (3) monthly principal paid. 
    '''

    # Insert $ in front and a comma every thousands place.
    pd.options.display.float_format = '${:,.2f}'.format

    # Allows for much more data to be displayed.
    pd.set_option('display.max_rows', 512)

    data = {
        'Remaining Balance': balances,
        'Total Interest Paid': total_interest_paid,
        'Total Principal Paid': total_principal_paid,
        'Monthly Interest Paid': monthly_interest_paid,
        'Monthly Principal Paid': monthly_principal_paid
        }

    df = pd.DataFrame(data)

    # Name the index column 'Month' instead of being unnamed by default
    df.index.name = 'Month'
 
    print(df)
#! /usr/bin/python3

def calculate_payment_amount(principal: float,
                             annual_interest_rate: float,
                             number_of_months: int) -> float:
    '''
    Calculates the monthly payment amount in order to amortizate a loan.
    
    Args:
        principal (float):              The total amount of money lent
        annual_interest_rate (float):   The percentage amount the owed amount will grow in a year
        number_of_months (int):         The lifetime of the loan in months

    Returns:
        monthly_payment_amount (float)
    '''

    # Convert annual interest rate as a percent to a decimal
    annual_interest_rate /= 100

    # Convert annual interest rate to monthly
    interest_rate = annual_interest_rate / 12


    
    numerator = interest_rate * ((1 + interest_rate) ** (number_of_months))
    denominator = ((1 + interest_rate) ** (number_of_months)) - 1

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
    Generates lists of funds with each index corrosponding to each month's relevant values

    Args:
        principal (float):                    The total amount of money lent
        annual_interest_rate (float):         The percentage amount the owed amount will grow in a year
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

    # Generates the lists, appending elements to each list until the remaining balances becomes zero   
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

        # Store these new values in each respective list
        balances.append(remaining_balance)
        total_interest_paid.append(total_interest_paid[-1] + interest_amount)
        total_principal_paid.append(total_principal_paid[-1] + principal_amount)
        monthly_interest_paid.append(interest_amount)
        monthly_principal_paid.append(principal_amount)
    
    
    
    return balances, total_interest_paid, total_principal_paid, monthly_interest_paid, monthly_principal_paid
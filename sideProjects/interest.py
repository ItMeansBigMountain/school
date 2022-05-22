import math 


def add_on_interest():
    principle = float(input("please enter loan amount: "))
    interest_rate = float(input("please enter interest percentage: ")) / 100
    years = float(input("please enter amount of years: "))
    months = years * 12

    # find simple interest
    simple_interest = principle * interest_rate * years
    simple_total = simple_interest + principle


    # divide number of payments from simple total
    total_monthly_payment = simple_total / months
    principle_monthly_payment = principle / months
    interest_monthly_payment = total_monthly_payment - principle_monthly_payment

    final_ratio = interest_monthly_payment / principle_monthly_payment
    annual_rate = final_ratio * 12 *100


    print("total monthly payment: " , total_monthly_payment)
    print("principle: " , principle_monthly_payment)
    print("interest: " , interest_monthly_payment)
    print("ratio: " , final_ratio)
    print("annual rate: " , annual_rate)

def compound_interest():
    principle  =  float(input("please enter principle: "))
    interest_rate =  float(input("please enter interest rate percentage: ")) / 100
    frequency_of_compounds =  float(input("please enter frequency of compounds per year: "))
    years  =  float(input("please enter years: "))

    # COMPOUND INTEREST FORMULA
    # A = P(1 + (r/n) ) ** (n*t)
    output = principle * ( 1 + (interest_rate/frequency_of_compounds)  ) ** (frequency_of_compounds*years)

    print("OUTPUT: " , output)

def annuity():
    # INIT
    deposit = float(input("please enter deposit: "))
    annual_interest_rate = float(input("please enter the Annual interest percentage: "))/100
    years = int(input("please enter years of investment: "))
    compound_frequency = int(input("How many compounds per year? "))
    deposit_frequency = int(input("How many deposits per year? "))
    interest_rate_per_compund = annual_interest_rate / compound_frequency


    # ITERATIVE SOLUTION
    total = 0
    for payment in range(0, (compound_frequency*years),1 ):
        interest = total * interest_rate_per_compund
        total = total + deposit
        total = total + interest
    print("ITERATIVE SOLUTION: " , total)  


    # FUNCTIONAL SOLUTION    A = R( ( ( (1+(r/m))**n  -1) / (r/m)  )  )
    output = deposit * ( ( ( 1+(annual_interest_rate/deposit_frequency))**(compound_frequency*years)  - 1) / (annual_interest_rate/compound_frequency) )
    print("MATH SOLUTION: " , output)


def find_annuity_deposit():
    '''
    R = reciprical of fraction who its multiiplied by
    '''
    # INIT
    initial_amount = float(input("please enter initial amount before time periods: "))
    annual_interest_rate = float(input("please enter the Annual interest percentage: "))/100
    years = int(input("please enter years of investment: "))
    compound_frequency = int(input("How many compounds per year? "))
    deposit_frequency = int(input("How many deposits per year? "))
    interest_rate_per_compund = annual_interest_rate / compound_frequency


    numerator = initial_amount * (annual_interest_rate/compound_frequency)
    denominator =  (  (1+(annual_interest_rate/compound_frequency))**(years*compound_frequency) ) - 1
    output = numerator / denominator 

    print(  output )




# CALLING FUNCTIONS DOWN HERE
# add_on_interest()
# compound_interest()
annuity()
# find_annuity_deposit()


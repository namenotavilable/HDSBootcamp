# This program was writen on 3 April 2023, with boot from HyperionDev and help from GPT from OpenAI
import math
# Capstone Project program for calculating Simple or Compound interest on Investment or Repayments on Mortgage

print("Hello,I AM your personal financial calculator, how can AM assist you today \n")

print("1. Investment: I can help you calculate the amount of interest.\n")

print("2. Mortgage: I can help you find out how much interest you will pay on your home loan.\n")

# Asking user for input on which product they would like to use and storing it in a variable

users_choice = input("Which product would you like to choose?\n")

# Using if statment and mathematical formulas to generate calculation of simple or compund interest  
# Using method .lower to lower case of input per task objective 

if users_choice.lower() == "investment":
    print("Investment")
    invest_amount = float(input("How much would you like to invest?\n"))
    invest_interest = float(input("What interest rate would you like to apply?\n"))
    invest_term = int(input("For how many years would you like to invest it for?\n"))
    invest_intertype = input("What type of interest? 1. Simple or 2. Compound:\n")
    if invest_intertype.lower() == "simple":
        simple_interest = invest_amount * (1 + (invest_interest / 100) * invest_term)
        print(simple_interest)
    elif invest_intertype.lower() == "compound":
        compound_interest = invest_amount * math.pow((1 + invest_interest / 100), invest_term)
        print(compound_interest)
    else:
        print("Please check your spelling")

# Using elif statment and mathematical formula for calculating repayment amount on home loan 

elif users_choice.lower() == "mortgage":
    print("Mortgage")
    collateral_value = float(input("What is your house worth?\n"))
    loan_interest = float(input("What will be the interest rate on that loan?\n"))
    loan_term = int(input("What will be the term of the loan in months?\n"))
    repayment_amount = (((loan_interest / 100) / 12) * collateral_value) / (1 - (1 + ((loan_interest / 100) / 12)) ** (-loan_term))
    print(repayment_amount)
else:
    print("Please check your spelling")

# Using else statment to catch any spelling errors or incorrect input     


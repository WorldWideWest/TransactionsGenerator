

# date_of_transaction - Specify the DateTime format
# designation - constants.py file 
# amount
# bank - constants.py file
# account_no - Randomly genrated
# iban - Randomly genrated


# Number of accounts 2, 5, 6 
# Auto generate the ibans for the created accounts
# Specfiy the Bank of the account also randomly
#################################################

# Generate the Transactions
# Ask the user for the number of transactions he/she wants 100
# Randomly generate the dates
# Randomly generate the designations
# Randomly generate the amounts
# Randomly assign the accounts to transactions


# 444444-444444-444448 (18)
import numpy as np
import pandas as pd
import random
from constants import Banks

number_of_accounts = 2
account_no, iban_no = "", ""
accounts = []

for i in range(0, number_of_accounts):
    
    sample_account_no = random.sample(range(100000, 900000), 3)
    sample_iban = random.sample(range(1000000000000000000, 9000000000000000000), 1)

    for i in range(0, len(sample_account_no)):
        if i == len(sample_account_no) - 1:
            account_no += f"{ sample_account_no[i] }"
        else:
            account_no += f"{ sample_account_no[i] }-"

    iban_no += f"BA{ sample_iban[0] }"
    sample_bank = random.choice(list(Banks))
    
    accounts.append([
        account_no, iban_no, random.choice(list(Banks)).value])
    account_no, iban_no = "", ""

for account in accounts:
    print(account)



if __name__ == "__main__":
    pass


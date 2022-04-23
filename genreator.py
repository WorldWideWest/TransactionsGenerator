

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
from faker import Faker
import pandas as pd
import random
import pytz
from datetime import datetime
from constants import Banks, Designations


number_of_accounts = 2
account_no, iban_no = "", ""
accounts = []
faker = Faker()

# Account Data Generator
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


# Transaction Data Generator


columns = ["date_of_transaction", "designation", "amount", "bank", "account_no", "iban"]
# dataFrame = pd.DataFrame(columns = columns)
data = []
amount = 0

for _ in range(50):
    # Date Generator

    date_time = faker.date_time_between(
            start_date = datetime(2019,1,1),
            tzinfo = pytz.timezone("Europe/Sarajevo"))

    designation_cat = random.choice(list(Designations))
    if designation_cat == Designations.vehicle:
        amount = round(random.uniform(1, 500), 2)
    elif designation_cat == Designations.loan:
        amount = round(random.uniform(10000, 500000), 2)
    elif designation_cat == Designations.pharmacy:
        amount = round(random.uniform(1, 200), 2)
    elif designation_cat == Designations.bank_fee:
        amount = round(random.uniform(1, 50), 2)
    elif designation_cat == Designations.atm:
        amount = round(random.uniform(0, 2000), 2)
    elif designation_cat == Designations.shopping:
        amount = round(random.uniform(0, 10000), 2)
    elif designation_cat == Designations.salary:
        amount = round(random.uniform(0, 10000), 2)
    elif designation_cat == Designations.other:
        amount = round(random.uniform(0, 500), 2)
    
    account = random.choice(accounts)
    data.append([
            date_time.strftime("%-d.%-m.%Y %H:%M"),
            random.choice(designation_cat.value),
            amount, account[2], account[0], account[1]
        ])

    #dataFrame.append({
    #    "date_of_transaction": date_time.strftime("%-d.%-m.%Y %H:%M"),
     #   "designation": random.choice(designation_cat.value), 
      #  "amount": amount,
       # "bank": account[2],
       # "account_no": account[0],
       # "iban": account[1]
       # }, ignore_index = True)

dataFrame = pd.DataFrame(data, columns = columns)
print(dataFrame)






if __name__ == "__main__":
    pass


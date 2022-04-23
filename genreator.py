import pandas as pd
from faker import Faker
from datetime import datetime
import random, pytz, sys, os

from constants import Banks, Designations


number_of_accounts, number_of_transactions = int(sys.argv[1]), int(sys.argv[2])
account_no, iban_no = "", ""
accounts = []
faker = Faker()

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


columns = ["date_of_transaction", "designation", "amount", "bank", "account_no", "iban"]
data, amount = [], 0

for _ in range(number_of_transactions):
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
            amount, account[2], account[0], account[1]])

dataFrame = pd.DataFrame(data, columns = columns)

if not os.path.exists(os.path.join(os.getcwd(), "exports")):
    os.makedirs("exports")

now = datetime.now().strftime("%-d-%-m-%Y_%H:%M")
dataFrame.to_csv(os.path.join(os.getcwd(), "exports", f"export_{ now }.csv"), sep=";", index = False)

print(dataFrame)

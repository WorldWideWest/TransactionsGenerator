import pandas as pd
from faker import Faker
from datetime import datetime
import random, pytz, os

from utils.constants import Designations
from utils.account import Account

def main():
    print("Please fill in the details")
    number_of_accounts = int(input("Number of accounts: "))
    number_of_transactions = int(input("Number of transactions: "))
    delimiter = str(input("Please insert your delimiter: "))
    faker = Faker()

    account = Account()
    accounts = account.generate_accounts(number_of_accounts)

    designations = list(Designations)
    designations.remove(designations[6])

    columns = ["date_of_transaction", "designation", "amount", "bank", "account_no", "iban"]
    data, amount = [], 0
    
    for _ in range(number_of_transactions):
        date_time = faker.date_time_between(start_date = datetime(2019,1,1), tzinfo = pytz.timezone("Europe/Sarajevo"))

        index = random.choice(range(len(accounts)))

        designation_cat = random.choice(list(Designations))
        if accounts[index][4] / accounts[index][3] < .7:
            if designation_cat == Designations.vehicle:
                amount = float(round(random.uniform(1, 100), 2))
            elif designation_cat == Designations.loan:
                amount = float(round(random.uniform(100, 5000), 2))
            elif designation_cat == Designations.pharmacy:
                amount = float(round(random.uniform(1, 200), 2))
            elif designation_cat == Designations.bank_fee:
                amount = float(round(random.uniform(1, 50), 2))
            elif designation_cat == Designations.atm:
                amount = float(round(random.uniform(1, 1500), 2))
            elif designation_cat == Designations.shopping:
                amount = float(round(random.uniform(1, 10000), 2))
            elif designation_cat == Designations.other:
                amount = float(round(random.uniform(1, 100), 2))
            accounts[index][4] += amount
        else:
            designation_cat = Designations.salary
            accounts[index][3] += float(round(random.uniform(1400, 10000), 2))

        data.append([date_time.strftime("%-d.%-m.%Y %H:%M"), random.choice(designation_cat.value),
                amount, accounts[index][0], accounts[index][1], accounts[index][2]])

    dataFrame = pd.DataFrame(data, columns = columns)

    if not os.path.exists(os.path.join(os.getcwd(), "exports")):
        os.makedirs("exports")

    now = datetime.now().strftime("%-d-%-m-%Y_%H-%M")
    dataFrame.to_csv(os.path.join(os.getcwd(), "exports", f"export_{ now }_accounts_{ len(accounts) }.csv"), sep = delimiter, index = False)

    print(dataFrame)

if __name__ == "__main__":
    main()

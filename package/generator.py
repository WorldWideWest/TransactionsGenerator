import pandas as pd
from faker import Faker
from datetime import datetime
import random, pytz, os

from utils.constants import Banks, Designations

def main():
    print("Please fill in the details")
    number_of_accounts = int(input("Number of accounts: "))
    number_of_transactions = int(input("Number of transactions: "))
    delimiter = str(input("Please insert your delimiter: "))
    account_no, iban_no = "", ""
    accounts, banks = [], list(Banks)
    faker = Faker()

    designations = list(Designations)
    designations.remove(designations[6])

    print(designations[0].name)

    for index in range(number_of_accounts):
        
        sample_account_no = random.sample(range(100000, 900000), 3)
        sample_iban = random.sample(range(100000000000000000, 900000000000000000), 1)

        for i in range(0, len(sample_account_no)):
            if i == len(sample_account_no) - 1:
                account_no += f"{ sample_account_no[i] }"
            else:
                account_no += f"{ sample_account_no[i] }-"

        iban_no += f"BA{ sample_iban[0] }"

        sample_bank = random.sample(banks, 1)
        banks.remove(sample_bank[0])
        accounts.append([sample_bank[0].value, account_no, iban_no, 1, 0])
            
        account_no, iban_no = "", ""

    columns = ["date_of_transaction", "designation", "amount", "bank", "account_no", "iban"]
    data, amount = [], 0

    for _ in range(number_of_transactions):
        date_time = faker.date_time_between(
                start_date = datetime(2019,1,1),
                tzinfo = pytz.timezone("Europe/Sarajevo"))

        account_index = random.choice(range(len(accounts)))

        designation_cat = random.choice(list(Designations))
        if accounts[account_index][4] / accounts[account_index][3] < .7:
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
            elif designation_cat == Designations.salary:
                amount = float(round(random.uniform(1, 10000), 2))
                accounts[account_index][3] += amount
            elif designation_cat == Designations.other:
                amount = float(round(random.uniform(1, 100), 2))

            accounts[account_index][4] += amount

        else:
            designation_cat = Designations.salary
            amount = float(round(random.uniform(1400, 10000), 2))
            accounts[account_index][3] += amount
            

        data.append([
                date_time.strftime("%-d.%-m.%Y %H:%M"),
                random.choice(designation_cat.value),
                amount, accounts[account_index][0], accounts[account_index][1], accounts[account_index][2]])

    dataFrame = pd.DataFrame(data, columns = columns)

    if not os.path.exists(os.path.join(os.getcwd(), "exports")):
        os.makedirs("exports")

    now = datetime.now().strftime("%-d-%-m-%Y_%H-%M")
    dataFrame.to_csv(os.path.join(os.getcwd(), "exports", f"export_{ now }_accounts_{ len(accounts) }.csv"), sep = delimiter, index = False)

    print(dataFrame)

    for i in accounts:
        print(i)

if __name__ == "__main__":
    main()

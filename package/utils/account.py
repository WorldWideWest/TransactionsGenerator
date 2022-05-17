import random
from .constants import Banks

class Account(object):

    def generate_accounts(self, number_of_accounts:int) -> list:
        accounts, banks = [], list(Banks)
        account_no, iban_no = "", ""

        for _ in range(number_of_accounts):
            
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

        return accounts
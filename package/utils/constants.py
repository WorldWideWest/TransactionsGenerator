from enum import Enum
from datetime import datetime

class Banks(Enum):
    bank_no_1 = "UniCredit Bank"
    bank_no_2 = "Sberbank Bank"
    bank_no_3 = "Raiffeisen Bank"
    bank_no_4 = "Bosna Bank International"
    bank_no_5 = "Intesa Sanpaolo Bank"
    bank_no_6 = "NLB Bank"
    bank_no_7 = "Ziraat Banka"
    bank_no_8 = "Sparkasse Bank"

class Designations(Enum):
    vehicle = ["ecotok", "gazprom", "hifa benz", "autoceste"]
    loan = ["kredit", "trajni nalog", "naplata po kredit.kartici"]
    pharmacy = ["apoteka", "pharmacy", "pharm"]
    bank_fee = ["naknada", "tekuci rn kamata", "provizija za nalog", "provision"]
    atm = ["atm"]
    shopping = ["doo", "kupovina", "bingo", "konzum", "merkator"]
    salary = ["plata", "topli", "prevoz", "uplata"]
    other = ["usluga", "kesa", "poklon", "teretana", "kino", "kafa", "izlazak"]

class Config(Enum):
    """ The configuration file contains constatns for generating the file name and date time formats for unix platforms and windows platform """
    fileName = lambda now, accounts, data: f"EXPORT_{ now }_ACC_{ len(accounts) }_TRA_{ len(data) }.csv"
    # Faker date fromat, File name date format
    dateFormatWin32 = ["%d.%m.%Y  %H:%M", "%d_%m_%Y_%H_%M"] 
    dateFormatUnix = ["%-d.%-m.%Y %H:%M", "%-d-%-m-%Y_%H-%M"] 


class Input(object):
    def get_inputs():
        number_of_accounts = int(input("Number of accounts: "))
        number_of_transactions = int(input("Number of transactions: "))
        delimiter = str(input("Please insert your delimiter: "))
        print()
        return number_of_accounts, number_of_transactions, delimiter
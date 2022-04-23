from enum import Enum

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

import pandas as pd
from faker import Faker
from datetime import datetime
import random, pytz, os, logging, sys

from utils.constants import Designations, Config, Input
from utils.account import Account
from utils.logger import Logger

def main():
    inputer, config = Input, Config
    inputs = inputer.get_inputs()

    account, faker = Account(), Faker()
    accounts = account.generate_accounts(inputs[0])

    designations = list(Designations)
    designations.remove(designations[6])

    data, amount = [], 0
    
    for _ in range(inputs[1]):
        date_time = faker.date_time_between(start_date = datetime(2019,1,1), tzinfo = pytz.timezone("Europe/Sarajevo"))

        index = random.choice(range(len(accounts)))

        designation_cat = random.choice(list(Designations))
        if accounts[index][4] / accounts[index][3] < .7:
            if designation_cat == Designations.vehicle:
                amount = float(round(random.uniform(1, 100), 2))
            elif designation_cat == Designations.loan:
                amount = float(round(random.uniform(100, 5000), 2))
            elif designation_cat == Designations.pharmacy:
                amount = float(round(random.uniform(1, 100), 2))
            elif designation_cat == Designations.bank_fee:
                amount = float(round(random.uniform(1, 10), 2))
            elif designation_cat == Designations.atm:
                amount = float(round(random.uniform(1, 500), 2))
            elif designation_cat == Designations.shopping:
                amount = float(round(random.uniform(1, 1000), 2))
            elif designation_cat == Designations.other:
                amount = float(round(random.uniform(1, 50), 2))
            accounts[index][4] += amount
        else:
            designation_cat = Designations.salary
            accounts[index][3] += float(round(random.uniform(1400, 5000), 2))

        data.append([date_time.strftime(config.DATE_FROMAT_UNIX.value[0] if sys.platform != "win32" else config.dateFormatWin32.value[0]), random.choice(designation_cat.value),
                amount, accounts[index][0], accounts[index][1], accounts[index][2]])

    dataFrame = pd.DataFrame(data, columns = config.COLUMNS.value)

    if not os.path.exists(os.path.join(os.getcwd(), config.DIR_NAME.value)):
        os.makedirs(config.DIR_NAME)

    logger = Logger(level = logging.INFO)
    logger = logger.get_logger()

    now = datetime.now().strftime(config.DATE_FROMAT_UNIX.value[1] if sys.platform != "win32" else config.dateFormatWin32.value[1])
    fileName = config.fileName(now, accounts, data)
    dataFrame.to_csv(os.path.join(os.getcwd(), config.DIR_NAME.value, fileName), sep = inputs[2], index = False)

    logger.info(config.LOG_MESSAGE(len(accounts), len(data), os.path.join(os.getcwd(), config.DIR_NAME.value, fileName)))

if __name__ == "__main__":
    main()

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6](https://img.shields.io/badge/python-3.8.10-blue.svg)](https://www.python.org/downloads/release/python-381/)

# TransactionsGenerator

## General info
The transaction generator is a simple python script that generates transactions data.
The script generates an bank account with `account number`, `iban`, `bank` and the assigns an transaction to that specific account.

The transactions are generated randomly for the time period from 1.1.2019 to today with different designations, amounts and timestamps.

After it generates the transactions and assigns them to the accounts it exports these transactions to a `.csv` file in the `/exports` folder which is generated on running the script.

## Running the script
Before you try to run the script please check if you [updated](https://www.theuptide.com/upgrade-pip/) `pip` because it can cause errors with the process of installing the necessary packages for this script.
To run the script you need to create an virtual environment for python, and you will do that by typing:
```bash
python3 -m venv env # env is the name of the environment
```
After the environment folder is create you run:
```bash
source env/bin/activate
```
Which should activate your environment, after that run the command to install all required packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Once all packages are installed you should be able to run the script. As you try to run the script you'll be prompted to insert 3 values:
```bash
python cli.py
```

Once you run the command you'll be asked to input these values:
1. Number of accounts - This value accepts an integer in range from 1 - 8, beacues a user can have only one account for one bank
2. Number of transactions - Here you can set any positive amount
3. Delimiter - The delimiter value that is going to sperate values between columns

The generated data is now available in the `exports` folder that the script created and it is in the form of a `.csv` file.
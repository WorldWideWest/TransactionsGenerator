# TransactionsGenerator

## General info
The transaction generator is a simple python script that generates transactions data.
The script generates an bank account with `account number`, `iban`, `bank` and the assigns an transaction to that specific account.

The transactions are generated randomly for the time period from 1.1.2019 to today with different designations, amounts and timestamps.

After it generates the transactions and assigns them to the accounts it exports these transactions to a `.csv` file in the `/exports` folder which is generated on running the script.

## Running the script
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
Once all packages are installed you should be able to run the script. But before that you need to pass two variables to the script on running it and these are the `number of accounts you want to generate` and `number of transactions`:
```bash
python generator.py 3 50 
# 3 - number of accounts that are generated
# 50 - number of transactions that are generated
```

The generated data is now available in the `transactions` folder that the script created and it is in the form of a `.csv` file.
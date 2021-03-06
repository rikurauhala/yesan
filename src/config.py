import os

from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATA_FOLDER_PATH = os.path.join(dirname, "..", "data")

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(DATA_FOLDER_PATH, DATABASE_FILENAME)

ACCOUNTS_FILENAME = os.getenv("ACCOUNTS_FILENAME") or "accounts.csv"
ACCOUNTS_FILE_PATH = os.path.join(DATA_FOLDER_PATH, ACCOUNTS_FILENAME)

TRANSACTIONS_FILENAME = os.getenv("TRANSACTIONS_FILENAME") or "transactions.csv"
TRANSACTIONS_FILE_PATH = os.path.join(DATA_FOLDER_PATH, TRANSACTIONS_FILENAME)

THOUSANDS_SEPARATOR = os.getenv("THOUSANDS_SEPARATOR") or " "

DECIMAL_SEPARATOR = os.getenv("DECIMAL_SEPARATOR") or ","

CURRENCY_SYMBOL = os.getenv("CURRENCY_SYMBOL") or "€"

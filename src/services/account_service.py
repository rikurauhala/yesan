import csv

from config import ACCOUNTS_FILE_PATH

from database_operations import get_database_connection

from entities.account import Account

from repositories.account_repository import AccountRepository


class AccountService:

    def __init__(self):
        self._account_repository = AccountRepository(get_database_connection())

    def create_account(self, account_name, account_type):
        return self._account_repository.create(account_name, account_type)

    def find_all(self):
        return self._account_repository.find_all()

    def get_list(self):
        return self._account_repository.get_list()

    def get_id_by_name(self, name):
        return self._account_repository.get_id_by_name(name)

    def delete_all(self):
        return self._account_repository.delete_all()

    def export(self):
        accounts = self.find_all()

        with open(ACCOUNTS_FILE_PATH, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            for account in accounts:
                details = []
                details.append(account.id)
                details.append(account.name)
                details.append(account.type)
                writer.writerow(details)

        return True

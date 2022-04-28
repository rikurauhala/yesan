from file_handler import file_handler

from repositories.account_repository import account_repository


class AccountService:

    def __init__(self):
        self._account_repository = account_repository

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
        return file_handler.export_accounts(accounts)

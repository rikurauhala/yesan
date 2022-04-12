from database.database_operations import get_database_connection
from entities.account import Account
from repositories.account_repository import AccountRepository


class AccountService:

    def __init__(self):
        self._account_repository = AccountRepository(get_database_connection())

    def create_account(self, account_name, account_type):
        new_account = Account(None, account_name, account_type)
        return self._account_repository.create(new_account)

    def find_all(self):
        return self._account_repository.find_all()

    def get_list(self):
        return self._account_repository.get_list()

    def get_id_by_name(self, name):
        return self._account_repository.get_id_by_name(name)

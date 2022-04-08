from database.database_connection import get_database_connection
from entities.account import Account
from repositories.account_repository import AccountRepository


class AccountService:

    def __init__(self):
        self._account_repository = AccountRepository(get_database_connection())

    def create_account(self, name, type):
        new_account = Account(name, type)
        return self._account_repository.create(new_account)

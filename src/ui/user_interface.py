from ui.views.main_view import MainView
from ui.views.account_view import AccountView
from ui.views.new_account_view import NewAccountView
from ui.views.transaction_view import TransactionView
from ui.views.new_transaction_view import NewTransactionView


class UserInterface:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _go_to_main_view(self):
        self._show_main_view()

    def _go_to_account_view(self):
        self._show_account_view()

    def _go_to_new_account_view(self):
        self._show_new_account_view()

    def _go_to_transaction_view(self):
        self._show_transaction_view()

    def _go_to_new_transaction_view(self):
        self._show_new_transaction_view()

    def _show_main_view(self):
        self._hide_current_view()
        self._current_view = MainView(
            self._root,
            self._go_to_account_view,
            self._go_to_transaction_view
        )
        self._current_view.pack()

    def _show_account_view(self):
        self._hide_current_view()
        self._current_view = AccountView(
            self._root,
            self._go_to_main_view,
            self._go_to_new_account_view
        )
        self._current_view.pack()

    def _show_new_account_view(self):
        self._hide_current_view()
        self._current_view = NewAccountView(
            self._root,
            self._go_to_account_view
        )
        self._current_view.pack()

    def _show_transaction_view(self):
        self._hide_current_view()
        self._current_view = TransactionView(
            self._root,
            self._go_to_main_view,
            self._go_to_new_transaction_view
        )
        self._current_view.pack()

    def _show_new_transaction_view(self):
        self._hide_current_view()
        self._current_view = NewTransactionView(
            self._root,
            self._go_to_transaction_view
        )
        self._current_view.pack()

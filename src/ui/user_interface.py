from ui.views.new_account_view import NewAccountView


class UserInterface:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_account_view()

    def _show_account_view(self):
        self._current_view = NewAccountView(self._root)
        self._current_view.pack()

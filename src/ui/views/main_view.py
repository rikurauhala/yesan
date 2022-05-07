from tkinter import constants, ttk
from tkinter.messagebox import askyesno

import ui.styles.fonts as fonts
import ui.styles.styles as styles


class MainView:
    """The main view (main menu) of the application."""

    def __init__(self, root, go_to_account_view, go_to_transaction_view, go_to_settings_view):
        """Initializes the view.

        Args:
            root (Tk): The main window.
            go_to_accounts_view (function): Called to go to the account view.
            go_to_transaction_view (function): Called to go to the transaction view.
            go_to_settings_view (function): Called to go to the settings view.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._go_to_account_view = go_to_account_view
        self._go_to_transaction_view = go_to_transaction_view
        self._go_to_settings_view = go_to_settings_view
        self._initialize()

    def pack(self):
        """Displays the view."""
        self._frame.pack(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def destroy(self):
        """Hides the view."""
        self._frame.destroy()

    def _initialize_title_label(self):
        txt_title = "Yesan"
        lbl_title = ttk.Label(
            master=self._frame,
            text=txt_title,
            font=fonts.TITLE,
            justify=constants.CENTER
        )
        lbl_title.grid(
            row=0,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_accounts_button(self):
        txt_accounts = "Accounts"
        btn_accounts = ttk.Button(
            master=self._frame,
            text=txt_accounts,
            command=self._go_to_account_view
        )
        btn_accounts.grid(
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_transactions_button(self):
        txt_transactions = "Transactions"
        btn_transactions = ttk.Button(
            master=self._frame,
            text=txt_transactions,
            command=self._go_to_transaction_view
        )
        btn_transactions.grid(
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_settings_button(self):
        txt_settings = "Settings"
        btn_settings = ttk.Button(
            master=self._frame,
            text=txt_settings,
            command=self._go_to_settings_view
        )
        btn_settings.grid(
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _handle_quit(self):
        answer = askyesno(
            title="Confirmation",
            message="Are you sure you want to quit?"
        )
        if answer:
            self._root.destroy()

    def _initialize_quit_button(self):
        txt_quit = "Quit"
        btn_quit = ttk.Button(
            master=self._frame,
            text=txt_quit,
            command=self._handle_quit
        )
        btn_quit.grid(
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_accounts_button()
        self._initialize_transactions_button()
        self._initialize_settings_button()
        self._initialize_quit_button()

from tkinter import constants, StringVar, ttk
from tkinter.messagebox import askyesno

from services.account_service import AccountService
from services.transaction_service import TransactionService

from ui.message.message import Message

import ui.styles.colors as colors
import ui.styles.fonts as fonts
import ui.styles.styles as styles


class AccountView:
    """A view that displays information about accounts."""

    def __init__(self, root, go_to_main_view, go_to_new_account_view):
        """Initializes the view.

        Args:
            root (Tk): The main window.
            go_to_main_view (function): Called to go back to the main view.
            go_to_new_account_view (function): Called to go to the new account view.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._buttons = ttk.Frame(master=self._frame)
        self._var_message = StringVar(self._frame)
        self._message = Message(self._frame, self._var_message)
        self._lbl_message = None
        self._go_to_main_view = go_to_main_view
        self._go_to_new_account_view = go_to_new_account_view
        self._account_service = AccountService()
        self._transaction_service = TransactionService()
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
        txt_title = "Accounts"
        lbl_title = ttk.Label(
            master=self._frame,
            text=txt_title,
            font=fonts.TITLE
        )
        lbl_title.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

    def _initialize_subtitles(self):
        txt_name = "Name"
        lbl_name = ttk.Label(
            master=self._frame,
            text=txt_name,
            font=fonts.SUBTITLE
        )
        lbl_name.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_type = "Type"
        lbl_type = ttk.Label(
            master=self._frame,
            text=txt_type,
            font=fonts.SUBTITLE
        )
        lbl_type.grid(
            row=1,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_balance = "Balance"
        lbl_balance = ttk.Label(
            master=self._frame,
            text=txt_balance,
            font=fonts.SUBTITLE
        )
        lbl_balance.grid(
            row=1,
            column=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_account_information(self, accounts, total):
        for i in range(total):
            txt_name = accounts[i].name
            lbl_name = ttk.Label(
                master=self._frame,
                text=txt_name
            )
            lbl_name.grid(
                row=i+2,
                column=0,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
            )

            txt_type = accounts[i].type
            lbl_type = ttk.Label(
                master=self._frame,
                text=txt_type
            )
            lbl_type.grid(
                row=i+2,
                column=1,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
            )

            account_id = self._account_service.get_id_by_name(accounts[i].name)
            txt_balance = self._transaction_service.get_balance_by_id(
                account_id
            )
            if not txt_balance:
                txt_balance = "0.00 ???"
            else:
                txt_balance = self._transaction_service.format_amount(
                    txt_balance
                )
            lbl_balance = None
            if str(txt_balance)[0] == "-":
                lbl_balance = ttk.Label(
                    master=self._frame,
                    text=txt_balance,
                    foreground=colors.NEGATIVE
                )
            else:
                lbl_balance = ttk.Label(
                    master=self._frame,
                    text=txt_balance
                )
            lbl_balance.grid(
                row=i+2,
                column=2,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.E
            )

    def _initialize_net_worth_separator(self, total):
        separator = ttk.Separator(master=self._frame, orient="horizontal")
        separator.grid(
            row=total+2,
            column=0,
            columnspan=3,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_net_worth_label(self, total):
        txt_net_worth = "Net worth"
        lbl_net_worth = ttk.Label(
            master=self._frame,
            text=txt_net_worth,
            font=fonts.BOLD
        )
        lbl_net_worth.grid(
            row=total+3,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_net_worth_info(self, total):
        net_worth = self._transaction_service.calculate_net_worth()
        txt_net_worth = self._transaction_service.format_amount(net_worth)
        lbl_net_worth = ttk.Label(
            master=self._frame,
            text=txt_net_worth,
            font=fonts.BOLD
        )
        lbl_net_worth.grid(
            row=total+3,
            column=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, code):
        self._lbl_message = self._message.get_message(code)
        self._lbl_message.grid(
            columnspan=3,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_back_button(self):
        txt_back = "?? Back"
        btn_back = ttk.Button(
            master=self._buttons,
            text=txt_back,
            command=self._go_to_main_view
        )
        btn_back.grid(
            row=0,
            column=0,
            padx=styles.PADDING_RIGHT
        )

    def _initialize_new_account_button(self):
        txt_new_account = "+ New account"
        btn_new_account = ttk.Button(
            master=self._buttons,
            text=txt_new_account,
            command=self._go_to_new_account_view
        )
        btn_new_account.grid(
            row=0,
            column=1,
            padx=styles.PADDING_RIGHT
        )

    def _handle_import(self):
        self._clear_message()
        answer = askyesno(
            title="Confirmation",
            message="Are you sure you want to import accounts?"
        )
        if answer:
            success = self._account_service.import_accounts()
            if not success:
                self._display_message("e-02")
            else:
                self._display_message("s-05")

    def _initialize_import_button(self):
        txt_import = "??? Import"
        btn_import = ttk.Button(
            master=self._buttons,
            text=txt_import,
            command=lambda: self._handle_import()
        )
        btn_import.grid(
            row=0,
            column=2,
            padx=styles.PADDING_RIGHT
        )

    def _handle_export(self):
        self._clear_message()
        answer = askyesno(
            title="Confirmation",
            message="Are you sure you want to export accounts?"
        )
        if answer:
            success = self._account_service.export_accounts()
            if not success:
                self._display_message("e-01")
            else:
                self._display_message("s-01")

    def _initialize_export_button(self):
        txt_export = "??? Export"
        btn_export = ttk.Button(
            master=self._buttons,
            text=txt_export,
            command=lambda: self._handle_export()
        )
        btn_export.grid(
            row=0,
            column=3,
            padx=styles.PADDING_RIGHT
        )

    def _initialize_buttons(self):
        self._initialize_back_button()
        self._initialize_new_account_button()
        self._initialize_import_button()
        self._initialize_export_button()
        self._buttons.grid(
            columnspan=3,
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_subtitles()
        accounts = self._account_service.find_all()
        total = len(accounts)
        self._initialize_account_information(accounts, total)
        self._initialize_net_worth_separator(total)
        self._initialize_net_worth_label(total)
        self._initialize_net_worth_info(total)
        self._initialize_buttons()

from datetime import date

from tkinter import constants, END, StringVar, ttk

from tkcalendar import DateEntry

from services.account_service import AccountService
from services.transaction_service import TransactionService

from ui.validator import Validator

from ui.message.message import Message

import ui.styles.colors as colors
import ui.styles.styles as styles


class NewTransactionView:
    """A view that offers an interface for creating a new transaction."""

    def __init__(self, root, go_to_transaction_view):
        """Initializes thew view.

        Args:
            root (Tk): The main window.
            go_to_transaction_view (function): Called to go back to the transaction view.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._lbl_message = None
        self._var_message = StringVar(self._frame)
        self._message = Message(self._frame, self._var_message)
        self._go_to_transaction_view = go_to_transaction_view
        self._ent_date = None
        self._ent_amount = None
        self._ent_category = None
        self._ent_description = None
        self._opt_account = None
        self._var_account = None
        self._ent_party = None
        self._accounts = None
        self._account_service = AccountService()
        self._transaction_service = TransactionService()
        self._validator = Validator()
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

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, code):
        self._lbl_message = self._message.get_message(code)
        self._lbl_message.grid(
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _validate_input(self):
        date_code = self._validator.validate_transaction_date(
            self._ent_date.get_date()
        )
        amount_code = self._validator.validate_transaction_amount(
            self._ent_amount.get()
        )
        category_code = self._validator.validate_transaction_category(
            self._ent_category.get()
        )
        description_code = self._validator.validate_transaction_description(
            self._ent_description.get()
        )
        account_name_code = self._validator.validate_transaction_account_name(
            self._var_account.get()
        )
        party_code = self._validator.validate_transaction_party(
            self._ent_party.get()
        )

        valid = True

        if date_code[0] == "e":
            self._display_message(date_code)
            valid = False
        elif amount_code[0] == "e":
            self._display_message(amount_code)
            valid = False
        elif category_code[0] == "e":
            self._display_message(category_code)
            valid = False
        elif description_code[0] == "e":
            self._display_message(description_code)
            valid = False
        elif account_name_code[0] == "e":
            self._display_message(account_name_code)
            valid = False
        elif party_code[0] == "e":
            self._display_message(party_code)
            valid = False

        return valid

    def _reset_fields(self):
        self._ent_date.set_date(date.today())
        self._ent_amount.delete(0, END)
        self._ent_category.delete(0, END)
        self._ent_description.delete(0, END)
        self._var_account.set("Select an account")
        self._ent_party.delete(0, END)

    def _handle_submit(self):
        self._clear_message()

        date = self._ent_date.get_date()
        amount = self._ent_amount.get()
        category = self._ent_category.get()
        description = self._ent_description.get()
        account_name = self._var_account.get()
        party = self._ent_party.get()

        if not self._validate_input():
            return

        account_id = self._account_service.get_id_by_name(account_name)
        self._transaction_service.create_transaction(
            date,
            amount,
            category,
            description,
            account_id,
            party
        )
        self._display_message("s-04")
        self._reset_fields()

    def _initialize_title_label(self):
        txt_title = "Add new transaction"
        lbl_title = ttk.Label(
            master=self._frame,
            text=txt_title
        )
        lbl_title.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

    def _initialize_date_label(self):
        txt_date = "Date"
        lbl_date = ttk.Label(
            master=self._frame,
            text=txt_date)
        lbl_date.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_date_entry(self):
        current_year = date.today().year
        self._ent_date = DateEntry(
            master=self._frame,
            background=colors.DARK_BLUE,
            foreground=colors.WHITE,
            borderwidth=2,
            date_pattern="YYYY-MM-DD",
            year=current_year
        )
        self._ent_date.grid(
            row=1,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_amount_label(self):
        txt_amount = "Amount"
        lbl_amount = ttk.Label(
            master=self._frame,
            text=txt_amount
        )
        lbl_amount.grid(
            row=2,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_amount_entry(self):
        self._ent_amount = ttk.Entry(master=self._frame)
        self._ent_amount.grid(
            row=2,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_category_label(self):
        txt_category = "Category"
        lbl_category = ttk.Label(
            master=self._frame,
            text=txt_category
        )
        lbl_category.grid(
            row=3,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_category_entry(self):
        self._ent_category = ttk.Entry(master=self._frame)
        self._ent_category.grid(
            row=3,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_description_label(self):
        txt_description = "Description"
        lbl_description = ttk.Label(
            master=self._frame,
            text=txt_description
        )
        lbl_description.grid(
            row=4,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_description_entry(self):
        self._ent_description = ttk.Entry(master=self._frame)
        self._ent_description.grid(
            row=4,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_account_label(self):
        txt_account = "Account"
        lbl_description = ttk.Label(
            master=self._frame,
            text=txt_account
        )
        lbl_description.grid(
            row=5,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_account_option_menu(self):
        self._accounts = self._account_service.get_list()
        self._var_account = StringVar(master=self._frame)
        txt_select_an_account = "Select an account"
        self._opt_account = ttk.OptionMenu(
            self._frame,
            self._var_account,
            txt_select_an_account,
            *self._accounts
        )
        self._opt_account.grid(
            row=5,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_party_label(self):
        txt_party = "Payer / Receiver"
        lbl_party = ttk.Label(
            master=self._frame,
            text=txt_party
        )
        lbl_party.grid(
            row=6,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_party_entry(self):
        self._ent_party = ttk.Entry(master=self._frame)
        self._ent_party.grid(
            row=6,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_back_button(self):
        txt_back = "?? Back"
        btn_back = ttk.Button(
            master=self._frame,
            text=txt_back,
            command=self._go_to_transaction_view
        )
        btn_back.grid(
            row=7,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_submit_button(self):
        txt_submit = "??? Submit"
        btn_submit = ttk.Button(
            master=self._frame,
            text=txt_submit,
            command=self._handle_submit
        )
        btn_submit.grid(
            row=7,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_date_label()
        self._initialize_date_entry()
        self._initialize_amount_label()
        self._initialize_amount_entry()
        self._initialize_category_label()
        self._initialize_category_entry()
        self._initialize_description_label()
        self._initialize_description_entry()
        self._initialize_account_label()
        self._initialize_account_option_menu()
        self._initialize_party_label()
        self._initialize_party_entry()
        self._initialize_back_button()
        self._initialize_submit_button()

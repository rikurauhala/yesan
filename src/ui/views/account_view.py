from tkinter import constants, ttk

from services.account_service import AccountService
from services.transaction_service import TransactionService

import ui.styles.colors as colors
import ui.styles.fonts as fonts
import ui.styles.styles as styles


class AccountView:
    def __init__(self, root, go_to_main_view, go_to_new_account_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._go_to_main_view = go_to_main_view
        self._go_to_new_account_view = go_to_new_account_view
        self._account_service = AccountService()
        self._transaction_service = TransactionService()
        self._initialize()

    def pack(self):
        self._frame.pack(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def destroy(self):
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
            sticky=constants.W
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
            txt_balance = self._transaction_service.get_balance_by_id(account_id)
            if not txt_balance:
                txt_balance = "0.00 €"
            else:
                euro = str(int(txt_balance/100))
                cents = str(txt_balance)[-2:]
                txt_balance = euro + "." + cents + " €"
            lbl_balance = None
            if txt_balance[0] == "-":
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

    def _initialize_back_button(self, total):
        txt_back = "« Back"
        btn_back = ttk.Button(
            master=self._frame,
            text=txt_back,
            command=self._go_to_main_view
        )
        btn_back.grid(
            row=total+2,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_new_account_button(self, total):
        txt_new_account = "+ New account"
        btn_new_account = ttk.Button(
            master=self._frame,
            text=txt_new_account,
            command=self._go_to_new_account_view
        )
        btn_new_account.grid(
            row=total+2,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_subtitles()
        accounts = self._account_service.find_all()
        total = len(accounts)
        self._initialize_account_information(accounts, total)
        self._initialize_back_button(total)
        self._initialize_new_account_button(total)

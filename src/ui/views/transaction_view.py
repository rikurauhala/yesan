from tkinter import constants, ttk

from services.transaction_service import TransactionService

import ui.styles.colors as colors
import ui.styles.fonts as fonts
import ui.styles.styles as styles


class TransactionView:
    def __init__(self, root, go_to_main_view, go_to_new_transaction_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._go_to_main_view = go_to_main_view
        self._go_to_new_transaction_view = go_to_new_transaction_view
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
        txt_title = "Transactions"
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
        txt_date = "Date"
        lbl_date = ttk.Label(
            master=self._frame,
            text=txt_date,
            font=fonts.SUBTITLE
        )
        lbl_date.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_amount = "Amount"
        lbl_amount = ttk.Label(
            master=self._frame,
            text=txt_amount,
            font=fonts.SUBTITLE
        )
        lbl_amount.grid(
            row=1,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_category = "Category"
        lbl_category = ttk.Label(
            master=self._frame,
            text=txt_category,
            font=fonts.SUBTITLE
        )
        lbl_category.grid(
            row=1,
            column=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_description = "Description"
        lbl_description = ttk.Label(
            master=self._frame,
            text=txt_description,
            font=fonts.SUBTITLE
        )
        lbl_description.grid(
            row=1,
            column=3,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_account = "Account"
        lbl_account = ttk.Label(
            master=self._frame,
            text=txt_account,
            font=fonts.SUBTITLE
        )
        lbl_account.grid(
            row=1,
            column=4,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

        txt_party = "Payer / receiver"
        lbl_party = ttk.Label(
            master=self._frame,
            text=txt_party,
            font=fonts.SUBTITLE
        )
        lbl_party.grid(
            row=1,
            column=5,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

    def _initialize_transaction_information(self, transactions, total):
        for i in range(total):
            txt_date = transactions[i].timestamp
            lbl_date = ttk.Label(
                master=self._frame,
                text=txt_date
            )
            lbl_date.grid(
                row=i+2,
                column=0,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
            )

            txt_amount = "{:.2f} €".format(transactions[i].amount/100)
            lbl_amount = None
            if txt_amount[0] == "-":
                lbl_amount = ttk.Label(
                    master=self._frame,
                    text=txt_amount,
                    foreground=colors.NEGATIVE
                )
            else:
                lbl_amount = ttk.Label(
                    master=self._frame,
                    text=txt_amount
                )
            lbl_amount.grid(
                row=i+2,
                column=1,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.E
            )

            txt_category = transactions[i].category
            lbl_category = ttk.Label(
                master=self._frame,
                text=txt_category
            )
            lbl_category.grid(
                row=i+2,
                column=2,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
            )

            txt_description = transactions[i].description
            lbl_description = ttk.Label(
                master=self._frame,
                text=txt_description
            )
            lbl_description.grid(
                row=i+2,
                column=3,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
            )

            txt_account = transactions[i].account_id
            lbl_account = ttk.Label(
                master=self._frame,
                text=txt_account
            )
            lbl_account.grid(
                row=i+2,
                column=4,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
            )

            txt_party = transactions[i].party
            lbl_party = ttk.Label(
                master=self._frame,
                text=txt_party
            )
            lbl_party.grid(
                row=i+2,
                column=5,
                padx=styles.PADDING,
                pady=styles.PADDING,
                sticky=constants.W
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

    def _initialize_new_transaction_button(self, total):
        txt_new_transaction = "New transaction"
        btn_new_transaction = ttk.Button(
            master=self._frame,
            text=txt_new_transaction,
            command=self._go_to_new_transaction_view
        )
        btn_new_transaction.grid(
            row=total+2,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_subtitles()
        transactions = self._transaction_service.find_all()
        total = len(transactions)
        self._initialize_transaction_information(transactions, total)
        self._initialize_back_button(total)
        self._initialize_new_transaction_button(total)

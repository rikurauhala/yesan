from tkinter import constants, StringVar, ttk
from tkinter.messagebox import askyesno

from services.transaction_service import TransactionService

import ui.styles.colors as colors
import ui.styles.fonts as fonts
import ui.styles.styles as styles


class TransactionView:
    def __init__(self, root, go_to_main_view, go_to_new_transaction_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._buttons = ttk.Frame(master=self._frame)
        self._lbl_message = None
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
            txt_date = transactions[i].date
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

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, mode):
        self._var_message = StringVar(self._frame)
        if mode == "missing":
            self._var_message.set(
                "Importing transactions is not supported yet!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "error":
            self._var_message.set("Exporting transactions failed!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "success":
            self._var_message.set("Transactions exported successfully!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.SUCCESS
            )
        self._lbl_message.grid(
            columnspan=6,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_back_button(self):
        txt_back = "« Back"
        btn_back = ttk.Button(
            master=self._buttons,
            text=txt_back,
            command=self._go_to_main_view
        )
        btn_back.grid(
            row=0,
            column=0,
            padx=styles.PADDING_RIGHT,
            sticky=constants.EW
        )

    def _initialize_new_transaction_button(self):
        txt_new_transaction = "+ New transaction"
        btn_new_transaction = ttk.Button(
            master=self._buttons,
            text=txt_new_transaction,
            command=self._go_to_new_transaction_view
        )
        btn_new_transaction.grid(
            row=0,
            column=1,
            padx=styles.PADDING_RIGHT,
            sticky=constants.EW
        )

    def _handle_import(self):
        self._clear_message()
        self._display_message("missing")

    def _initialize_import_button(self):
        txt_import = "↓ Import"
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
            message="Are you sure you want to export transactions?"
        )
        if answer:
            success = self._transaction_service.export()
            if not success:
                self._display_message("error")
            else:
                self._display_message("success")

    def _initialize_export_button(self):
        txt_export = "↑ Export"
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
        self._initialize_new_transaction_button()
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
        transactions = self._transaction_service.find_all()
        total = len(transactions)
        self._initialize_transaction_information(transactions, total)
        self._initialize_back_button()
        self._initialize_new_transaction_button()
        self._initialize_buttons()

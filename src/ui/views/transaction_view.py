from tkinter import constants, END, StringVar, ttk
from tkinter.messagebox import askyesno

from services.transaction_service import TransactionService

from ui.message import Message

import ui.styles.colors as colors
import ui.styles.fonts as fonts
import ui.styles.styles as styles


class TransactionView:
    def __init__(self, root, go_to_main_view, go_to_new_transaction_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._data_tree = None
        self._buttons = ttk.Frame(master=self._frame)
        self._lbl_message = None
        self._var_message = StringVar(self._frame)
        self._message = Message(self._frame, self._var_message)
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

    def _initialize_data_tree(self):
        columns = (
            "date",
            "amount",
            "category",
            "description",
            "account",
            "party"
        )

        self._data_tree = ttk.Treeview(
            master=self._frame,
            columns=columns,
            show="headings",
            height=20
        )

        self._data_tree.heading("date", text="Date")
        self._data_tree.column("date", anchor=constants.CENTER, width=100)
        self._data_tree.heading("amount", text="Amount")
        self._data_tree.column("amount", anchor=constants.E, width=120)
        self._data_tree.heading("category", text="Category")
        self._data_tree.heading("description", text="Description")
        self._data_tree.heading("account", text="Account")
        self._data_tree.heading("party", text="Payer / Receiver")

        transactions = self._transaction_service.find_all_as_list()

        for transaction in transactions:
            if transaction[1][0] == "-":
                self._data_tree.insert(
                    "", END, values=transaction, tags=("negative", ))
            else:
                self._data_tree.insert("", END, values=transaction)

        self._data_tree.tag_configure("negative", foreground=colors.NEGATIVE)
        self._data_tree.grid(row=1, column=0, sticky="NSEW")
        self._initialize_scrollbar()

    def _initialize_scrollbar(self):
        scrollbar = ttk.Scrollbar(
            self._frame,
            orient=constants.VERTICAL,
            command=self._data_tree.yview
        )
        self._data_tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="NS")

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, code):
        self._lbl_message = self._message.get_message(code)
        self._lbl_message.grid(
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
        answer = askyesno(
            title="Confirmation",
            message="Are you sure you want to import transactions?"
        )
        if answer:
            success = self._transaction_service.import_transactions()
            if not success:
                self._display_message("e-07")
            else:
                self._display_message("s-06")

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
            success = self._transaction_service.export_transactions()
            if not success:
                self._display_message("e-06")
            else:
                self._display_message("s-03")

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
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN,
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_data_tree()
        self._initialize_buttons()

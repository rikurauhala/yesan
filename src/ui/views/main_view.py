from tkinter import constants, ttk

import ui.styles.fonts as fonts
import ui.styles.styles as styles


class MainView:
    def __init__(self, root, go_to_accounts_view, go_to_new_transaction_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._go_to_accounts_view = go_to_accounts_view
        self._go_to_new_transaction_view = go_to_new_transaction_view
        self._initialize()

    def pack(self):
        self._frame.pack(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def destroy(self):
        self._frame.destroy()

    def _initialize_title_label(self):
        txt_title = "Yesan"
        lbl_title = ttk.Label(
            master=self._frame,
            text=txt_title,
            font=fonts.TITLE
        )
        lbl_title.grid(
            row=0,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

    def _initialize_accounts_button(self):
        txt_accounts = "Accounts"
        btn_accounts = ttk.Button(
            master=self._frame,
            text=txt_accounts,
            command=self._go_to_accounts_view
        )
        btn_accounts.grid(
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_new_transaction_button(self):
        txt_new_transaction = "New transaction"
        btn_new_transaction = ttk.Button(
            master=self._frame,
            text=txt_new_transaction,
            command=self._go_to_new_transaction_view
        )
        btn_new_transaction.grid(
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_accounts_button()
        self._initialize_new_transaction_button()

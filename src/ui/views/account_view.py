from tkinter import constants, ttk

from services.account_service import AccountService


class AccountView:
    def __init__(self, root, handle_new_account):
        self._root = root
        self._frame = None
        self._handle_new_account = handle_new_account
        self._padx = 7
        self._pady = 7
        self._account_service = AccountService()
        self._initialize()

    def pack(self):
        self._frame.pack(padx=10, pady=10)

    def destroy(self):
        self._frame.destroy()

    def _initialize_title_label(self):
        txt_title = "Accounts"
        lbl_title = ttk.Label(master=self._frame,
                              text=txt_title, font=("Helvetica", 16, "bold"))
        lbl_title.grid(row=0, column=0, columnspan=2,
                       padx=self._padx, pady=self._pady, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_title_label()

        font = ("Helvetica", 12, "bold")

        txt_name = "Name"
        lbl_name = ttk.Label(master=self._frame, text=txt_name, font=font)
        lbl_name.grid(row=1, column=0, padx=self._padx,
                      pady=self._pady, sticky=constants.W)

        txt_type = "Type"
        lbl_type = ttk.Label(master=self._frame, text=txt_type, font=font)
        lbl_type.grid(row=1, column=1, padx=self._padx,
                      pady=self._pady, sticky=constants.W)

        txt_balance = "Balance"
        lbl_balance = ttk.Label(master=self._frame, text=txt_balance, font=font)
        lbl_balance.grid(row=1, column=2, padx=self._padx,
                         pady=self._pady, sticky=constants.W)

        accounts = self._account_service.find_all()
        for i in range(len(accounts)):
            txt_name = accounts[i].name
            lbl_name = ttk.Label(master=self._frame, text=txt_name)
            lbl_name.grid(row=i+2, column=0, padx=self._padx,
                          pady=self._pady, sticky=constants.W)

            txt_type = accounts[i].type
            lbl_type = ttk.Label(master=self._frame, text=txt_type)
            lbl_type.grid(row=i+2, column=1, padx=self._padx,
                          pady=self._pady, sticky=constants.W)

            txt_balance = "0.00 €"
            lbl_balance = ttk.Label(master=self._frame, text=txt_balance)
            lbl_balance.grid(row=i+2, column=2, padx=self._padx,
                             pady=self._pady, sticky=constants.E)

        txt_new_account = "New account"
        btn_new_account = ttk.Button(master=self._frame, text=txt_new_account,
                                command=self._handle_new_account)
        btn_new_account.grid(row=(len(accounts)+2), column=0, padx=self._padx,
                        pady=self._pady, sticky=constants.EW)

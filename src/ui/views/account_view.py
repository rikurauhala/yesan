from tkinter import constants, ttk

from services.account_service import AccountService


class AccountView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._padx = 7
        self._pady = 7
        self._account_service = AccountService()
        self._initialize()

    def pack(self):
        self._frame.pack(padx=10, pady=10)

    def destroy(self):
        self._frame.destroy()

    def _handle_button(self):
        pass

    def _initialize_title_label(self):
        txt_title = "Accounts"
        lbl_title = ttk.Label(master=self._frame, text=txt_title)
        lbl_title.grid(row=0, column=0, columnspan=2,
                       padx=self._padx, pady=self._pady, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_title_label()

        accounts = self._account_service.find_all()
        for i in range(len(accounts)):
            txt_name = accounts[i].name
            lbl_name = ttk.Label(master=self._frame, text=txt_name)
            lbl_name.grid(row=i+1, column=0, padx=self._padx,
                          pady=self._pady, sticky=constants.W)

            txt_type = accounts[i].type
            lbl_type = ttk.Label(master=self._frame, text=txt_type)
            lbl_type.grid(row=i+1, column=1, padx=self._padx,
                          pady=self._pady, sticky=constants.W)


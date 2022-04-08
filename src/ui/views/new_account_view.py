from tkinter import ttk, constants

from services.account_service import AccountService


class NewAccountView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._ent_name = None
        self._ent_type = None
        self._account_service = AccountService()
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _handle_account_creation(self):
        name = self._ent_name.get()
        type = self._ent_type.get()
        self._account_service.create_account(name, type)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        padx = 7
        pady = 7

        txt_title = "Add new account"
        lbl_title = ttk.Label(master=self._frame, text=txt_title)
        lbl_title.grid(row=0, column=0, columnspan=2, padx=padx, pady=pady, sticky=constants.W)

        txt_name = "Name"
        lbl_name = ttk.Label(master=self._frame, text=txt_name)
        lbl_name.grid(row=1, column=0, padx=padx, pady=pady)

        self._ent_name = ttk.Entry(master=self._frame)
        self._ent_name.grid(row=1, column=1, padx=padx, pady=pady)

        txt_type = "Type"
        lbl_type = ttk.Label(master=self._frame, text=txt_type)
        lbl_type.grid(row=2, column=0, padx=padx, pady=pady)

        self._ent_type = ttk.Entry(master=self._frame)
        self._ent_type.grid(row=2, column=1, padx=padx, pady=pady)

        txt_submit = "Submit"
        btn_submit = ttk.Button(master=self._frame, text=txt_submit, 
                                command=self._handle_account_creation)
        btn_submit.grid(row=3, column=0, padx=padx, pady=pady, columnspan=2, sticky=constants.EW)


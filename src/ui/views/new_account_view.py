from tkinter import constants, END, StringVar, ttk

from services.account_service import AccountService


class NewAccountView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._padx = 7
        self._pady = 7
        self._ent_name = None
        self._ent_type = None
        self._var_message = None
        self._lbl_message = None
        self._account_service = AccountService()
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _handle_cancel(self):
        pass

    def _handle_submit(self):
        self._clear_message()
        name = self._ent_name.get()
        type = self._ent_type.get()
        self._account_service.create_account(name, type)
        self._var_message = StringVar(self._frame)
        self._var_message.set("New account added!")
        self._lbl_message = ttk.Label(
            master=self._frame,
            textvariable=self._var_message,
            foreground="green"
        )
        self._lbl_message.grid(columnspan=2, padx=self._padx, pady=self._pady)
        self._ent_name.delete(0, END)
        self._ent_type.delete(0, END)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        txt_title = "Add new account"
        lbl_title = ttk.Label(master=self._frame, text=txt_title)
        lbl_title.grid(row=0, column=0, columnspan=2,
                       padx=self._padx, pady=self._pady, sticky=constants.W)

        txt_name = "Name"
        lbl_name = ttk.Label(master=self._frame, text=txt_name)
        lbl_name.grid(row=1, column=0, padx=self._padx, pady=self._pady)

        self._ent_name = ttk.Entry(master=self._frame)
        self._ent_name.grid(row=1, column=1, padx=self._padx, pady=self._pady)

        txt_type = "Type"
        lbl_type = ttk.Label(master=self._frame, text=txt_type)
        lbl_type.grid(row=2, column=0, padx=self._padx, pady=self._pady)

        self._ent_type = ttk.Entry(master=self._frame)
        self._ent_type.grid(row=2, column=1, padx=self._padx, pady=self._pady)

        txt_cancel = "Cancel"
        btn_cancel = ttk.Button(master=self._frame, text=txt_cancel,
                                command=self._handle_cancel)
        btn_cancel.grid(row=3, column=0, padx=self._padx,
                        pady=self._pady, sticky=constants.EW)

        txt_submit = "Submit"
        btn_submit = ttk.Button(master=self._frame, text=txt_submit,
                                command=self._handle_submit)
        btn_submit.grid(row=3, column=1, padx=self._padx,
                        pady=self._pady, sticky=constants.EW)

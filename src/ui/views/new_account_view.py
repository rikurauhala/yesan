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
        self._frame.pack(padx=10, pady=10)

    def destroy(self):
        self._frame.destroy()

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, mode):
        self._var_message = StringVar(self._frame)
        if mode == "error":
            self._var_message.set("Please enter name and type!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground="red"
            )
        if mode == "success":
            self._var_message.set("New account added!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground="green"
            )
        self._lbl_message.grid(columnspan=2, padx=self._padx, pady=self._pady)

    def _handle_cancel(self):
        pass

    def _handle_submit(self):
        self._clear_message()
        name = self._ent_name.get()
        type = self._ent_type.get()
        if not name or not type:
            self._display_message("error")
        else:
            self._account_service.create_account(name, type)
            self._display_message("success")
            self._ent_name.delete(0, END)
            self._ent_type.delete(0, END)

    def _initialize_title_label(self):
        txt_title = "Add new account"
        lbl_title = ttk.Label(master=self._frame, text=txt_title)
        lbl_title.grid(row=0, column=0, columnspan=2,
                       padx=self._padx, pady=self._pady, sticky=constants.W)

    def _initialize_name_label(self):
        txt_name = "Name"
        lbl_name = ttk.Label(master=self._frame, text=txt_name)
        lbl_name.grid(row=1, column=0, padx=self._padx,
                      pady=self._pady, sticky=constants.E)

    def _initialize_name_entry(self):
        self._ent_name = ttk.Entry(master=self._frame)
        self._ent_name.grid(row=1, column=1, padx=self._padx, pady=self._pady)

    def _initialize_type_label(self):
        txt_type = "Type"
        lbl_type = ttk.Label(master=self._frame, text=txt_type)
        lbl_type.grid(row=2, column=0, padx=self._padx,
                      pady=self._pady, sticky=constants.E)

    def _initialize_type_entry(self):
        self._ent_type = ttk.Entry(master=self._frame)
        self._ent_type.grid(row=2, column=1, padx=self._padx, pady=self._pady)

    def _initialize_cancel_button(self):
        txt_cancel = "Cancel"
        btn_cancel = ttk.Button(master=self._frame, text=txt_cancel,
                                command=self._handle_cancel)
        btn_cancel.grid(row=3, column=0, padx=self._padx,
                        pady=self._pady, sticky=constants.EW)

    def _initialize_submit_button(self):
        txt_submit = "Submit"
        btn_submit = ttk.Button(master=self._frame, text=txt_submit,
                                command=self._handle_submit)
        btn_submit.grid(row=3, column=1, padx=self._padx,
                        pady=self._pady, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_title_label()
        self._initialize_name_label()
        self._initialize_name_entry()
        self._initialize_type_label()
        self._initialize_type_entry()
        self._initialize_cancel_button()
        self._initialize_submit_button()

from tkinter import ttk


class AccountView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        txt_title = "Add new account"
        lbl_title = ttk.Label(master=self._frame, text=txt_title)
        lbl_title.grid(row=0, column=0)

        txt_name = "Name"
        lbl_name = ttk.Label(master=self._frame, text=txt_name)
        lbl_name.grid(row=1, column=0)

        ent_name = ttk.Entry(master=self._frame)
        ent_name.grid(row=1, column=1)

        txt_type = "Type"
        lbl_type = ttk.Label(master=self._frame, text=txt_type)
        lbl_type.grid(row=2, column=0)

        ent_type = ttk.Entry(master=self._frame)
        ent_type.grid(row=2, column=1)

        txt_submit = "Submit"
        btn_submit = ttk.Button(master=self._frame, text=txt_submit)
        btn_submit.grid(row=3, column=0)


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

        text = "Add new account"
        label_title = ttk.Label(master=self._frame, text=text)
        label_title.grid(row=0, column=0)

        text = "Name"
        label_name = ttk.Label(master=self._frame, text=text)
        label_name.grid(row=1, column=0)

        entry_name = ttk.Entry(master=self._frame)
        entry_name.grid(row=1, column=1)

        text = "Type"
        label_type = ttk.Label(master=self._frame, text=text)
        label_type.grid(row=2, column=0)

        entry_type = ttk.Entry(master=self._frame)
        entry_type.grid(row=2, column=1)

        text = "Submit"
        button = ttk.Button(master=self._frame, text=text)
        button.grid(row=3, column=0)


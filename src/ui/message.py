from tkinter import ttk

import ui.styles.colors as colors


class Message:

    def __init__(self, frame, var_message):
        self._frame = frame
        self._var_message = var_message
        self._lbl_message = None

    def get_message(self, mode):
        if mode == "missing":
            self._var_message.set("Importing accounts is not supported yet!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "error":
            self._var_message.set("Exporting accounts failed!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "success":
            self._var_message.set("Accounts exported successfully!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.SUCCESS
            )
        return self._lbl_message

from tkinter import ttk

import ui.styles.colors as colors


class Message:

    def __init__(self, frame, var_message):
        self._frame = frame
        self._var_message = var_message

    def get_message(self, mode):
        lbl_message = None
        if mode == "missing":
            self._var_message.set("Importing accounts is not supported yet!")
            lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "error":
            self._var_message.set("Exporting accounts failed!")
            lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "success":
            self._var_message.set("Accounts exported successfully!")
            lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.SUCCESS
            )
        return lbl_message

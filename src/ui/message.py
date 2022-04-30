from tkinter import ttk

import ui.styles.colors as colors


class Message:

    def __init__(self, frame, var_message):
        self._frame = frame
        self._var_message = var_message
        self._lbl_message = None

    def _get_error_message(self, mode):
        if mode == "missing":
            self._var_message.set("Importing accounts is not supported yet!")
        elif mode == "error":
            self._var_message.set("Exporting accounts failed!")

        self._lbl_message = ttk.Label(
            master=self._frame,
            textvariable=self._var_message,
            foreground=colors.ERROR
        )

    def _get_success_message(self, mode):
        if mode == "success":
            self._var_message.set("Accounts exported successfully!")
        
        self._lbl_message = ttk.Label(
            master=self._frame,
            textvariable=self._var_message,
            foreground=colors.SUCCESS
        )

    def get_message(self, mode):
        if mode == "missing" or mode == "error":
            self._get_error_message(mode)
        else:
            self._get_success_message(mode)
        
        return self._lbl_message

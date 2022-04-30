from tkinter import ttk

import ui.styles.colors as colors

error = {
    "e-01": "Exporting accounts failed!",
    "e-02": "Importing accounts is not supported yet!",
    "e-03": "Please enter name!",
    "e-04": "Please enter type!",
    "e-05": "Failed to add a new account!",
    "e-06": "Exporting transactions failed!",
    "e-07": "Importing transactions is not supported yet!",
    "e-08": "Please choose a correct date!",
    "e-09": "Please enter a correct amount!",
    "e-10": "Please enter a category!",
    "e-11": "Please enter a description!",
    "e-12": "Please choose an account!",
    "e-13": "Please enter a sender / receiver!",
}

success = {
    "s-01": "Accounts exported successfully!",
    "s-02": "New account added!",
    "s-03": "Transactions exported successfully!",
    "s-04": "New transaction added!",
}


class Message:

    def __init__(self, frame, var_message):
        self._frame = frame
        self._var_message = var_message
        self._lbl_message = None

    def _get_error_message(self, code):
        content = error[code]
        self._var_message.set(content)

        self._lbl_message = ttk.Label(
            master=self._frame,
            textvariable=self._var_message,
            foreground=colors.ERROR
        )

    def _get_success_message(self, code):
        content = success[code]
        self._var_message.set(content)

        self._lbl_message = ttk.Label(
            master=self._frame,
            textvariable=self._var_message,
            foreground=colors.SUCCESS
        )

    def get_message(self, code):
        if code[0] == "e":
            self._get_error_message(code)
        else:
            self._get_success_message(code)

        return self._lbl_message

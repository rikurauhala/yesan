from tkinter import ttk

import ui.styles.colors as colors

error = {
    "e-01": "Exporting accounts failed!",
    "e-02": "Importing accounts is not supported yet!",
}

success = {
    "s-01": "Accounts exported successfully!",
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

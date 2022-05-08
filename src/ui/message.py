from tkinter import ttk

import ui.styles.colors as colors

error = {
    "e-01": "Exporting accounts failed!",
    "e-02": "Importing accounts failed!",
    "e-03": "Please enter name!",
    "e-04": "Please enter type!",
    "e-05": "Failed to add a new account!",
    "e-06": "Exporting transactions failed!",
    "e-07": "Importing transactions failed!",
    "e-08": "Please choose a correct date!",
    "e-09": "Please enter a correct amount!",
    "e-10": "Please enter a category!",
    "e-11": "Please enter a description!",
    "e-12": "Please choose an account!",
    "e-13": "Please enter a sender / receiver!",
    "e-14": "Saving settings failed!",
    "e-15": "Name should contain at least 3 characters!",
    "e-16": "Name should contain fewer than 50 characters!",
    "e-17": "Type should contain at least 3 characters!",
    "e-18": "Type should contain fewer than 50 characters!",
}

success = {
    "s-01": "Accounts exported successfully!",
    "s-02": "New account added!",
    "s-03": "Transactions exported successfully!",
    "s-04": "New transaction added!",
    "s-05": "Accounts imported successfully!",
    "s-06": "Transactions imported successfully!",
    "s-07": "Settings saved successfully!",
}


class Message:
    """Handles functionality for displaying a message in the user interface."""

    def __init__(self, frame, var_message):
        """Initializes a new instance of the Message class.

        Args:
            frame (Frame): A Frame widget which will be the master of all other widgets.
            var_message (StringVar): A StringVar widget that will contain the message.
        """
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
        """Returns the message corresponding to the code given.

        Args:
            code (String): An error or a success code.

        Returns:
            Label: A Label widget that contains the message in a StringVar widget.
        """
        if code[0] == "e":
            self._get_error_message(code)
        else:
            self._get_success_message(code)

        return self._lbl_message

from tkinter import ttk

import ui.styles.colors as colors

from ui.error import error
from ui.success import success


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

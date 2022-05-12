from tkinter import constants, END, StringVar, ttk

from services.account_service import AccountService

from ui.validator import Validator

from ui.message.message import Message

import ui.styles.styles as styles


class NewAccountView:
    """A view that offers an interface for creating a new account."""

    def __init__(self, root, go_to_account_view):
        """Initializes the view.

        Args:
            root (Tk): The main window.
            go_to_account_view (function): Called to go back to the account view.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._lbl_message = None
        self._var_message = StringVar(self._frame)
        self._message = Message(self._frame, self._var_message)
        self._go_to_account_view = go_to_account_view
        self._ent_name = None
        self._ent_type = None
        self._account_service = AccountService()
        self._validator = Validator()
        self._initialize()

    def pack(self):
        """Displays the view."""
        self._frame.pack(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def destroy(self):
        """Hides the view."""
        self._frame.destroy()

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, code):
        self._lbl_message = self._message.get_message(code)
        self._lbl_message.grid(
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _validate_input(self):
        name_code = self._validator.validate_account_name(
            self._ent_name.get()
        )
        type_code = self._validator.validate_account_type(
            self._ent_type.get()
        )
        valid = True
        if name_code[0] == "e":
            self._display_message(name_code)
            valid = False
        elif type_code[0] == "e":
            self._display_message(type_code)
            valid = False
        return valid

    def _reset_fields(self):
        self._ent_name.delete(0, END)
        self._ent_type.delete(0, END)

    def _handle_submit(self):
        self._clear_message()
        name = self._ent_name.get()
        type = self._ent_type.get()

        if not self._validate_input():
            return

        if self._account_service.create_account(name, type):
            self._display_message("s-02")
            self._reset_fields()
        else:
            self._display_message("e-05")

    def _initialize_title_label(self):
        txt_title = "Add new account"
        lbl_title = ttk.Label(
            master=self._frame,
            text=txt_title
        )
        lbl_title.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

    def _initialize_name_label(self):
        txt_name = "Name"
        lbl_name = ttk.Label(
            master=self._frame,
            text=txt_name
        )
        lbl_name.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_name_entry(self):
        self._ent_name = ttk.Entry(master=self._frame)
        self._ent_name.grid(
            row=1,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_type_label(self):
        txt_type = "Type"
        lbl_type = ttk.Label(
            master=self._frame,
            text=txt_type
        )
        lbl_type.grid(
            row=2,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_type_entry(self):
        self._ent_type = ttk.Entry(master=self._frame)
        self._ent_type.grid(
            row=2,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_back_button(self):
        txt_back = "« Back"
        btn_back = ttk.Button(
            master=self._frame,
            text=txt_back,
            command=self._go_to_account_view
        )
        btn_back.grid(
            row=3,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_submit_button(self):
        txt_submit = "✔ Submit"
        btn_submit = ttk.Button(
            master=self._frame,
            text=txt_submit,
            command=self._handle_submit
        )
        btn_submit.grid(
            row=3,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_name_label()
        self._initialize_name_entry()
        self._initialize_type_label()
        self._initialize_type_entry()
        self._initialize_back_button()
        self._initialize_submit_button()

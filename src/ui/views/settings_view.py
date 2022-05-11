from tkinter import constants, StringVar, Text, ttk

from services.settings_service import settings_service

from ui.message.message import Message

import ui.styles.colors as colors
import ui.styles.fonts as fonts
import ui.styles.styles as styles


class SettingsView:
    """A view that allows the user to see and edit the settings (config) file."""

    def __init__(self, root, go_to_main_view):
        """Initializes the view.

        Args:
            root (Tk): The main window.
            go_to_main_view (function): Called to go back to the main view.
        """
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._buttons = ttk.Frame(master=self._frame)
        self._var_message = StringVar(self._frame)
        self._message = Message(self._frame, self._var_message)
        self._lbl_message = None
        self._text = None
        self._go_to_main_view = go_to_main_view
        self._settings_service = settings_service
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
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_title_label(self):
        txt_title = "Settings"
        lbl_title = ttk.Label(
            master=self._frame,
            text=txt_title,
            font=fonts.TITLE
        )
        lbl_title.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.W
        )

    def _initialize_text_field_content(self, default=False):
        self._text.delete("1.0", constants.END)
        self._text.tag_configure("comment", foreground=colors.COMMENT)
        no = 0
        lines = self._settings_service.import_settings(default)
        for line in lines:
            no = no + 1
            self._text.insert(constants.END, line)
            if line[0] == "#":
                self._text.tag_add("comment", f"{no}.0", f"{no}.{len(line)}")

    def _initialize_text_field(self):
        self._text = Text(
            master=self._frame,
            height=20,
            width=60
        )
        self._text.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING
        )
        self._initialize_text_field_content()

    def _initialize_back_button(self):
        txt_back = "« Back"
        btn_back = ttk.Button(
            master=self._buttons,
            text=txt_back,
            command=self._go_to_main_view
        )
        btn_back.grid(
            row=0,
            column=0,
            padx=styles.PADDING_RIGHT
        )

    def _handle_save(self):
        self._clear_message()
        content = self._text.get(1.0, constants.END)
        success = self._settings_service.export_settings(content)
        if success:
            self._display_message("s-07")
        else:
            self._display_message("e-14")

    def _initialize_save_button(self):
        txt_save = "✔ Save"
        btn_save = ttk.Button(
            master=self._buttons,
            text=txt_save,
            command=self._handle_save
        )
        btn_save.grid(
            row=0,
            column=1,
            padx=styles.PADDING_RIGHT
        )

    def _handle_reset(self):
        self._clear_message()
        self._initialize_text_field_content(default=True)
        self._display_message("s-08")

    def _initialize_reset_button(self):
        txt_reset = "↺ Reset"
        btn_reset = ttk.Button(
            master=self._buttons,
            text=txt_reset,
            command=self._handle_reset
        )
        btn_reset.grid(
            row=0,
            column=2,
            padx=styles.PADDING_RIGHT
        )

    def _initialize_buttons(self):
        self._initialize_back_button()
        self._initialize_save_button()
        self._initialize_reset_button()
        self._buttons.grid(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN,
            sticky=constants.W
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_text_field()
        self._initialize_buttons()

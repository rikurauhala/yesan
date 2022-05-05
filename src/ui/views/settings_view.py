from tkinter import constants, StringVar, Text, ttk

from ui.message import Message

from services.settings_service import settings_service

import ui.styles.fonts as fonts
import ui.styles.styles as styles


class SettingsView:
    def __init__(self, root, go_to_main_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._buttons = ttk.Frame(master=self._frame)
        self._var_message = StringVar(self._frame)
        self._message = Message(self._frame, self._var_message)
        self._lbl_message = None
        self._txt_text = None
        self._go_to_main_view = go_to_main_view
        self._settings_service = settings_service
        self._initialize()

    def pack(self):
        self._frame.pack(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def destroy(self):
        self._frame.destroy()

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

    def _initialize_text_field_content(self):
        lines = self._settings_service.import_settings()
        for line in lines:
            self._txt_text.insert(constants.END, line)

    def _initialize_text_field(self):
        self._txt_text = Text(
            master=self._frame,
            height=15,
            width=50,
        )
        self._txt_text.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
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

    def _handle_submit(self):
        content = self._txt_text.get(1.0, constants.END)
        self._settings_service.export_settings(content)

    def _initialize_submit_button(self):
        txt_submit = "✔ Submit"
        btn_submit = ttk.Button(
            master=self._buttons,
            text=txt_submit,
            command=self._handle_submit
        )
        btn_submit.grid(
            row=0,
            column=1,
            padx=styles.PADDING_RIGHT
        )

    def _initialize_buttons(self):
        self._initialize_back_button()
        self._initialize_submit_button()
        self._buttons.grid(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN,
            sticky=constants.W
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_text_field()
        self._initialize_buttons()

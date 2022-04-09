from tkinter import constants, END, StringVar, ttk

from services.account_service import AccountService
import ui.styles.colors as colors
import ui.styles.styles as styles


class NewTransactionView:
    def __init__(self, root, go_to_main_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._go_to_main_view = go_to_main_view
        self._ent_amount = None
        self._ent_category = None
        self._ent_description = None
        self._ent_account_id = None
        self._ent_party = None
        self._var_message = None
        self._lbl_message = None
        self._account_service = AccountService()
        self._initialize()

    def pack(self):
        self._frame.pack(
            padx=styles.PADDING_MAIN,
            pady=styles.PADDING_MAIN
        )

    def destroy(self):
        self._frame.destroy()

    def _clear_message(self):
        if self._lbl_message:
            self._lbl_message.destroy()

    def _display_message(self, mode):
        self._var_message = StringVar(self._frame)
        if mode == "error":
            self._var_message.set("Please enter every detail!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.ERROR
            )
        if mode == "success":
            self._var_message.set("New transaction added!")
            self._lbl_message = ttk.Label(
                master=self._frame,
                textvariable=self._var_message,
                foreground=colors.SUCCESS
            )
        self._lbl_message.grid(
            columnspan=2,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _handle_submit(self):
        self._clear_message()

    def _initialize_title_label(self):
        txt_title = "Add new transaction"
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
            sticky=constants.W)

    def _initialize_amount_label(self):
        txt_amount = "Amount"
        lbl_amount = ttk.Label(
            master=self._frame,
            text=txt_amount
        )
        lbl_amount.grid(
            row=1,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_amount_entry(self):
        self._ent_amount = ttk.Entry(master=self._frame)
        self._ent_amount.grid(
            row=1,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_category_label(self):
        txt_category = "Category"
        lbl_category = ttk.Label(
            master=self._frame,
            text=txt_category
        )
        lbl_category.grid(
            row=2,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_category_entry(self):
        self._ent_category = ttk.Entry(master=self._frame)
        self._ent_category.grid(
            row=2,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_description_label(self):
        txt_description = "Description"
        lbl_description = ttk.Label(
            master=self._frame,
            text=txt_description
        )
        lbl_description.grid(
            row=3,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_description_entry(self):
        self._ent_description = ttk.Entry(master=self._frame)
        self._ent_description.grid(
            row=3,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_account_label(self):
        txt_account = "Account"
        lbl_description = ttk.Label(
            master=self._frame,
            text=txt_account
        )
        lbl_description.grid(
            row=4,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_account_entry(self):
        self._ent_account = ttk.Entry(master=self._frame)
        self._ent_account.grid(
            row=4,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_party_label(self):
        txt_party = "Payer / Receiver"
        lbl_party = ttk.Label(
            master=self._frame,
            text=txt_party
        )
        lbl_party.grid(
            row=5,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.E
        )

    def _initialize_party_entry(self):
        self._ent_party = ttk.Entry(master=self._frame)
        self._ent_party.grid(
            row=5,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING
        )

    def _initialize_back_button(self):
        txt_back = "Back"
        btn_back = ttk.Button(
            master=self._frame,
            text=txt_back,
            command=self._go_to_main_view
        )
        btn_back.grid(
            row=6,
            column=0,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize_submit_button(self):
        txt_submit = "Submit"
        btn_submit = ttk.Button(
            master=self._frame,
            text=txt_submit,
            command=self._handle_submit
        )
        btn_submit.grid(
            row=6,
            column=1,
            padx=styles.PADDING,
            pady=styles.PADDING,
            sticky=constants.EW
        )

    def _initialize(self):
        self._initialize_title_label()
        self._initialize_amount_label()
        self._initialize_amount_entry()
        self._initialize_category_label()
        self._initialize_category_entry()
        self._initialize_description_label()
        self._initialize_description_entry()
        self._initialize_account_label()
        self._initialize_account_entry()
        self._initialize_party_label()
        self._initialize_party_entry()
        self._initialize_back_button()
        self._initialize_submit_button()

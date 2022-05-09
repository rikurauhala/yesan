import re


class Validator:
    """Validates user input."""

    def __init__(self):
        """Creates a new instance of Validator."""

    def validate_account_name(self, name):
        """Validates the contents of the name field in NewAccountView.

        Args:
            name (String): Account name.

        Returns:
            String: Status code.
        """
        length = len(name)
        if not name:
            return "e-03"
        if length < 3:
            return "e-15"
        if length > 50:
            return "e-16"
        return "ok"

    def validate_account_type(self, type):
        """Validates the contents of the type field in NewAccountView.

        Args:
            type (String): Account type.

        Returns:
            String: Status code.
        """
        length = len(type)
        if not type:
            return "e-04"
        if length < 3:
            return "e-17"
        if length > 50:
            return "e-18"
        return "ok"

    def validate_transaction_date(self, date):
        """Validates the contents of the date field in NewTransactionView.

        Args:
            date (String): Expects a date in the YYYY-MM-DD format.

        Returns:
            String: Status code.
        """
        if not date:
            return "e-08"
        return "ok"

    def validate_transaction_amount(self, amount):
        """Validates the contents of the amount field in NewTransactionView.

        Args:
            amount (String): Expects an amount with a dot as the decimal separator.

        Returns:
            String: Status code.
        """
        pattern = r"^-?(?=\d)\d*(?:\.\d{1,2})?$"
        if not amount:
            return "e-09"
        if not re.match(pattern, amount):
            return "e-19"
        return "ok"

    def validate_transaction_category(self, category):
        """Validates the contents of the category field in NewTransactionView.

        Args:
            category (String): Category of the transaction.

        Returns:
            String: Status code.
        """
        length = len(category)
        if not category:
            return "e-10"
        if length < 3:
            return "e-20"
        if length > 50:
            return "e-21"
        return "ok"

    def validate_transaction_description(self, description):
        """Validates the contents of the description field in NewTransactionView.

        Args:
            description (String): Description of the transaction.

        Returns:
            String: Status code.
        """
        length = len(description)
        if not description:
            return "e-11"
        if length < 3:
            return "e-22"
        if length > 100:
            return "e-23"
        return "ok"

    def validate_transaction_account_name(self, account_name):
        """Validates the contents of the account field in NewTransactionView.

        Args:
            account_name (String): Name of the account to be associated with the transaction.

        Returns:
            String: Status code.
        """
        if not account_name:
            return "e-12"
        return "ok"

    def validate_transaction_party(self, party):
        """Validates the contents of the party field in NewTransactionView.

        Args:
            party (String): Payer / receiver.

        Returns:
            String: Status code.
        """
        length = len(party)
        if not party:
            return "e-13"
        if length < 3:
            return "e-24"
        if length > 50:
            return "e-25"
        return "ok"

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
        if not date:
            return "e-08"
        return "ok"

    def validate_transaction_amount(self, amount):
        if not amount:
            return "e-09"
        return "ok"

    def validate_transaction_category(self, category):
        if not category:
            return "e-10"
        return "ok"

    def validate_transaction_description(self, description):
        if not description:
            return "e-11"
        return "ok"

    def validate_transaction_account_name(self, account_name):
        if not account_name:
            return "e-12"
        return "ok"

    def validate_transaction_party(self, party):
        if not party:
            return "e-13"
        return "ok"

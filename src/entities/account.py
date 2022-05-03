class Account:
    """Account object, stores properties of an account.

    Attributes:
        id: String, unique identifier of an account in the UUID format.
        name: String, name of an account.
        type: String, type of an account.
    """

    def __init__(self, account_id, account_name, account_type):
        """Initializes a new instance of an Account object.

        Args:
            account_id (String): Unique identifier of an account in the UUID format.
            account_name (String): Name of an account.
            account_type (String): Type of an account.
        """

        self.id = account_id
        self.name = account_name
        self.type = account_type

class Transaction:
    """Transaction object, stores properties of a transaction.

    Attributes:
        id: String, unique identifier of a transaction in the UUID format.
        date: Timestamp, date when the transaction was made. 
        amount: Integer, amount of money involved in the transaction.
        category: String, category to which the transaction belongs to.
        description: String, describes the purpose of the transaction.
        account_id: String, connects the transaction to an account.
        party: String, specifies the other party (payer/receiver) of the transaction.
    """

    def __init__(self, transaction_id, date, amount, category, description, account_id, party):
        """Initializes a new instance of a Transaction object.

        Args:
            transaction_id (String): Unique identifier of a transaction in the UUID format.
            date (Timestamp): Date when the transaction was made. 
            amount (Integer): Amount of money involved in the transaction.
            category (String): String, category to which the transaction belongs to.
            description (String): Describes the purpose of the transaction.
            account_id (String): Connects the transaction to an account.
            party (String): Specifies the other party (payer/receiver) of the transaction.
        """

        self.id = transaction_id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.account_id = account_id
        self.party = party

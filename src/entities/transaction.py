class Transaction:

    def __init__(self, transaction_id, date, amount, category, description, account_id, party):
        self.id = transaction_id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.account_id = account_id
        self.party = party

class Transaction:

    def __init__(self, id, timestamp, amount, category, description, account_id, party):
        self.id = id
        self.timestamp = timestamp
        self.amount = amount
        self.category = category
        self.description = description
        self.account_id = account_id
        self.party = party

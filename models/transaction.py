from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, user, transaction_amount):
        self.transaction_type = transaction_type
        self.user = user
        self.created_on = datetime.now()
        self.transaction_amount = transaction_amount

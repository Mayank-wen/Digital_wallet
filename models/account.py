from datetime import datetime

from models.user import User


class Account:
    def __init__(self, name, amount):
        self.user = User(name)
        self.amount = amount
        self.created_on = datetime.now()
        self.transactions = []
        self.transactions_count = 0
        self.fixed_deposit = False
        self.fixed_deposit_amount = 0
        self.fixed_deposit_start_trans_count = 0

    @staticmethod
    def comparator(a, b):
        if a.transactions_count == b.transactions_count:
            if a.amount == b.amount:
                if a.created_on < b.created_on:
                    return 1
                else:
                    return -1
            elif a.amount > b.amount:
                return 1
            else:
                return -1
        elif a.transactions_count > b.transactions_count:
            return 1
        else:
            return -1

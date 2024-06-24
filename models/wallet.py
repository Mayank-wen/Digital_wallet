import logging
from functools import cmp_to_key

from models.account import Account
from utils.constants import MINIMUM_BAL, TRANSACTION_TYPES, OFFER1_REWARD, OFFER2_REWARDS
from models.transaction import Transaction

logging.basicConfig(filename='logs/app.log', filemode='a', format='%(asctime)s - %(message)s')


class Wallet:
    def __init__(self):
        self.accounts = []

    def create_wallet(self, name, amount):
        account = Account(name, amount)
        self.accounts.append(account)

    @staticmethod
    def check_fixed_deposit(account, amount):
        if account.fixed_deposit:
            if account.amount - amount < account.fixed_deposit_amount:
                account.fixed_deposit = False
                account.fixed_deposit_amount = 0
                account.fixed_deposit_start_trans_count = 0
            else:
                account.fixed_deposit_start_trans_count += 1
        if account.fixed_deposit and account.fixed_deposit_start_trans_count//5 > 0:
            account.amount += 10
            transaction = Transaction(TRANSACTION_TYPES[0], "FD", 10)
            account.transactions.append(transaction)

    def transfer_money(self, sender, receiver, amount):
        sender_acc, receiver_acc = None, None
        for account in self.accounts:
            if account.user.name == sender:
                sender_acc = account
            elif account.user.name == receiver:
                receiver_acc = account
        if not sender_acc or not receiver_acc:
            logging.error("Either Sender or Receiver Account Not found!")
        elif sender_acc.amount - amount >= MINIMUM_BAL:
            self.check_fixed_deposit(sender_acc, amount)
            self.check_fixed_deposit(receiver_acc, amount)
            transaction = Transaction(TRANSACTION_TYPES[0], sender_acc.user.name, amount)
            receiver_acc.transactions.append(transaction)
            transaction = Transaction(TRANSACTION_TYPES[1], receiver_acc.user.name, amount)
            sender_acc.transactions.append(transaction)
            sender_acc.amount -= amount
            receiver_acc.amount += amount
            sender_acc.transactions_count += 1
            receiver_acc.transactions_count += 1
            if sender_acc.amount == receiver_acc.amount:
                self.__offer1(sender_acc, receiver_acc)
        else:
            logging.error("Account Balance is not sufficient for transaction!")

    def statement(self, name):
        user_account = None
        for account in self.accounts:
            if account.user.name == name:
                user_account = account

                break

        for transaction in user_account.transactions:
            print("{} {} {}".format(transaction.user, transaction.transaction_type, transaction.transaction_amount))
            # Bonus part
            # print("{} {} {} {}".format(transaction.user, transaction.transaction_type, transaction.transaction_amount, user_account.fixed_deposit_amount))

    def overview(self):
        for account in self.accounts:
            print("{} {}".format(account.user.name, account.amount))
            # Bonus Part
            # print("{} {} {}".format(account.user.name, account.amount, account.fixed_deposit_amount))

    @staticmethod
    def __offer1(sender_acc, receiver_acc, amount=OFFER1_REWARD):
        transaction = Transaction(TRANSACTION_TYPES[0], TRANSACTION_TYPES[2], amount)
        receiver_acc.transactions.append(transaction)
        transaction = Transaction(TRANSACTION_TYPES[0], TRANSACTION_TYPES[2], amount)
        sender_acc.transactions.append(transaction)
        sender_acc.amount += amount
        receiver_acc.amount += amount

    def offer2(self, reward_users=3):
        accounts = sorted(self.accounts, key=cmp_to_key(Account.comparator), reverse=True)
        for index, acc in enumerate(accounts[: reward_users]):
            transaction = Transaction(TRANSACTION_TYPES[3], acc.user.name, OFFER2_REWARDS[index])
            acc.transactions.append(transaction)
            acc.amount += OFFER2_REWARDS[index]

    def fixed_deposit(self, name, amount):
        customer_account = None
        for account in self.accounts:
            if account.user.name == name:
                customer_account = account
                break
        if amount <= customer_account.amount:
            customer_account.fixed_deposit = True
            customer_account.fixed_deposit_amount = amount
        else:
            logging.error("Customer account balance is less than fixed_deposit amount")
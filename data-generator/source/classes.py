
from collections import OrderedDict
from datetime import datetime

import numpy as np
from faker import Faker
import pandas as pd


class Transaction:
    def __init__(self) -> None:
        self.Id: int = None
        self.Amount: int = None
        self.Date: str = None
        self.Description: str = None
        self.Type: str = None
        self.Category: str = None
        self.AccountId: int = None
        self.Tags: str = None
        self.Notes: str = None
        self.IsReconciled: bool = False
        self.IsCleared: bool = False

    def set_id(self, id: int) -> None:
        self.Id = id

    def set_amount(self, amount: int) -> None:
        self.Amount = amount

    def set_date(self, date: datetime) -> None:
        self.Date = date.strftime("%Y-%m-%d")

    def set_description(self, description: str) -> None:
        self.Description = description

    def set_type(self, type: str) -> None:
        self.Type = type

    def set_category(self, category: str) -> None:
        self.Category = category

    def set_accountId(self, accountId: int) -> None:
        self.AccountId = accountId

    def set_tags(self, tags: str) -> None:
        self.Tags = tags

    def set_notes(self, notes: str) -> None:
        self.Notes = notes

    def set_is_reconciled(self, is_reconciled: bool) -> None:
        self.IsReconciled = is_reconciled

    def set_is_cleared(self, is_cleared: bool) -> None:
        self.IsCleared = is_cleared

    @staticmethod
    def calculate_transaction_total(transactions: OrderedDict) -> int:
        total = 0
        total += sum([x["Amount"] for x in transactions])
        return total


class Person:
    def __init__(self) -> None:
        self.Id: int = None
        self.LastName: str = None
        self.FirstName: str = None
        self.Phone: str = None
        self.Email: str = None
        
        self.Accounts: list = []

    def get_full_name(self) -> str:
        return self.FirstName + " " + self.LastName


class Account:
    def __init__(self) -> None:
        self.Id: int = None
        self.PersonId: int = None
        self.Provider: str = None
        self.CardNumber: str = None
        self.CardType: str = None
        self.CreditCap: int = None
        self.StartingBalance: int = None
        self.CurrentBalance: int = None
        
        self.Transactions: list = []


class Generactor:
    def __init__(self) -> None:
        self.IdTracker: int = 1
        self.AccountIdTracker: int = 1
        self.PersonIdTracker: int = 1

        locales = OrderedDict([
            ('en-US', 1),
        ])

        self.faker = Faker(locales)
        
    def generate_data(self, count: int) -> list:
        people = []
        for _ in range(count):
            people.append(self.generate_person().__dict__)
        return people

    def generate_person(self) -> Person:
        person = Person()
        person.Id = self.PersonIdTracker
        self.PersonIdTracker += 1

        person.LastName = self.faker.last_name()
        person.FirstName = self.faker.first_name()
        person.Phone = self.faker.phone_number()
        person.Email = self.faker.email()

        for (i, _) in enumerate(range(self.faker.random_int(min=1, max=5))):
            person.Accounts.append(self.generate_account(person.Id).__dict__)

        return person

    def generate_transaction(self, account: Account) -> Transaction:
        transaction = Transaction()
        transaction.set_id(self.IdTracker)
        transaction.set_accountId(account.Id)
        self.IdTracker += 1

        transaction.set_amount(self.generate_amount())
        transaction.set_date(self.generate_date())
        transaction.set_description(self.generate_description())
        transaction.set_notes(self.generate_description())
        transaction.set_type(self.generate_type())
        transaction.set_category(self.generate_category())
        transaction.set_tags(self.generate_description())
        transaction.set_is_reconciled(self.faker.random_int(min=0, max=1) == 1)
        transaction.set_is_cleared(self.faker.random_int(min=0, max=1) == 1)

        return transaction


    def generate_category(self):
        return self.faker.random_element(
            elements=['food', 'transport', 'entertainment', 'other', 'transfer', 'income'])

    def generate_type(self):
        return self.faker.random_element(elements=['credit', 'debit'])

    def generate_description(self):
        return self.faker.sentence()

    def generate_date(self):
        return self.faker.date_time_this_year()

    def generate_amount(self):
        amount = self.faker.random_int(min=1, max=500)

        return amount if np.random.randint(0, 4) == 0 or 1 or 2 else -amount

    def generate_account(self, personId: int) -> Account:
        account = Account()
        account.Id: int = self.AccountIdTracker
        self.AccountIdTracker += 1
        account.PersonId: int = personId

        account.Provider = self.faker.credit_card_provider()
        # TODO: add more type
        account.CardType = self.faker.random_element(elements=['debit'])
        account.CardNumber = self.faker.credit_card_number()

        account.StartingBalance = self.faker.random_int(min=0, max=10000)

        account.Transactions = self.generate_multiple_transaction(
            account, self.faker.random_int(min=1, max=15))

        account.CurrentBalance = account.StartingBalance + \
            Transaction.calculate_transaction_total(account.Transactions)
        return account

    def generate_multiple_transaction(self, account: Account, count: int) -> OrderedDict:
        transactions = []
        for i in range(count):
            transactions.append(self.generate_transaction(account).__dict__)
        return transactions


# test = Generactor()

# df = pd.DataFrame(columns=['id', 'personId', 'provider', 'card_number',
#                   'card_type', 'credit_cap', 'starting_balance', 'current_balance'])
# print(df)

# dict = test.generate_account(1).__dict__
# tett = dict.pop('transactions')

# print(pd.DataFrame(dict, index=[0]))

# print(test.generate_person().__dict__)

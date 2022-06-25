
from collections import OrderedDict, namedtuple
import json
from faker import Faker
import os
import requests

AMOUNT_OF_PERSON = 50
API_ROUTE = 'https://localhost:44389/api/DataGenerator/ImportJsonData'
API_ROUTE_FOR_ID = 'https://localhost:44389/api/DataGenerator/GetNextId'

person_id_tracker = 1
account_id_tracker = 1
transaction_id_tracker = 1


class Transaction:
    def __init__(self, account_id, faker: Faker) -> None:
        self.Id: int = self.init_id()
        self.Date: str = faker.date_time_this_year().strftime('%Y-%m-%d')
        self.Description: str = faker.sentence(
            nb_words=6, variable_nb_words=True, ext_word_list=None)
        self.Category: str = faker.random_element(
            elements=['food', 'transport', 'entertainment', 'other', 'income'])
        self.Amount: int = self.init_amount(faker)
        self.AccountId: int = account_id
        self.Tags: str = faker.sentence(
            nb_words=6, variable_nb_words=True, ext_word_list=None)
        self.Notes: str = faker.sentence(
            nb_words=6, variable_nb_words=True, ext_word_list=None)
        self.IsReconciled: bool = faker.boolean()
        self.IsCleared: bool = faker.boolean()

    def init_id(self) -> int:
        global transaction_id_tracker
        transaction_id_tracker = transaction_id_tracker + 1
        return transaction_id_tracker

    def init_amount(self, faker: Faker) -> None:
        amount = faker.random_int(min=0, max=1000)
        return amount * 6 if self.Category == 'income' else -amount

    @staticmethod
    def calculate_transaction_total(transactions: list) -> int:
        total = 0
        total += sum([x["Amount"] for x in transactions])
        return total


class Account:
    def __init__(self, person_id, faker: Faker) -> None:
        self.Id: int = self.init_id()
        self.PersonId: int = person_id
        self.Provider: str = faker.credit_card_provider()
        self.CardNumber: str = faker.credit_card_number()
        self.AccountType: str = faker.random_element(elements=['debit'])
        self.StartingBalance: int = faker.random_int(min=0, max=10000)
        self.Balance: int = self.StartingBalance

        self.Transactions: list = []

    def init_id(self) -> int:
        global account_id_tracker
        account_id_tracker = account_id_tracker + 1
        return account_id_tracker

    def add_transaction(self, transaction: Transaction) -> None:
        self.Transactions.append(transaction.__dict__)


class Person:
    def __init__(self, faker: Faker) -> None:
        self.Id: int = self.init_id()
        self.FirstName: str = faker.first_name()
        self.LastName: str = faker.last_name()
        self.Email: str = faker.email()
        self.Phone: str = faker.phone_number()
        self.BirthDate: str = faker.date_of_birth().strftime("%Y-%m-%d")
        self.Address: str = faker.address()
        self.City: str = faker.city()
        self.State: str = faker.state()
        self.Zip: str = faker.zipcode()
        self.Country: str = faker.country()
        self.Company: str = faker.company()
        self.JobTitle: str = faker.job()
        self.CompanyDescription: str = faker.text()
        self.CompanyDomain: str = faker.domain_name()

        self.Accounts: list = []

    def init_id(self) -> int:
        global person_id_tracker
        person_id_tracker = person_id_tracker + 1
        return person_id_tracker

    def get_full_name(self) -> str:
        return self.FirstName + " " + self.LastName

    def add_account(self, account: Account) -> None:
        self.Accounts.append(account.__dict__)


class Generactor:
    def __init__(self) -> None:

        locales = OrderedDict([
            ('en-US', 1),
        ])

        self.faker = Faker(locales)

    def generate_data(self, count: int) -> list:
        people = []
        for _ in range(count):
            person = self.generate_person()
            for _ in range(self.faker.random_int(min=1, max=5)):
                account = self.generate_account(person)
                for _ in range(self.faker.random_int(min=1, max=20),):
                    transaction = self.generate_transaction(account)
                    account.add_transaction(transaction)
                account.Balance += Transaction.calculate_transaction_total(
                    account.Transactions)
                person.add_account(account)
            people.append(person.__dict__)
        return people

    def generate_person(self) -> Person:
        return Person(self.faker)

    def generate_account(self, person: Person) -> Account:
        return Account(person.Id, self.faker)

    def generate_transaction(self, account: Account) -> Transaction:
        return Transaction(account.Id, self.faker)

def repair_json(person_dict: dict) -> None:
    with open('data.json', 'w') as f:
        f.write(json.dumps([x for x in person_dict], separators=(',', ':'), ))
    with open('data.json', 'r') as f:
        return f.read()

def main():

    response = json.decoder.JSONDecoder().decode(requests.get(API_ROUTE_FOR_ID, verify=False).content.decode('utf-8'))
    print("response: ", response)
    global person_id_tracker
    global account_id_tracker
    global transaction_id_tracker
    
    person_id_tracker = response["personId"]
    account_id_tracker = response["accountId"]
    transaction_id_tracker = response["transactionId"]
    
    print("person_id_tracker: ", person_id_tracker)
    print("account_id_tracker: ", account_id_tracker)
    print("transaction_id_tracker: ", transaction_id_tracker)

    person_dict: dict = Generactor().generate_data(AMOUNT_OF_PERSON)

    json_string = repair_json(person_dict)
        
    os.remove('data.json')
        
    requests.post(API_ROUTE, data=json_string, verify=False , headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    main()
#account == Wallet

from dataclasses import dataclass, field
from enum import Enum
import hashlib
import sys
from typing import Optional

accounts : list = []

@staticmethod
def hash_password(password: str):
    return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()


class walletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'

@dataclass
class BankAccount:
    name : str
    surname : str
    wallet : float = field(init=False, default=500.0)
    password : str


    def set_password(self, password: str):
        self.password = hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()
    
    def check_password(self, password: str) -> bool:
        return self.password == hash_password(password)
    
    def addToBankAccount(name:str, surname:str, cash:float):
        BankAccount.wallet=BankAccount.wallet + cash
        print(f'Net Available Balance {BankAccount.wallet}')
    
    def substractFromBankAccount(name:str, surname:str, cash:float):
        BankAccount.wallet = BankAccount.wallet - cash
        print(f'Net Available Balance {BankAccount.wallet}')

    def moneyConversion():
        ...
    
    def toString(name:str, surname:str, password:str):
        account = BankAccount(name=name, surname=surname, password=password)
        print(account)
        
    def deconstructor(name:str):
        del BankAccount.name







def create_account(name: str, surname : str, password: str) -> BankAccount:
    account = BankAccount(name=name, surname=surname, password=password)
    account.set_password(password=password)
    accounts.append(account)
    print(password)
    
    return 'Done!'

def get_account(name: str, surname : str, password: str) -> Optional[BankAccount]:
    account = next((u for u in accounts if name == u.name and surname == u.surname and u.check_password(password)), None)

    if not account:
        print('User not found')
        return

    print('You sign-in!')
    print("""
Choose your actions:
1. Add money to account
2. Substract money from account
3. Money Conversion
4. Get account information
5. Delete account
0. Exit
""")
    command = input('')
    if(command=='1'):
        print('How many cash do you want to add:')
        cash = input()
        BankAccount.addToBankAccount(name=name, surname=surname, cash=int(cash))
    elif(command=='2'):
        print('How many cash do you want substract:')
        cash = input()
        BankAccount.substractFromBankAccount(name=name, surname=surname, cash=int(cash))
    elif(command=='3'):
        print('Sorry, I dont understand this topic')
    elif(command=='4'):
        BankAccount.toString(name=name, surname=surname, password=password)
    elif(command=='5'):
        BankAccount.deconstructor(name=name)
        print('account destroyed')
    else:
        print('Invalid command')




while (True):
        print("""Choose your actions:
1. Create a account
2. Select a account
0. Exit""")
        command = input('')
        if(command=='1'):
            name, surname, password = input('Create account: ').split(' ')
            bankaccount = create_account(name=name, surname=surname, password=password)
            print(bankaccount)
        elif(command=='2'):
            name, surname, password = input('Enter your creds: ').split(' ')
            print(get_account(name=name, surname=surname, password=password))

        elif(command=='0'):
            sys.exit(0)
        else:
            print('invalid command')


        
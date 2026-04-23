class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount

    def take_money(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        self.min_balance = min_balance
        super().__init__(balance)
    
    def take_money(self, amount):
        try:
            if ((self.balance - amount) > self.min_balance):
                self.balance -= amount
            else:
                raise ValueError('Transferencia denegada, no hay suficiente dinero en la cuenta!')

        except Exception as error:
            print(f'An error occurred on take_money(): {error}')

new_account = SavingsAccount(1000, 100)
print(f'Current balance: {new_account.balance}')

new_account.add_money(1000)
print(f'Current balance: {new_account.balance}')
new_account.take_money(1500)
print(f'Current balance: {new_account.balance}')
new_account.take_money(3000)
print(f'Current balance: {new_account.balance}')
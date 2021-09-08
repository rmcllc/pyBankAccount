class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, deposit_amount):
        self.account_balance += deposit_amount
        print(
            f"Hello, {self.name} Deposit Amount: {deposit_amount} Available Balance: {self.account_balance}")
        return self

    def make_withdrawal(self, withdrawal_amount):
        self.account_balance -= withdrawal_amount
        print(
            f"Hello, {self.name} Withdrawal Amount: {withdrawal_amount} Available Balance: {self.account_balance}")
        return self

    def display_user_balance(self):
        print(
            f"Hello, {self.name}. Your available balance: {self.account_balance}")
        return self

    def make_transfer(self, amount, name):
        self.make_withdrawal(amount)
        name.make_deposit(amount)
        return self


michael = User('michael', 'mike@email.com')
robin = User('robin', 'robin.email.com')
peter = User('peter', 'peter@email.com')


michael.make_deposit(50).make_deposit(
    50).make_deposit(250).make_withdrawal(100)

robin.make_deposit(200).make_deposit(50).make_withdrawal(
    200).make_withdrawal(100).display_user_balance()

peter.make_deposit(5000) .make_withdrawal(
    2) .make_withdrawal(500) .make_withdrawal(2000)
peter.display_user_balance()

peter.make_transfer(300, robin)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, deposit_amount):
        self.account_balance += deposit_amount
        return (f"Hello, {self.name} Deposit Amount: {deposit_amount} Available Balance: {self.account_balance}")

    def make_withdrawal(self, withdrawal_amount):
        self.account_balance -= withdrawal_amount
        return (f"Hello, {self.name} Withdrawal Amount: {withdrawal_amount} Available Balance: {self.account_balance}")

    def display_user_balance(self):
        return (f"Hello, {self.name}. Your available balance: {self.account_balance}")

    def make_transfer(self, amount, name):
        self.make_withdrawal(amount)
        name.make_deposit(amount)
        return(self.display_user_balance(), name.display_user_balance(), amount)


michael = User('michael', 'mike@email.com')
robin = User('robin', 'robin.email.com')
peter = User('peter', 'peter@email.com')


print(michael.make_deposit(50))
print(michael.make_deposit(50))
print(michael.make_deposit(250))
print(michael.make_withdrawal(100))

robin.make_deposit(200)
robin.make_deposit(50)
robin.make_withdrawal(200)
robin.make_withdrawal(100)
# print(robin.display_user_balance())

peter.make_deposit(5000)
peter.make_withdrawal(2)
peter.make_withdrawal(500)
peter.make_withdrawal(2000)
# print(peter.display_user_balance())

print(peter.make_transfer(300, robin))

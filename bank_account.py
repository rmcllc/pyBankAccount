class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Your deposit of {amount} was successful! Your new balance is {self.balance}")
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        print(
            f"Your withdrawal of {amount} was successful! Your new balance is {self.balance}")
        return self

    def display_account_info(self):
        print(
            f"Your acount balance is {self.balance}. Your interest rate is {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self


mike = BankAccount('mike', 0.02, 2000)
mary = BankAccount('mary', 0.05, 100)

mike.yield_interest()
print(mike.balance)

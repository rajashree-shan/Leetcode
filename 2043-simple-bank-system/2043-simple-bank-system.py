class Bank:

    def __init__(self, balance: list[int]):
        # store balances
        self.balance = balance
        self.n = len(balance)

    def valid(self, account: int) -> bool:
        return 1 <= account <= self.n

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid(account) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # both accounts valid and enough money in account1
        if (not self.valid(account1) or
            not self.valid(account2) or
            self.balance[account1 - 1] < money):
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

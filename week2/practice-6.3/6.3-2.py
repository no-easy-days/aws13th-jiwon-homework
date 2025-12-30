class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        if self.balance > balance:
            self.balance -= balance
        else:
            print("잔액이 부족합니다")

    def get_balance(self):
        return self.balance

account = BankAccount("홍길동")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000

account.withdraw(10000)  # 잔액이 부족합니다
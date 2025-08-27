class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{self.owner}님의 계좌로 {amount}원 입금되었습니다. 현재 잔액 : {self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.owner}님의 계좌에서 {amount}원을 출금하였습니다! 현재 잔액 : {self.balance}")
        else:
            print("잔액이 부족합니다")

    def check_balance(self):
        print(f"{self.owner}님의 현재 계좌 잔액 : {self.balance}원")

bank1 = BankAccount("모은지",10000)
bank1.check_balance()
bank1.deposit(100000)
bank1.check_balance()
bank1.withdraw(50000)
bank1.check_balance()

bank2 = BankAccount("홍길동",100000000)
bank2.check_balance()

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if self.balance >= amount >0:
            self.balance -= amount
        else:
            print("Insufficient funds")   

    def print_balance(self):
        print(f"Balance: ${self.balance}")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0):
        super().__init__(balance)
        if interest_rate > 0:
            self.interest_rate = interest_rate
        else:
            self.interest_rate = 0.0001

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} added. New balance: ${self.balance}")



class CheckingAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)


def main():
    cont_economii = SavingsAccount(balance=1000, interest_rate=0.02)
    cont_economii.deposit(500)
    cont_economii.calculate_interest()

    cont_curent = CheckingAccount(balance=500)
    cont_curent.withdraw(300)
    cont_curent.withdraw(700)
    cont_curent.print_balance()

if __name__ == "__main__":  
    main()
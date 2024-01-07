import time
class ATM:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance
def main():
    atm = ATM()

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
            print(f"Your new balance is: {atm.check_balance()}")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            result = atm.withdraw(amount)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Your new balance is: {result}")

        elif choice == '3':
            print(f"Your current balance is: {atm.check_balance()}")

        elif choice == '4':
            print("Thank you for using our ATM. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")

        time.sleep(2) # Wait for 2 seconds before proceeding

if __name__ == "__main__":
    main()
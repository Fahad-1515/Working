#Simple Banking Program
def create_account():
    name = input("Enter your name: ")
    balance = 0.0
    return name, balance

def check_balance(name, balance):
    print(f"{name}'s Balance: ${balance}")

def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount}")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew: ${amount}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance

def main():
    print("Welcome to the Simple Bank App")
    name, balance = create_account()

    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            check_balance(name, balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("Thank you for using the Simple Bank App. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

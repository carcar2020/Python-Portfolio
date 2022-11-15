import Bank_classes

# First user in our branch

user1 = Bank_classes.Bank("carlos", "Omega Bank", "12345")
user2 = Bank_classes.Bank("Ryan", "Omega Bank", "12345")

# First user data
print("welcome", user1.getname())
print("your current balance is: $" + str(user1.getbalance()))

print("Do you wish to withdraw yes or no (Y/N)")
choice = input("Enter Y for yes or N for no:")
if choice.upper() == "Y":
    Withdraw = float(input("Enter Amount to be Withdrawn:$"))
    user1.withdraws(Withdraw)
    print("Withdraw was successful")
    print("Your new Account balance is:$", user1.getbalance())
elif choice.upper() == "N":
    print("No Withdraw was made")
else:
    print(" You entered wrong data type or something other then (y or n)")

# print( "your new balance is: $", user1.withdraws(100))

print("Your new balance is now: $" + str(user1.getbalance()))

print("Do you wish to make a Deposit yes or no (Y/N)")
choice = input("Enter Y for yes or N for no:")
if choice.upper() == "Y":
    Dep = float(input("Enter Amount to be deposited:$"))
    user1.Deposit(Dep)
    print("Deposit was Succesful")
    print("Your new Account balance is:$", user1.getbalance())
elif choice.upper() == "N":
    print("No deposit was made")
else:
    print(" You entered wrong data type or something other then (y or n)")

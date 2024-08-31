age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
elif age < 0:
    print("Please enter a valid number!")
else:
    print("Not eligible to vote")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

def Greatest(num1, num2, num3):
    if num1 == num2 == num3:
        print("All the numbers are Equal")
    elif num1 > num2 and num1 > num3:
        print("First number is Largest")
    elif num2 > num1 and num2 > num3:
        print("Second number is the Largest")
    elif num3 > num1 and num3 > num2:
        print("Third number is the Largest")
    elif num1 == num2 and num1 > num3:
        print("First and second both are Largest")
    elif num2 == num3 and num2 > num1:
        print("Second and Third both are Largest")
    elif num1 == num3 and num1 > num2:
        print("First and Third both are Largest")
Greatest(num1, num2, num3)

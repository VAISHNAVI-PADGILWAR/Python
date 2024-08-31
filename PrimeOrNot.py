num = int(input("Enter a number: "))

def PrimeOrNot(num):
    flag = 1
    if num >1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                flag = 0
        if flag == 1:
            print("The number is Prime")
        else:
            print("The number is Composite")
    else:
        print("Enter a number greater than 1")

PrimeOrNot(num)

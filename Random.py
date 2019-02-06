import random
flag = 'Y'


def rand(number):
    print("Current Random Number is ")
    print(random.randint(0, number))


while flag == "Y" or flag == "y":
    num = int(input("Enter Random Number range from 1 to : "))
    rand(num)
    flag = input("Check another Random Number (Y/N): "))
    print(flag)

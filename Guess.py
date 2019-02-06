import random
flag = 'Y'


RandomNum = random.randint(0, 100)

InputNum = int(input("Enter the random number you have guess: "))
if RandomNum == InputNum:
    print("Congrats !!!! Your guessed it right in first time :)")
elif RandomNum < InputNum:
    print("oops !! that was not quite right. Try little lower number...")
    InputNum = int(input("\nEnter the Next random number you have guessed: "))
elif RandomNum > InputNum:
    print("oops !! that was not quite right. Try little higher number...")
    InputNum = int(input("\nEnter the Next random number you have guessed: "))

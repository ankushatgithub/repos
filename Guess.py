import random
flag = 'Y'


RandomNum = random.randint(0, 100)
print (RandomNum)
times = 0
InputNum = int(input("Enter the random number between 1 to 100: "))
times += 1
while RandomNum != InputNum:

    if RandomNum == InputNum:
        print("Congrats !!!! Your guessed it right in %s time :)" %times)
    elif RandomNum < InputNum:
        print("oops !! that was not quite right. Try little lower number...")
        InputNum = int(input("\nEnter the Next random number you have guessed: "))
        times += 1
    elif RandomNum > InputNum:
        print("oops !! that was not quite right. Try little higher number...")
        InputNum = int(input("\nEnter the Next random number you have guessed: "))
        times += 1
    if times > 3:
        break

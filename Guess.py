import random


RandomNum = random.randint(0, 100)
# print (RandomNum)
times = 0
InputNum = int(input("Enter the random number between 1 to 100: "))
times += 1
if RandomNum == InputNum:
    print("Congrats !!!! Your guessed it right in 1st attempt :)")
while RandomNum != InputNum:
    if times >= 3:
        print("Sorry !!! Number of attempts exceeded ... Correct Number was %s" % RandomNum)
        break
    if RandomNum < InputNum:
        print("oops !! that was not quite right. Try little lower number...")
        InputNum = int(input("\nEnter the Next random number you have guessed: "))
        times += 1
    elif RandomNum > InputNum:
        print("oops !! that was not quite right. Try little higher number...")
        InputNum = int(input("\nEnter the Next random number you have guessed: "))
        times += 1
    if RandomNum == InputNum:
        print("Congrats !!!! Your guessed it right in %s attempts :)" % times)
        break

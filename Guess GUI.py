from Tkinter import *
import random
# import ttk

window = Tk()

note_l = Label(text='Enter the random number between 1 to 100: ')
attrem_l = Label(text="Attempts Remaining: 3")
result_l = Label(text='Result: ')
RandomNum = random.randint(1, 100)
times = 0
TotalAttempts = 3
guess_l1 = Label(text="Guess 1 ")
guess_l2 = Label(text="Guess 2 ")
guess_l3 = Label(text="Guess 3 ")

window.title("--Guess Random Number--")
window.geometry('800x400')
e = Entry(window)


def clicked():
    # print (RandomNum)
    b.configure(text="Check Again")
    InputNum = int(e.get())
    global times
    global TotalAttempts
    global result
    times += 1

    if times == 1:
        guess_l1.configure(text="Guess 1 = " + str(InputNum))
    elif times == 2:
        guess_l2.configure(text="Guess 2 = " + str(InputNum))
    elif times == 3:
        guess_l3.configure(text="Guess 3 = " + str(InputNum))

    attrem_l.configure(text="Attempts Remaining: "+str(TotalAttempts-times))
    if RandomNum == InputNum:
        result_l.configure(text="Result: Congrats !!!! Your guessed it right in " + str(times) + " attempts :)")
        return
    while RandomNum != InputNum:
        if times >= TotalAttempts:
            result_l.configure(text="Result: Sorry !!! Number of attempts exceeded ... Correct Number was "+str(RandomNum))
            break
        if RandomNum < InputNum:
            result_l.configure(text="Result: oops !! that was not quite right. Try little lower number...")
        elif RandomNum > InputNum:
            result_l.configure(text="Result: oops !! that was not quite right. Try little higher number...")
        e.delete(0, END)
        return


b = Button(text="Check", width=10, command=clicked)
e.focus_set()
note_l.pack()
attrem_l.pack()
result_l.pack()
e.pack()
b.pack()
guess_l1.pack()
guess_l2.pack()
guess_l3.pack()
window.mainloop()

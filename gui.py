from tkinter import *
from tkinter import ttk
import tkinter as tk
import collections

def action(inputSymbol, inputReplace, movement, nextState):
    global head, state, tape
    if tape[head] == inputSymbol:
        tape[head] = inputReplace
        state = nextState
        if movement == 'R':
            head += 1
        elif movement == 'L':
            head -= 1
        return True
    return False
##################################################################

window = Tk()
window.title("Turing Machine Simulator")
window.geometry('500x500')

title = Label(window, text="Turing Machine Simulator", width=500, anchor=W, background="#3caea3")
title.config(font=("Roboto", 20), foreground="white", padx=10, pady=10)
title.pack()

# separator = ttk.Separator(orient='horizontal')
# separator.place(x=0, y=50, relwidth=1, relheight=1)

frameInput = LabelFrame(window, text="input", padx=5, pady=5)
frameInput.pack(padx=10, pady=10)

input1 = StringVar(window)
input1.set("positive integer")

operand = StringVar(window)
operand.set("+")

input2 = StringVar(window)
input2.set("positive integer")

entry1 = Entry(frameInput, textvariable=input1)
entry1.pack(padx=20, pady=20, side=tk.LEFT)

option = OptionMenu(frameInput, operand,"+", "-", "*", "/", "!", "%", "^", "log")
option.pack(padx=20, pady=20, side=tk.LEFT)

entry2 = Entry(frameInput, textvariable=input2)
entry2.pack(padx=20, pady=20, side=tk.LEFT)

frameOutput = LabelFrame(window, text="output", padx=5, pady=5)
frameOutput.pack(padx=10, pady=10)



    

##################################################################

def caller():
    global temp1, temp2, inputAdd, head, state, tape
    temp1, temp2 = "", ""
    for i in range (int(input1.get())):
        temp1 += "0"
    for i in range (int(input2.get())):
        temp2 += "0"
    if operand.get() == "+":
        inputAdd = temp1 + "a" + temp2
        inputString = inputAdd
        inputLength = len(inputString) * 2
        tape = ['B'] * inputLength
        i = 1
        head = 1
        for char in inputString:
            tape[i] = char
            i += 1
        state = 0
        oldHead = -1
        acc = False
        X, R, L, B = 'X', 'R', 'L', 'B' #simbol yang diperlukan fungsi
        a = 'a' #simbol adisi
        while(oldHead != head):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)

            if state == 0:
                if action('0', X, R, 1) or action(a, B, L, 5):
                    pass
            
            elif state == 1:
                if action('0', '0', R, 1) or action(a, a, R, 2):
                    pass
            
            elif state == 2:
                if action('0', '0', R, 2) or action(B, '0', L, 3):
                    pass
            
            elif state == 3:
                if action('0', '0', L, 3) or action(a, a, L, 4):
                    pass
            
            elif state == 4:
                if action('0', '0', L, 4) or action(X, X, R, 0):
                    pass

            elif state == 5:
                if action(X, B, L, 5):
                    acc = True
                    pass

        elements_count = collections.Counter(tape)
        if acc:
            print("Input halt dan diterima di state: ", state, " dengan hasil: ", elements_count['0'])
            Label(frameOutput, text=elements_count['0']).pack()
        else:
            print("Input tidak diterima di state: ", state)    

    elif operand.get() == "/":
        inputDiv = temp1 + "d" + temp2
        inputString = inputDiv
        inputLength = len(inputString) * 2
        tape = ['B'] * inputLength
        i = 1
        head = 1
        for char in inputString:
            tape[i] = char
            i += 1
        state = 0
        oldHead = -1
        acc = False
        X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B' #simbol yang diperlukan fungsi
        d = 'd' #simbol divisi
        while(oldHead != head):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)

            if state == 0:
                if action('0', B, R, 1) or action(d, B, R, 8):
                    pass
            
            elif state == 1:
                if action('0', '0', R, 1) or action(d, d, R, 2):
                    pass
            
            elif state == 2:
                if action('0', '0', R, 2) or action(X, X, R, 2) or action(Y, Y, L, 3) or action(B, B, L, 3):
                    pass
            
            elif state == 3:
                if action(X, X, L, 3) or action('0', X, L, 4):
                    pass
            
            elif state == 4:
                if action('0', '0', L, 6) or action(d, d, R, 5):
                    pass

            elif state == 5:
                if action(X, '0', R, 5) or action(Y, Y, R, 5) or action(B, Y, L, 6):
                    pass

            elif state == 6:
                if action('0', '0', L, 6) or action(Y, Y, L, 6) or action(d, d, L, 7):
                    pass

            elif state == 7:
                if action('0', '0', L, 7) or action(B, B, R, 0):
                    pass

            elif state == 8:
                if action(Y, '0', R, 8) or action('0', B, R, 8) or action(B, B, R, 9):
                    pass

            elif state == 9:
                acc = True

        elements_count = collections.Counter(tape)
        if acc:
            print("Input halt dan diterima di state: ", state, " dengan hasil: ", elements_count['0'])
        else:
            print("Input tidak diterima di state: ", state)    

submit = Button(frameInput, text="run", command=caller)
submit.pack(side=tk.BOTTOM)


window.mainloop()
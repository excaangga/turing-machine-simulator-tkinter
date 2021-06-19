from tkinter import *
from tkinter import ttk
import collections
import os


def restart():
    canvas.delete("all")
    for widget in frameResult.winfo_children():
        widget.pack_forget()

##################################################################
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
window.geometry('700x700')

title = Label(window, text="Turing Machine Simulator", width=700, anchor=N, background="#3caea3")
title.config(font=("Roboto", 20), foreground="white", padx=10, pady=10)
title.pack(pady=(0, 20))

# separator = ttk.Separator(orient='horizontal')
# separator.place(x=0, y=50, relwidth=1, relheight=1)

frameInput = ttk.LabelFrame(window, text="input")
frameInput.pack(padx=10, pady=10)

input1 = StringVar(window)
input1.set("positive integer")

operand = StringVar(window)
operand.set("+")

input2 = StringVar(window)
input2.set("positive integer")

entry1 = ttk.Entry(frameInput, textvariable=input1)
entry1.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)

option = ttk.OptionMenu(frameInput, operand,"+", "-", "*", "/", "!", "%", "^", "log")
option.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)

entry2 = ttk.Entry(frameInput, textvariable=input2)
entry2.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)



frameOutput = ttk.LabelFrame(window, text="output", width=600)

v = Scrollbar(frameOutput)
h = Scrollbar(frameOutput, orient=HORIZONTAL)
v.pack(side=RIGHT, fill=Y)
h.pack(side=BOTTOM, fill=X)
canvas = Canvas(frameOutput, width=550, height=400, yscrollcommand=v.set, xscrollcommand=h.set)
canvas.pack()
v.config(command=canvas.yview)
h.config(command=canvas.xview)

frameOutput.pack()



frameResult = Frame(window)
frameResult.pack(anchor=CENTER)


    

##################################################################

def drawInline(inputLength, x1, x2, y1, y2, counter, tape, head):
    for j in range (inputLength):
        x1 += 20
        x2 += 20
        if True:
            box = canvas.create_rectangle(x1, y1, x2+20, y2, fill="white smoke")
            #print("TESTTTTT", j)
            cells.append(box)
            label = canvas.create_text((x1+x2)/2 + 10, (y1+y2)/2, text=tape[j])
            if head == j:
                canvas.itemconfig(box, fill="yellow")
            
            canvas.config(scrollregion=(0, 0, x1+40, y1+40))
            canvas.pack(expand=YES, fill=BOTH)
            counter += 1
        
        # else:
        #     drawInline(inputLength-counter, 0, 0, y1+40, y2+40, counter, tape)

##################################################################

def caller():
    global temp1, temp2, head, state, tape, cells
    temp1, temp2 = "", ""
    cells = []
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
        x1, x2 = 0, 0
        y1, y2 = 20, 40
        for char in inputString:
            tape[i] = char
            i += 1
        state = 0
        oldHead = -1
        acc = False
        X, R, L, B = 'X', 'R', 'L', 'B' #simbol yang diperlukan fungsi
        a = 'a' #simbol adisi
        increment = 0
        while(oldHead != head):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)
            drawInline(inputLength, x1, x2, y1+increment, y2+increment, 0, tape, head)
            increment += 40
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
            ttk.Label(frameResult, text="Result: ").pack(pady=10)
            ttk.Label(frameResult, text=elements_count['0']).pack()
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

ttk.Style().configure("TButton", padding=5, relief="flat")
submit = ttk.Button(frameInput, text="run", command=caller, width=7)
reset = ttk.Button(frameInput, text="reset", command=restart, width=7)
submit.pack(side=LEFT, anchor=CENTER, padx=10)
reset.pack(side=LEFT, anchor=CENTER, padx=10)


window.mainloop()
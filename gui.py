# "Bismillah" first before reading this whole untested __masterpiece__ :"v


from tkinter import *
from tkinter import ttk
import collections

# this block is for restarting the operation


def restart():
    canvas.delete("all")
    for widget in frameResult.winfo_children():
        widget.pack_forget()

##################################################################

# this block handles the turing tape movement


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


# this is basically the window creation
window = Tk()
window.title("Turing Machine Simulator")
window.geometry('700x750')

# titling the window
title = Label(window, text="Turing Machine Simulator",
              width=700, anchor=N, background="#3caea3")
title.config(font=("Roboto", 20), foreground="white", padx=10, pady=10)
title.pack(pady=(0, 20))

# make a frame that contains input widgets, later called as "INPUT" in its child comments
frameInput = ttk.LabelFrame(window, text="input")
frameInput.pack(padx=10, pady=10)

# INPUT | entry1(input1)
# this is the param
input1 = StringVar(window)
input1.set("positive integer")

# INPUT | option(operand)
# this is the param
operand = StringVar(window)
operand.set("")

# INPUT | entry2(input2)
# this is the param
input2 = StringVar(window)
input2.set("positive integer")

# INPUT | entry1(input1)
entry1 = ttk.Entry(frameInput, textvariable=input1)
entry1.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)

# function to detect change in option


def opt(event):
    global warning
    if operand.get() == "log(2)" or operand.get() == "!":
        entry2.pack_forget()
        input2.set(0)
    else:
        entry2.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)
        input1.set("positive integer")
        input2.set("positive integer")
    if operand.get() == "-":
        warning = ttk.Label(frameWarning, text="Entry 1 must be equal or less than Entry 2 to proceed").pack(
            pady=10, side=BOTTOM)
    else:
        for widget in frameWarning.winfo_children():
            widget.destroy()


# INPUT | option(operand)
option = ttk.OptionMenu(frameInput, operand, "+", "+",
                        "-", "*", "/", "!", "%", "^", "log(2)", command=opt)
option.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)

# INPUT | entry2(input2)
entry2 = ttk.Entry(frameInput, textvariable=input2)
entry2.pack(padx=20, pady=20, side=LEFT, anchor=CENTER)

# make a frame for warnings
frameWarning = ttk.Frame(window)
frameWarning.pack()

# make a frame that contains output drawings
frameOutput = ttk.LabelFrame(window, text="output", width=600)

# defining the scrollbar, both vertical and horizontal
v = Scrollbar(frameOutput)
h = Scrollbar(frameOutput, orient=HORIZONTAL)
v.pack(side=RIGHT, fill=Y)
h.pack(side=BOTTOM, fill=X)

# making canvas for the tapes' drawings
canvas = Canvas(frameOutput, width=550, height=400,
                yscrollcommand=v.set, xscrollcommand=h.set)
canvas.pack()

# assigning the scrollbar to the canvas
v.config(command=canvas.yview)
h.config(command=canvas.xview)

frameOutput.pack()

# make a frame that contains result of the calculation, later called as "RESULT" in its child comments
frameResult = Frame(window)
frameResult.pack(anchor=CENTER)

##################################################################

# the function that responsible for drawing tapes


def drawInline(inputLength, x1, x2, y1, y2, counter, tape, head):
    for j in range(inputLength):
        x1 += 20
        x2 += 20
        box = canvas.create_rectangle(x1, y1, x2+20, y2, fill="white smoke")
        label = canvas.create_text((x1+x2)/2 + 10, (y1+y2)/2, text=tape[j])
        if head == j:
            canvas.itemconfig(box, fill="yellow")

        canvas.config(scrollregion=(0, 0, x1+40, y1+40))
        canvas.pack(expand=YES, fill=BOTH)
        counter += 1

##################################################################

# main function for starting the turing machine


def caller():
    global temp1, temp2, head, state, tape, cells
    temp1, temp2 = "", ""

    # converting GUI input to CLI input
    for i in range(int(input1.get())):
        temp1 += "0"
    for i in range(int(input2.get())):
        temp2 += "0"

    # + operation
    if operand.get() == "+":
        inputString = temp1 + "a" + temp2
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
        # just "as-usual" turing symbols
        X, R, L, B = 'X', 'R', 'L', 'B'
        # symbol for addition
        a = 'a'
        increment = 0
        # a whole movement block
        while(oldHead != head):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)
            drawInline(inputLength, x1, x2, y1+increment,
                       y2+increment, 0, tape, head)
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

        # make a counter for the 0's in the tape as the final result
        elements_count = collections.Counter(tape)
        if acc:
            print("Input halt dan diterima di state: ", state,
                  " dengan hasil: ", elements_count['0'])
            # RESULT | labels
            ttk.Label(frameResult, text="Result: ").pack(pady=10)
            ttk.Label(frameResult, text=elements_count['0']).pack()
        else:
            print("Input tidak diterima di state: ", state)
            ttk.Label(frameResult, text="Input declined on state: ").pack(
                pady=10)
            ttk.Label(frameResult, text=state).pack()

    # / operation
    elif operand.get() == "/":
        inputString = temp1 + "d" + temp2
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
        # just "as-usual" turing symbols
        X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'
        # symbol for division
        d = 'd'
        increment = 0
        # a whole movement block
        while(oldHead != head):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)
            drawInline(inputLength, x1, x2, y1+increment,
                       y2+increment, 0, tape, head)
            increment += 40
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
                if action(Y, '0', R, 8) or action('0', B, R, 8) or action(B, B, L, 9):
                    pass

            elif state == 9:
                acc = True

        # make a counter for the 0's in the tape as the final result
        elements_count = collections.Counter(tape)
        if acc:
            print("Input halt dan diterima di state: ", state,
                  " dengan hasil: ", elements_count['0'])
            # RESULT | labels
            ttk.Label(frameResult, text="Result: ").pack(pady=10)
            ttk.Label(frameResult, text=elements_count['0']).pack()
        else:
            print("Input tidak diterima di state: ", state)
            ttk.Label(frameResult, text="Input declined on state: ").pack(
                pady=10)
            ttk.Label(frameResult, text=state).pack()

    # % operation
    elif operand.get() == "%":
        if temp1 != "" and temp2 != "":
            inputString = temp1 + "m" + temp2
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
            # just "as-usual" turing symbols
            X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'
            # symbol for modulation
            m = 'm'
            increment = 0
            # a whole movement block
            while(oldHead != head):
                oldHead = head
                print(tape, ", head di index ", head, " pada state ", state)
                drawInline(inputLength, x1, x2, y1+increment,
                           y2+increment, 0, tape, head)
                increment += 40
                if state == 0:
                    if action('0', '0', R, 0) or action(m, m, R, 1):
                        pass

                elif state == 1:
                    if action('0', '0', R, 1) or action(B, m, L, 2):
                        pass

                elif state == 2:
                    if action(m, m, R, 7) or action('0', X, L, 3):
                        pass

                elif state == 3:
                    if action('0', '0', L, 3) or action(m, m, L, 4):
                        pass

                elif state == 4:
                    if action(B, B, R, 8) or action(Y, Y, L, 4) or action('0', Y, R, 5):
                        pass

                elif state == 5:
                    if action(Y, Y, R, 5) or action(m, m, R, 6):
                        pass

                elif state == 6:
                    if action('0', '0', R, 6) or action(X, X, L, 2):
                        pass

                elif state == 7:
                    if action(m, m, L, 2) or action(X, '0', R, 7):
                        pass

                elif state == 8:
                    if action(Y, B, R, 8) or action(m, B, R, 9):
                        pass

                elif state == 9:
                    if action('0', B, R, 9) or action(X, '0', R, 9) or action(m, B, L, 10):
                        pass

                elif state == 10:
                    if action('0', B, L, 11):
                        pass

                elif state == 11:
                    acc = True

            # make a counter for the 0's in the tape as the final result
            elements_count = collections.Counter(tape)
            if acc:
                print("Input halt dan diterima di state: ", state,
                      " dengan hasil: ", elements_count['0'])
                # RESULT | labels
                ttk.Label(frameResult, text="Result: ").pack(pady=10)
                ttk.Label(frameResult, text=elements_count['0']).pack()
            else:
                print("Input tidak diterima di state: ", state)
                ttk.Label(frameResult, text="Input declined on state: ").pack(
                    pady=10)
                ttk.Label(frameResult, text=state).pack()
        else:
            print("Input tidak bisa diproses")
            ttk.Label(frameResult, text="Input can't be processed").pack(pady=10)

    # binary log operation
    elif operand.get() == "log(2)":
        if temp1 != "" and int(input1.get()) % 2 == 0:
            inputString = temp1
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
            # just "as-usual" turing symbols
            X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'
            increment = 0
            # a whole movement block
            while(oldHead != head):
                oldHead = head
                print(tape, ", head di index ", head, " pada state ", state)
                drawInline(inputLength, x1, x2, y1+increment,
                           y2+increment, 0, tape, head)
                increment += 40
                if state == 0:
                    if action('0', '0', R, 1) or action(B, B, R, 12):
                        pass

                elif state == 1:
                    if action('0', '0', R, 2) or action(B, B, L, 11):
                        pass

                elif state == 2:
                    if action('0', X, R, 3) or action(B, B, L, 11):
                        pass

                elif state == 3:
                    if action(X, X, R, 3) or action('0', X, L, 4) or action(B, B, L, 7):
                        pass

                elif state == 4:
                    if action(Y, Y, L, 4) or action('0', '0', L, 4) or action(X, X, L, 4) or action(B, B, R, 5):
                        pass

                elif state == 5:
                    if action('0', Y, R, 5) or action(Y, '0', R, 6) or action(X, '0', R, 6):
                        pass

                elif state == 6:
                    if action(Y, Y, R, 6) or action('0', '0', R, 6) or action(X, X, R, 3):
                        pass

                elif state == 7:
                    if action(Y, Y, L, 7) or action('0', '0', L, 7) or action(X, B, L, 7) or action(B, B, R, 8):
                        pass

                elif state == 8:
                    if action(Y, '0', R, 8) or action('0', '0', R, 9):
                        pass

                elif state == 9:
                    if action(Y, '0', R, 9) or action('0', '0', R, 10) or action(B, B, L, 11):
                        pass

                elif state == 10:
                    if action(Y, '0', R, 10) or action('0', '0', R, 10) or action(B, B, R, 12):
                        pass

                elif state == 11:
                    if action('0', B, R, 12):
                        pass

                elif state == 12:
                    acc = True

            # make a counter for the 0's in the tape as the final result
            elements_count = collections.Counter(tape)
            if acc:
                print("Input halt dan diterima di state: ", state,
                      " dengan hasil: ", elements_count['0'])
                # RESULT | labels
                ttk.Label(frameResult, text="Result: ").pack(pady=10)
                ttk.Label(frameResult, text=elements_count['0']).pack()
            else:
                print("Input tidak diterima di state: ", state)
                ttk.Label(frameResult, text="Input declined on state: ").pack(
                    pady=10)
                ttk.Label(frameResult, text=state).pack()
        else:
            print("Input tidak bisa diproses")
            ttk.Label(frameResult, text="Input can't be processed").pack(pady=10)

    # - operation
    elif operand.get() == "-":
        if temp1 != "" and temp2 != "" and int(input1.get()) >= int(input2.get()):
            inputString = temp1 + "X" + temp2
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
            # just "as-usual" turing symbols
            X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'
            increment = 0
            # a whole movement block
            while(oldHead != head):
                oldHead = head
                print(tape, ", head di index ", head, " pada state ", state)
                drawInline(inputLength, x1, x2, y1+increment,
                           y2+increment, 0, tape, head)
                increment += 40
                if state == 0:
                    if action('0', '0', R, 0) or action(X, X, R, 1):
                        pass

                elif state == 1:
                    if action('0', '0', R, 1) or action(B, B, L, 2):
                        pass

                elif state == 2:
                    if action('0', B, L, 3) or action(X, B, L, 6):
                        pass

                elif state == 3:
                    if action('0', '0', L, 3) or action(X, X, L, 4):
                        pass

                elif state == 4:
                    if action('0', '0', L, 4) or action(B, B, R, 5):
                        pass

                elif state == 5:
                    if action('0', B, R, 0):
                        pass

                elif state == 6:
                    acc = True

            # make a counter for the 0's in the tape as the final result
            elements_count = collections.Counter(tape)
            if acc:
                print("Input halt dan diterima di state: ", state,
                      " dengan hasil: ", elements_count['0'])
                # RESULT | labels
                ttk.Label(frameResult, text="Result: ").pack(pady=10)
                ttk.Label(frameResult, text=elements_count['0']).pack()
            else:
                print("Input tidak diterima di state: ", state)
                ttk.Label(frameResult, text="Input declined on state: ").pack(
                    pady=10)
                ttk.Label(frameResult, text=state).pack()
        else:
            print("Input tidak bisa diproses")
            ttk.Label(frameResult, text="Input can't be processed").pack(pady=10)

    # dear my future self, i'm sorry for hardcoding the entire system :( - angga
    # factorial operation
    elif operand.get() == "!":
        if temp1 != "":
            inputString = temp1
            # this length is usable for n! where n <= 4 :(
            inputLength = len(inputString*3) * 10
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
            # just "as-usual" turing symbols
            X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'
            increment = 0
            # a whole movement block
            while(oldHead != head):
                oldHead = head
                print(tape, ", head di index ", head, " pada state ", state)
                drawInline(inputLength, x1, x2, y1+increment,
                           y2+increment, 0, tape, head)
                increment += 40
                if state == 0:
                    if action('0', '0', R, 0) or action(B, '1', L, 1):
                        pass

                elif state == 1:
                    if action('0', '0', L, 1) or action('1', '1', L, 1) or action(B, B, R, 2):
                        pass

                elif state == 2:
                    if action('1', '1', R, 5) or action('0', X, R, 3):
                        pass

                elif state == 3:
                    if action('0', '0', R, 3) or action('1', '1', R, 3) or action(B, '0', L, 4):
                        pass

                elif state == 4:
                    if action('0', '0', L, 4) or action('1', '1', L, 4) or action(X, X, R, 2):
                        pass

                elif state == 5:
                    if action('0', '0', R, 5) or action(B, '1', L, 7):
                        pass

                elif state == 6:
                    if action('1', '1', L, 6) or action(X, X, L, 6) or action('0', '0', L, 6) or action(B, B, R, 16):
                        pass

                elif state == 7:
                    if action('1', '1', L, 7) or action('0', '0', L, 7) or action(X, '0', L, 7) or action(B, B, R, 8):
                        pass

                elif state == 8:
                    if action('0', B, R, 9):
                        pass

                elif state == 9:
                    if action('0', X, R, 10) or action('1', '1', L, 6):
                        pass

                elif state == 10:
                    if action('1', '1', R, 11) or action('0', '0', R, 10):
                        pass

                elif state == 11:
                    if action('1', '1', L, 14) or action('0', X, R, 12):
                        pass

                elif state == 12:
                    if action('0', '0', R, 12) or action('1', '1', R, 12) or action(B, '0', L, 13):
                        pass

                elif state == 13:
                    if action('1', '1', L, 13) or action('0', '0', L, 13) or action(X, X, R, 11):
                        pass

                elif state == 14:
                    if action(X, '0', L, 14) or action('1', '1', L, 15):
                        pass

                elif state == 15:
                    if action('0', '0', L, 15) or action('1', '0', L, 15) or action(X, X, R, 9):
                        pass

                elif state == 16:
                    if action('1', B, R, 25) or action(X, B, R, 17):
                        pass

                elif state == 17:
                    if action(X, X, R, 19) or action('1', B, R, 18) or action('0', B, R, 18):
                        pass

                elif state == 18:
                    if action('0', B, R, 18) or action(X, X, R, 22) or action('1', B, L, 24):
                        pass

                elif state == 19:
                    if action('1', '1', R, 20) or action(X, X, R, 19) or action('0', '0', R, 19):
                        pass

                elif state == 20:
                    if action(X, X, R, 20) or action('0', '0', R, 20) or action('1', '1', L, 21):
                        pass

                elif state == 21:
                    if action(X, X, L, 21) or action('0', X, L, 6) or action('1', X, L, 6):
                        pass

                elif state == 22:
                    if action(X, X, R, 22) or action('1', '1', R, 22) or action('0', '0', R, 22) or action(B, '1', L, 23):
                        pass

                elif state == 23:
                    if action(X, '0', R, 23) or action('0', '0', L, 23) or action('1', '1', L, 23) or action(B, B, R, 9):
                        pass

                elif state == 24:
                    acc = True
                    pass

                elif state == 25:
                    if action('0', '0', R, 25) or action('1', B, R, 25) or action(B, B, L, 24):
                        pass
            # make a counter for the 0's in the tape as the final result
            elements_count = collections.Counter(tape)
            if acc:
                print("Input halt dan diterima di state: ", state,
                      " dengan hasil: ", elements_count['0'])
                # RESULT | labels
                ttk.Label(frameResult, text="Result: ").pack(pady=10)
                ttk.Label(frameResult, text=elements_count['0']).pack()
            else:
                print("Input tidak diterima di state: ", state)
                ttk.Label(frameResult, text="Input declined on state: ").pack(
                    pady=10)
                ttk.Label(frameResult, text=state).pack()
        else:
            print("Input tidak bisa diproses")
            ttk.Label(frameResult, text="Input can't be processed").pack(pady=10)

    # ^ operation
    elif operand.get() == "^":
        inputString = temp2 + "C" + temp1
        inputLength = len(inputString) ** 2
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
        # just "as-usual" turing symbols
        X, Y, R, L, B, C = 'X', 'Y', 'R', 'L', 'B', 'C'
        increment = 0
        # a whole movement block
        while(oldHead != head):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)
            drawInline(inputLength, x1, x2, y1+increment,
                       y2+increment, 0, tape, head)
            increment += 40
            if state == 0:
                if action(C, B, R, 31) or action('0', X, R, 1):
                    pass

            elif state == 1:
                if action(C, C, R, 1) or action('0', '0', R, 1) or action(B, C, L, 2):
                    pass

            elif state == 2:
                if action(C, C, L, 2) or action('0', '0', L, 2) or action(X, X, R, 3):
                    pass

            elif state == 3:
                if action(C, B, L, 13) or action('0', X, R, 4):
                    pass

            elif state == 4:
                if action(C, C, R, 5) or action('0', '0', R, 4):
                    pass

            elif state == 5:
                if action(C, C, R, 9) or action('0', Y, R, 6) or action(Y, Y, R, 5):
                    pass

            elif state == 6:
                if action(C, C, R, 7) or action('0', '0', R, 6):
                    pass

            elif state == 7:
                if action(C, C, R, 7) or action('0', '0', R, 7) or action(B, '0', L, 8):
                    pass

            elif state == 8:
                if action(C, C, L, 8) or action('0', '0', L, 8) or action(Y, Y, R, 5):
                    pass

            elif state == 9:
                if action(C, C, R, 9) or action('0', '0', R, 9) or action(B, C, L, 10):
                    pass

            elif state == 10:
                if action(C, C, L, 10) or action('0', '0', L, 10) or action(Y, '0', L, 11):
                    pass

            elif state == 11:
                if action(C, C, L, 12) or action(Y, '0', L, 11):
                    pass

            elif state == 12:
                if action('0', '0', L, 12) or action(X, X, R, 2):
                    pass

            elif state == 13:
                if action(X, B, L, 13) or action(B, B, R, 14):
                    pass

            elif state == 14:
                if action('0', X, R, 15) or action(B, B, R, 14):
                    pass

            elif state == 15:
                if action(C, C, R, 16) or action('0', '0', R, 15):
                    pass

            elif state == 16:
                if action(C, C, L, 20) or action('0', Y, R, 17) or action(Y, Y, R, 16) or action(B, B, L, 29):
                    pass

            elif state == 17:
                if action(C, C, R, 18) or action('0', '0', R, 17):
                    pass

            elif state == 18:
                if action(C, C, R, 18) or action('0', '0', R, 18) or action(B, '0', L, 19):
                    pass

            elif state == 19:
                if action(C, C, L, 19) or action('0', '0', L, 19) or action(Y, Y, R, 16):
                    pass

            elif state == 20:
                if action(C, C, L, 21) or action(Y, '0', L, 20):
                    pass

            elif state == 21:
                if action('0', '0', L, 22) or action(X, B, L, 23):
                    pass

            elif state == 22:
                if action('0', '0', L, 22) or action(X, X, R, 14):
                    pass

            elif state == 23:
                if action(X, B, L, 23) or action(B, B, R, 24):
                    pass

            elif state == 24:
                if action(C, B, R, 25) or action(B, B, R, 24):
                    pass

            elif state == 25:
                if action(C, B, R, 26) or action('0', B, R, 25):
                    pass

            elif state == 26:
                if action(C, C, R, 27) or action('0', '0', R, 26) or action(B, B, L, 32):
                    pass

            elif state == 27:
                if action(C, C, R, 27) or action('0', '0', R, 27) or action(B, C, L, 28):
                    pass

            elif state == 28:
                if action(C, C, L, 28) or action('0', '0', L, 28) or action(B, B, R, 14):
                    pass

            elif state == 29:
                if action(C, '0', L, 30):
                    pass

            elif state == 30:
                if action('0', '0', L, 30) or action(X, B, R, 26):
                    pass

            elif state == 31:
                if action('0', B, R, 31) or action(B, '0', R, 26):
                    pass

            elif state == 32:
                acc = True

        # make a counter for the 0's in the tape as the final result
        elements_count = collections.Counter(tape)
        if acc:
            print("Input halt dan diterima di state: ", state,
                  " dengan hasil: ", elements_count['0'])
            # RESULT | labels
            ttk.Label(frameResult, text="Result: ").pack(pady=10)
            ttk.Label(frameResult, text=elements_count['0']).pack()
        else:
            print("Input tidak diterima di state: ", state)
            ttk.Label(frameResult, text="Input declined on state: ").pack(
                pady=10)
            ttk.Label(frameResult, text=state).pack()

    # * operation
    elif operand.get() == "*":
        inputString = temp1 + "m" + temp2
        inputLength = len(inputString) * 3
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
        # just "as-usual" turing symbols
        X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'
        # symbol for multiplication
        m = 'm'
        increment = 0
        # a whole movement block
        while(oldHead != head and head != -1):
            oldHead = head
            print(tape, ", head di index ", head, " pada state ", state)
            drawInline(inputLength, x1, x2, y1+increment,
                       y2+increment, 0, tape, head)
            increment += 40
            if state == 0:
                if action('0', '0', R, 0) or action(m, m, R, 1):
                    pass

            elif state == 1:
                if action('0', '0', R, 1) or action(B, m, L, 2):
                    pass

            elif state == 2:
                if action(m, m, R, 3) or action('0', '0', L, 2):
                    pass

            elif state == 3:
                if action(X, X, R, 3) or action(m, B, R, 12) or action('0', X, L, 4):
                    pass

            elif state == 4:
                if action(X, X, L, 4) or action(m, m, L, 5):
                    pass

            elif state == 5:
                if action(Y, Y, L, 5) or action('0', Y, R, 6) or action(B, B, R, 11):
                    pass

            elif state == 6:
                if action(Y, Y, R, 6) or action(m, m, R, 7):
                    pass

            elif state == 7:
                if action('0', '0', R, 7) or action(X, X, R, 7) or action(m, m, R, 8):
                    pass

            elif state == 8:
                if action('0', '0', R, 8) or action(B, '0', L, 9):
                    pass

            elif state == 9:
                if action('0', '0', L, 9) or action(m, m, L, 10):
                    pass

            elif state == 10:
                if action('0', '0', L, 10) or action(X, X, L, 10) or action(m, m, L, 5):
                    pass

            elif state == 11:
                if action(Y, '0', R, 11) or action(m, m, R, 3):
                    pass

            elif state == 12:
                if action('0', '0', L, 13) or action(X, B, L, 13) or action(m, B, L, 13) or action('0', B, L, 13):
                    acc = False
                    pass

            elif state == 13:
                if action(B, B, L, 12) or action(X, B, L, 13) or action(m, B, L, 13) or action('0', B, L, 13):
                    acc = True
                    pass

        # make a counter for the 0's in the tape as the final result
        elements_count = collections.Counter(tape)
        if acc:
            print("Input halt dan diterima di state: ", state,
                  " dengan hasil: ", elements_count['0'])
            # RESULT | labels
            ttk.Label(frameResult, text="Result: ").pack(pady=10)
            ttk.Label(frameResult, text=elements_count['0']).pack()
        else:
            print("Input tidak diterima di state: ", state)
            ttk.Label(frameResult, text="Input declined on state: ").pack(
                pady=10)
            ttk.Label(frameResult, text=state).pack()


ttk.Style().configure("TButton", padding=5, relief="flat")
submit = ttk.Button(frameInput, text="run", command=caller, width=7)
reset = ttk.Button(frameInput, text="reset", command=restart, width=7)
reset.pack(side=RIGHT, anchor=CENTER, padx=10)
submit.pack(side=RIGHT, anchor=CENTER, padx=10)


window.mainloop()

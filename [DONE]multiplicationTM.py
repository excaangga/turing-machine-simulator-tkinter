import collections
from typing import AsyncIterable

def action(inputSymbol, inputReplace, movement, nextState):
    global head, state
    if tape[head] == inputSymbol:
        tape[head] = inputReplace
        state = nextState
        if movement == 'R':
            head += 1
        elif movement == 'L':
            head -= 1
        return True
    return False

inputString = input("Masukkan input: ")
inputLength = len(inputString) * 3
tape = ['B'] * inputLength
i = 1
head = 1
for char in inputString:
    tape[i] = char
    i += 1
state = 0
oldHead = -1
acc = False
X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B' # simbol yang diperlukan fungsi
m = "m"

while(oldHead != head and head != -1):
    oldHead = head
    print(tape, ", head di index ", head, " pada state ", state)

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
        if action('0', '0', L, 13)or action(X, B, L, 13) or action(m, B, L, 13) or action('0', B, L, 13):
            acc = False
            pass
    
    elif state == 13:
        if action(B, B, L, 12) or action(X, B, L, 13) or action(m, B, L, 13) or action('0', B, L, 13):
            acc = True
            pass


elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state,
          " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)

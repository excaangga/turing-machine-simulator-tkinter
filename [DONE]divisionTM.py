import collections


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
X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B'  # simbol yang diperlukan fungsi
d = 'd'  # simbol divisi
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
        if action(Y, '0', R, 8) or action('0', B, R, 8) or action(B, B, L, 9):
            pass

    elif state == 9:
        acc = True

elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state,
          " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)

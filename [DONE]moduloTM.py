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
m = 'm'  # simbol divisi
while(oldHead != head):
    oldHead = head
    print(tape, ", head di index ", head, " pada state ", state)

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

elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state,
          " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)

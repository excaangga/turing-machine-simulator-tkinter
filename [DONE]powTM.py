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
inputLength = len(inputString) ** 4
tape = ['B'] * inputLength
i = 1
head = 1
for char in inputString:
    tape[i] = char
    i += 1
state = 0
oldHead = -1
acc = False
X, Y, B, C, R, L = 'X', 'Y', 'B', 'C', 'R', 'L'  # simbol yang diperlukan fungsi
while(oldHead != head):
    oldHead = head
    print(tape, ", head di index ", head, " pada state ", state)

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
        if action(C, B, L, 13) or action('0', X, R, 4) or action(F, '0', S, 4):
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

elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state,
          " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)

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
        elif movement == 'H':
            head += 0
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
X, Y, R, L, H, B = 'X', 'Y', 'R', 'L', 'H', 'B'  # simbol yang diperlukan fungsi
while(oldHead != head):
    oldHead = head
    print(tape, ", head di index ", head, " pada state ", state)

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
        if action('0', '0', R, 25) or action('1', B, R, 25) or action(B, B, H, 24):
            pass

elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state,
          " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)

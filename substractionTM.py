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
X, R, L, B = 'X', 'R', 'L', 'B'  # simbol yang diperlukan fungsi
s = 's'  # simbol adisi
while(oldHead != head):
    oldHead = head
    print(tape, ", head di index ", head, " pada state ", state)

    if state == 0:
        if action('0', '0', R, 0) or action(s, s, R, 1):
            pass

    elif state == 1:
        if action(X, X, R, 1) or action(0, X, L, 2) or action(B, B, L, 5):
            pass

    elif state == 2:
        if action(X, X, L, 2) or action(s, s, L, 3):
            pass

    elif state == 3:
        if action('0', '0', L, 3) or action(B, B, R, 4):
            pass

    elif state == 4:
        if action('0', B, R, 0):
            pass

    elif state == 5:
        if action(X, B, L, 5) or action(s, B, L, 6):
            pass

    elif state == 6:
        acc = True

elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state,
          " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)

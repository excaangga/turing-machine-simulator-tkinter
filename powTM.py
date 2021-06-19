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
X, Y, R, L, B = 'X', 'Y', 'R', 'L', 'B' #simbol yang diperlukan fungsi
m = 'm' #simbol divisi
while(oldHead != head):
    oldHead = head
    print(tape, ", head di index ", head, " pada state ", state)

    if state == 0:
        if action('0', X, R, 1) or action(Y, Y, R, 3):
            pass
    
    elif state == 1:
        if action('0', '0', R, 1) or action(Y, Y, R, 1) or action('1', Y, L, 2):
            pass
    
    elif state == 2:
        if action(Y, Y, L, 2) or action('0', '0', L, 2) or action(X, X, R, 0):
            pass
    
    elif state == 3:
        if action(Y, Y, R, 3) or action(B, B, R, 4):
            pass
    
    elif state == 4:
        acc = True


elements_count = collections.Counter(tape)
if acc:
    print("Input halt dan diterima di state: ", state, " dengan hasil: ", elements_count['0'])
else:
    print("Input tidak diterima di state: ", state)    
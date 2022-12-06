document = open('input.txt')
stream = document.read().split()[0]

bufferSize = 14

def iterate():
    buffer = []
    characterCount = 0

    for char in stream:
        characterCount += 1
        if len(buffer) == bufferSize: del buffer[0]
        buffer.append(char)
        if len(buffer) >= bufferSize and len(set(buffer)) == len(buffer):
            return characterCount

print(iterate())

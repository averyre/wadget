# Simple module for control over output.

def out(message):
    print(message)

def horizontalLine(length):
    return ('-' * (int(length/len('-'))+1))[:length]

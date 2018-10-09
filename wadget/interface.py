# Simple module for control over output.


def out(message):
    print(message)

# Does what it says on the tin, returns a horizontal line at requested length


def horizontalLine(length):
    return ('-' * (int(length / len('-')) + 1))[:length]


# Returns the response ofa Y/N prompt

def ynPrompt(promptText):
    resultInput = input(promptText + " (y/n): ")
    if(resultInput.lower() == 'y') or (resultInput.lower() == "yes"):
        return True
    else:
        return False

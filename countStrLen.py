


def numStr(stR):
    count = len(stR) - stR.count(' ')
    return('\nThe word "{}" has '.format(stR) + str(count) + " letters.")


def numPresent(str):
    if(any(character.isdigit() for character in str) == True):
        return True, "The string contains a number!"
    else:
        return False, "The string does not contain a number!"

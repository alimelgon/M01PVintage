def clear():
    print("\033[2J")

def locate(line,column):
    print("\033[{};{}H".format(line,column),end="")

def clearLine(line=None, column=None):
    if line is not None and column is not None:
        locate(line, column)
    elif line is not None:
        locate(line, 1)
    print("\033[K", end="")
        
def Print(cadena, line, column, delEnd=False):
    locate(line, column)
    if delEnd:
        clearLine()
    print(cadena, end="")
def Input(msg, line, column, delEnd=True):
    locate(line, column)
    if delEnd:
        clearLine()
    return input(msg)

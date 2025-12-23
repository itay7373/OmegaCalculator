def catch_exceptions(e, index=0):
    if isinstance(e, ZeroDivisionError):
        return "Math Error: " + " " * (30 + index) + '^' + "\ncan't divide by zero!\n"
    if isinstance(e, RecursionError):
        return "Math Error: " + " " * (32 + index) + '^' + "\ncan't calculate!\n"
    if isinstance(e, OverflowError):
        return "Math Error:\ncan't calculate!\n"
    return "Syntax Error: " + " " * (30 + index) + '^'

class NoCloseBracketException(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "Missing closing parenthesis!"
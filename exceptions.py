def catch_exceptions(e, index = 0):
  if isinstance(e, ZeroDivisionError):
      return "Math Error: "+" " * (30 + index) + '^' + "\ncan't divide by zero!\n"
  if isinstance(e, RecursionError):
      return "Math Error: "+" " * (34 + index) + '^' + "\ncan't calculate!\n"
  if isinstance(e, OverflowError):
      return "Math Error:\ncan't calculate!\n"
  return "Syntax Error: "+" " * (30+index) + '^'

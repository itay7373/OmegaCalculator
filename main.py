from parser import calc

expression = input("Enter your expression (enter EXIT to exit): ")

while expression.upper() != "EXIT":
  expression = "".join(expression.split())
  print(f"\nthe answer is: {calc(expression)}\n---------------------------")
  expression = input("Enter your expression (enter EXIT to exit): ")

print("thank you for using my calculator!")
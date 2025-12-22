from parser import calc

expression = input("Enter your expression (enter EXIT to exit): ")

while expression.upper() != "EXIT":
  print(f"\nthe answer is: {calc(expression.replace(" ", ""))}\n---------------------------")
  expression = input("Enter your expression (enter EXIT to exit): ")

print("thank you for using my calculator!")
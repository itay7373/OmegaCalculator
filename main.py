from exceptions import catch_exceptions
from parser import calc

expression = input("Enter your expression (enter EXIT to exit): ")

while expression.upper() != "EXIT":
    # מוריד תווים לבנים מהביטוי שהתקבל
    try:
        expression = "".join(expression.split())
        print(f"\nthe answer is: {calc(expression)}\n---------------------------")
    except Exception as e:
        print(f'Error: {e}\n---------------------------\n')

    expression = input("Enter your expression (enter EXIT to exit): ")

print("thank you for using my calculator!")

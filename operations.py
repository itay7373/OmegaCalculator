# מפה שנותנת לכל אופרטור את עוצמת הקדימות שלו
power_map = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '^': 2,
    '%': 3,
    '$': 4,
    '&': 4,
    '@': 4,
}


# מקבל אופרטור ושני מספרים ומחזיר את התוצאה ביניהם
def calculate_operation(operation, num1, num2=0):
    match operation:
        case '-':
            return num1 - num2
        case '+':
            return num1 + num2
        case '/':
            return num1 / num2
        case '*':
            return num1 * num2
        case '^':
            return num1 ** num2
        case '%':
            return num1 % num2
        case '$':
            return max(num1, num2)
        case '&':
            return min(num1, num2)
        case '@':
            return (num1 + num2) / 2
        case '!':
            return factorial(num1)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

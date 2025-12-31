from exceptions import catch_exceptions, NoCloseBracketException, EmptyExpressionException
from operations import power_map, calculate_operation


def find_number(expression, index=0):
    minus_counter = 0
    start_index = index

    # בודק אם יש ~ לפני המספר ומעדכן את מונה המינוסים בהתאם
    if expression[index] == '~':
        start_index += 1
        minus_counter = 1

    # סופר כמה מינוסים יש לפני המספר
    while expression[start_index] == '-':
        minus_counter += 1
        start_index += 1

    # מטפל בסוגריים
    if start_index < len(expression) and expression[start_index] == '(':
        balance = 1
        end_index = start_index + 1
        while end_index < len(expression):
            if expression[end_index] == '(':
                balance += 1
            elif expression[end_index] == ')':
                balance -= 1
            if balance == 0:
                break
            end_index += 1
            if end_index == len(expression):
                raise NoCloseBracketException()

        # קריאה רקורסיבית לחישוב הביטוי שבתוך הסוגריים
        number = calc(expression[start_index + 1:end_index])
        end_index += 1

    else:
        end_index = start_index
        dot_counter = 0

        # רץ כל עוד לא הגענו לסוף הביטוי המתמטי וכל עוד התו הוא מספר או נקודה
        while end_index < len(expression) and (expression[end_index].isnumeric() or expression[end_index] == '.'):
            if expression[end_index] == '.':
                dot_counter += 1
                # אם יש יותר מנקודה אחת במספר עוצר - לא תקין
                if dot_counter > 1:
                    break
            end_index += 1

        # הופך את המחרוזת למספר
        number = float(expression[start_index: end_index])

    number = number if minus_counter % 2 == 0 else -number

    # מטפל במספר שהוא עצרת
    if end_index < len(expression):
        while expression[end_index] == '!' or expression[end_index] == '#':
            if expression[end_index] == '!':
                number = calculate_operation('!', number)
            else:
                number = calculate_operation('#', number)
            end_index += 1


    # מחזיר את המספר, מטפל בשליליות וחיוביות ומחזיר את האינדקס הבא בביטוי המתמטי
    # מחזיר את האינדקס של התו הבא בביטוי המתמטי כדי להמשיך לפתור את התרגיל
    return number, end_index


# מקבל את המטריצה, מספר ואופרנד ומכניס את המספר והאופרנד למטריצה
def insert_to_mat(mat, num, operand=None):
    if operand in power_map:
        mat[power_map[operand]].append(num)
        mat[power_map[operand]].append(operand)


# מקבל את המטריצה ואופרנד ובודקאם קיים אופרנד בעל קדימות גבוה יותר או זהה במטריצה
def check_mat(mat, operand):
    for i in range(len(mat) - 1, power_map[operand] - 1, -1):
        if len(mat[i]) > 0:
            return i
    return -1


# מקבל את המטריצה, מספר ואופרנד, בודק אם להכניס את אותם למטרציה או לבצע חישוב קודם ולהכניס את התוצאה החדשה למטריצה
def calc_mat(mat, num, operand=None):
    index = check_mat(mat, operand)
    if index != -1:
        num2 = mat[index].pop(0)
        operand2 = mat[index].pop()
        new_result = calculate_operation(operand2, num2, num)
        calc_mat(mat, new_result, operand)
    else:
        insert_to_mat(mat, num, operand)


def preparing_expression(expression):
    expression += '+0'
    # מוריד תווים לבנים מהביטוי שהתקבל
    expression = "".join(expression.split())

    minus_counter = 0
    index = 0

    while expression[index] == '-':
        minus_counter += 1
        index += 1

    if minus_counter % 2 == 1:
        expression = '0' + expression

    return expression


# הפעולה מקבלת ביטוי ומחשבת את התוצאה
# דרכי הפעולה של הפונקציה:
# היא מחפשת את המספר ואת פעולת החשבון הבאים - זוג, ובכל פעם מנסה להכניס אום ל"מטריצה"
# כל זוג כזה נכנס למטריצה למערך של רמת החוזקה של הפעולה שלו
# כך ש+1 יכנס במקום ה0 במטריצה אבל @3 יכנס במקום ה4 במטריצה
# אם במטריצה קיים זוג חזק יותר, המטריצה מחשבת את התוצאה בין המספר שקיים במטריצה, פעולת החשבון החזקה יותר והמספר החדש
# ומכניסה למטריצה את התוצאה ואת הפעולת חשבון החלשה יותר
# לכל ביטוי נוסיף +0 בסוף הביטוי, כל שהוא לא משפיע על התוצאה הסופית אבל מאפשר לנו לצמצם את המטריצה בגלל ש+ נמצא ברמת חוזקה הקטנה ביותר
# ובכך נוכל להגיד שתמיד התוצאה של הביטוי כולו הוא המקום ה0 0 במטריצה בסוף החישוב
def calc(expression):
    # אם הביטוי ריק מעלה שגיאה מתאימה
    if len(expression) == 0:
        raise EmptyExpressionException()

    expression = preparing_expression(expression)

    mat = [
        [],
        [],
        [],
        [],
        []
    ]

    index = 0

    try:
        # מקבל את המספר הראשון בביטוי ואת האינדקס של האופרטור שאחריו
        num, index = find_number(expression, index)
        while index < len(expression):
            # מקבל את האופרטור שאחרי המספר
            op = expression[index]

            # מטפל במקרים שלא צויינה פעולת חשבון לפני הסוגריים (כפל) לדוגמה (2+1)2
            if op == '(':
                op = '*'
                index -= 1

            # מכניס את המספר והאופרטור למטרציה ומבצע חישוב במטריצה
            calc_mat(mat, num, op)

            # מגדיל את האינדקס באחד כי אנחנו כרגע נמצאים על האינדקס של האופרטור ואנחנו רוצים לעבור לתחילת המספר הבא
            index += 1
            # מקבל את המספר הבא בביטוי ואת האינדקס של האופרטור שאחריו
            num, index = find_number(expression, index)
    # טיפול בשגיאות
    except Exception as e:
        print(catch_exceptions(e, index))
        raise e

    return mat[0][0]

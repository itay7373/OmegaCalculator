from operations import power_map, calculate_operation


def find_number(expression, index=0):
    minus_counter = 0
    start_index = index

    #בודק אם יש ~ לפני המספר ומעדכן את מונה המינוסים בהתאם
    if expression[index] == '~':
        start_index += 1
        minus_counter = 1

    # סופר כמה מינוסים יש לפני המספר
    while expression[start_index] == '-':
        minus_counter += 1
        start_index += 1

    end_index = start_index
    dot_counter = 0

    #רץ כל עוד לא הגענו לסוף הביטוי המתמטי וכל עוד התו הוא מספר או נקודה
    while end_index < len(expression) and (expression[end_index].isnumeric() or expression[end_index] == '.'):
        if expression[end_index] == '.':
            dot_counter += 1
            # אם יש יותר מנקודה אחת במספר עוצר - לא תקין
            if dot_counter > 1:
                break
        end_index += 1

    #הופך את המחרוזת למספר
    number = float(expression[start_index: end_index])

    #מחזיר את המספר, מטפל בשליליות וחיוביות ומחזיר את האינדקס הבא בביטוי המתמטי
    return (number, end_index) if minus_counter % 2 == 0 else (number * (-1), end_index)


def insert_to_mat(mat, num, operand = None):
  if operand in power_map:
    mat[power_map[operand]].append(num)
    mat[power_map[operand]].append(operand)


def check_mat(mat, operand):
  for i in range(len(mat) - 1, power_map[operand] - 1,-1):
    if len(mat[i]) > 0:
      return i
  return -1


def calc_mat(mat, num, operand = None):
  index = check_mat(mat, operand)
  if index != -1:
    num2 = mat[index].pop(0)
    operand2 = mat[index].pop()
    new_reasult = calculate_operation(operand2, num2, num)
    calc_mat(mat, new_reasult, operand)
  else:
    insert_to_mat(mat, num, operand)


def calc(expression):
  if len(expression) == 0:
    print("the expression must not be empty")
    return None

  expression += '+0'

  mat = [
      [],
      [],
      [],
      [],
      []
  ]

  index = 0
  num, index = find_number(expression, index)

  while index < len(expression):
    op = expression[index]
    calc_mat(mat, num, op)
    check_mat(mat,op)
    index += 1
    num, index = find_number(expression, index)


  return mat[0][0]

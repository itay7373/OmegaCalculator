def find_number(expression, index=0):
    minus_counter = 0
    start_index = index

    #בודק אם יש ~ לפני המספר ומעדכן את מונה המינוסים בהתאם
    if (expression[index] == '~'):
        start_index += 1
        minus_counter = 1

    # סופר כמה מינוסים יש לפני המספר
    while (expression[start_index] == '-'):
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
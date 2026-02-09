
# функци для подсчета BMI
def calculate_bmi(weight, height):
    BMI = weight / height**2
    category = ("Ожирение", "Избыточный вес", "Нормальный вес", "Недостаточный вес")[(BMI < 30) + (BMI < 25) + (BMI < 18.5)]
    return (BMI, category)
print(calculate_bmi(100, 1.8))

print('\n')

# функция взаимодействия со строкой
def analyse_text(text):
    diff = text.split(' ')
    print('Длина строки' ,len(diff))
    print('Колличество символов' , len(text.replace(" ", "")))
    print('максимальная длина слова' , max(diff, key=len))
    print('средняя длина строки' , len(text.replace(" ", "")) / len(diff))
    print('колличество букв в верхнем регистре' , len([count for count in text if count.isupper()]))
print(analyse_text('vjif jFFFFidf jdkf'))

# генератор безопасных паролей
def generate_password(lenght, use_special=True):
    import random
    import secrets
    import string
    if lenght < 8:
        print('длина кода должна быть ольше 8')
        return
    

    password=[]
    password = [secrets.choice(string.ascii_lowercase) for a in range(2)] + [secrets.choice(string.ascii_uppercase) for a in range(2)]
    password += [secrets.choice(string.digits) for a in range(2)]
    if use_special == True:
        password +=  [secrets.choice("!@#$%^&*") for a in range(2)]
        nedostatoch= lenght - 8
        dopchisla= ''.join(secrets.choice(string.ascii_letters + string.digits + "!@#$%^&*") for _ in range(nedostatoch))
    else:
        nedostatoch= lenght - 6
        dopchisla= ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(nedostatoch))

    password += dopchisla

    secrets.SystemRandom().shuffle(password)



    digits = any( i.isdigit() for i in password )
    letter = any( i.isascii() for i in password )
    speeec= "!@#$%^&*"
    special = any(i in speeec for i in password)
    svag = []
    if letter == True: 
        category = "слабый"
    if all([digits, letter]):
        category = "средний"
    if all([digits, letter,special]):
        category = "хороший"
    if (all([digits, letter,special])) and lenght > 14:
        category = "отличный"
    if (all([digits, letter,special])) and lenght > 16:
        category = "превосходный"
    
    password=''.join(password)
    
    return(password,category)

print(generate_password(17, True))

def validate_expression(expression):
    import re
    
    matemat = all(i in (' 0123456789+-=()*/.') for i in expression)
    if matemat == False: 
        print('не математическая конструкция') 
        return
    elif (any(expression[i] in "-+=/" and expression[i+1] in "-+=/" for i in range(len(expression)-1) )):
        print("есть ошибка в двойно   операторе в констркуции")
    
    if expression.count('(') != expression.count(')'):
        print('нет закрывающей/зайкрывающей скобки')
        return
    

    for i in range(len(expression)-1):
        if expression[i] == '/' and expression[i+1] == '0':
            print('есть деление на ноль')
            return

    for i in range(len(expression)-2):
        if expression[i].isdigit() and expression[i+1] == ' ' and expression[i+2] == '.':
            print("ошибка в написании числа, пример: 2 .0 ")
            return
        elif expression[i].isdigit() and expression[i+1] == ' ' and expression[i+2] == '.':
            print("ошибка в написании числа, пример: 2. ")
            return
        
    if expression.count('(') != expression.count(')'):
        print('нет/не хватае закрывающей/открывающей скобки')
        return
    while expression.find('(') != -1:
        end = expression.find(')')
        start = expression.rfind('(', 0, end)
        subexpr = expression[start+1:end]
        tokens = re.findall(r'\d+\.?\d*|[+\-*/]', subexpr)
        for i, token in enumerate(tokens):
            if token not in '+-*/':
                tokens[i] = float(token) if '.' in token else int(token)
        i = 0
        while i < len(tokens):
            if tokens[i] == '*':
                tokens[i-1] = tokens[i-1] * tokens[i+1]
                del tokens[i:i+2]
            elif tokens[i] == '/':
                tokens[i-1] = tokens[i-1] / tokens[i+1]
                del tokens[i:i+2]
            else:
                i += 1 
        i = 0
        while i < len(tokens):
            if tokens[i] == '+':
                tokens[i-1] = tokens[i-1] + tokens[i+1]
                del tokens[i:i+2]
            elif tokens[i] == '-':
                tokens[i-1] = tokens[i-1] - tokens[i+1]
                del tokens[i:i+2]
            else:
                i += 1
        result = str(tokens[0])
        expression = expression[:start] + result + expression[end+1:]
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expression)
    for i, token in enumerate(tokens):
        if token not in '+-*/':
            tokens[i] = float(token) if '.' in token else int(token)
    i = 0
    while i < len(tokens):
            if tokens[i] == '*':
                tokens[i-1] = tokens[i-1] * tokens[i+1]
                del tokens[i:i+2]
            elif tokens[i] == '/':
                tokens[i-1] = tokens[i-1] / tokens[i+1]
                del tokens[i:i+2]
            else:
                i += 1
    i = 0
    while i < len(tokens):
            if tokens[i] == '+':
                tokens[i-1] = tokens[i-1] + tokens[i+1]
                del tokens[i:i+2]
            elif tokens[i] == '-':
                tokens[i-1] = tokens[i-1] - tokens[i+1]
                del tokens[i:i+2]
            else:
                i += 1
    return str(tokens[0])


print(validate_expression(expression ="(2 + 3) * 4 - 5 / (6 + 1)"))    
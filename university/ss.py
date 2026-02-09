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
        end = expression.find(')')
        start = expression.rfind('(', 0, end)
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
    return str(tokens[0]) if tokens else expression


print(validate_expression(expression ="(2 + 3) * 4 - 5 / (6 + 1)"))
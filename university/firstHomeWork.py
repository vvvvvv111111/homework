
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

import json
with open("library.json", "r", encoding='utf-8') as file:
    library_json = json.load(file)

def add_book(name, author, year, genre):
        with open("library.json", "r", encoding='utf-8') as file:
            library_json = json.load(file)
        for i in library_json["Library"]["book"]:
            if i["name"] == name:
                 print("Такая книга уже есть в библиотеке")
                 return

        newbook= [
        {
                "name": name,
                "author": author,
                "genre": genre,
                "year": year,
            }
        ]
        library_json["Library"]["book"].append(newbook[0])
        with open('library.json', 'w', encoding='utf-8') as file:
            json.dump(library_json, file, ensure_ascii=False, indent=4)
        print("Книга", name, "добавлена в библиотеку")

def remove_book(name):
    with open("library.json", "r", encoding='utf-8') as file:
        library_json = json.load(file)
    for i in library_json["Library"]["book"]:
        if i["name"] == name:
            print("книга", name,"найдена")
    staroe = library_json["Library"]["book"]
    library_json["Library"]["book"] = [i for i in library_json["Library"]["book"] if i["name"] != name ]
    with open('library.json', 'w', encoding='utf-8') as file:
        json.dump(library_json, file, ensure_ascii=False, indent=4)
    if staroe == library_json["Library"]["book"]:
        print("книга не найдена")
    else: print('книга', name,'удалена') 


def find_books_by_genre(genre):
    with open("library.json", "r", encoding='utf-8') as file:
        library_json = json.load(file)
    count = 0
    for i in library_json["Library"]["book"]:
        if i["genre"] == genre:
            print(i["name"])
            count += 1
    if count == 0: 
        print("книг с таким жанром не найдено")

def find_books_by_author(author):
    with open("library.json", "r", encoding='utf-8') as file:
        library_json = json.load(file)
    count = 0
    for i in library_json["Library"]["book"]:
        if i["author"] == author:
            print(i["name"])
            count += 1
    if count == 0: 
        print("книг с таким автором нет")

def get_books_published_after(year):
    with open("library.json", "r", encoding='utf-8') as file:
        library_json = json.load(file)
    count = 0
    for i in library_json["Library"]["book"]:
        if int(i["year"]) >= year:
            print(i["name"])
            count += 1
    if count == 0: 
        print("книг после этого года не найдено")

def get_library_statistics():
    with open("library.json", "r", encoding='utf-8') as file:
        library_json = json.load(file)
    count = 0
    for i in library_json["Library"]["book"]:
        count += 1
    print("всего книг в библиотеке", count)
    count = 0
    staroe = "nachalo"
    for i in library_json["Library"]["book"]:
        swag = int(i["year"])
        if staroe == "nachalo": staroe = swag
        if staroe > swag:
            staroe = swag
    print("самая старая книга выпущина в",staroe)
    autori = []
    for i in library_json["Library"]["book"]:
        authorr = i["author"]
        if authorr not in autori:
            autori.append(authorr)
    print("Авторы:", autori) 

    ganri = []
    for i in library_json["Library"]["book"]:
        ganr = i["genre"]
        ganri.append(ganr)

    genre_count = {}
    for book in library_json["Library"]["book"]:
        genre = book["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    if genre_count:
        most_popular = max(genre_count, key=genre_count.get)
        print("Самый популярный жанр:",most_popular, "книг", genre_count[most_popular])
                
   

               
          

          



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
    
    return(password,category)

print(generate_password(17, True))
    
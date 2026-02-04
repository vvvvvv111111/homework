
# функци для подсчета BMI
def calculate_bmi(weight, height):
    BMI = weight / height**2
    category = ("Недостаточный вес", "Нормальный вес", "Избыточный вес", "Ожирение")[(BMI < 18.5)+(BMI < 25) + (BMI < 30)]
    return (BMI, category)
print(calculate_bmi(67, 67))

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
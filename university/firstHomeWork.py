
def calculate_bmi(weight, height):
    BMI = weight / height**2
    if BMI < 18.5:
        category = 'Недостаточный вес'
    else:
        if BMI < 25:
            category = 'Нормальный вес'
        else:
            if BMI < 30:
                category = 'Избыточный вес'
            else:
                category = 'Ожирение'
    return (BMI, category)


print(calculate_bmi(67, 67))

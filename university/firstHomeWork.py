
def calculate_bmi(weight, height):
    BMI = weight / height**2
    category = ("Недостаточный вес", "Нормальный вес", "Избыточный вес", "Ожирение")[(BMI < 18.5)+(BMI < 25) + (BMI < 30)]
    return (BMI, category)
print(calculate_bmi(67, 67))

import json

class item: 
    check = ["оружие", "зелье" , "броня"]
    def __init__(self, name: str, type: str, weight: float, value: float):
        if type not in self.check:
            print("такого типа предмета не существует, есть только: оружие, зелье, броня")
            return
        self.name = name
        self.data= [type, weight, value]

    def description(self):
        print(self.data)
    def use(self):
        pass
class inventory:

    def __init__(self,player: player, max_weight):
        self.player = player
        self.max_weight = max_weight
        self.weight = 0
        self.items = {}
        pass
    def podschet_weight(self):
        with open("inventory.json","r", encoding="utf-8") as file:
                self.player.data = json.load(file)
        self.weight = 0
        for i in self.player.data[self.player.name]:
            self.weight += self.player.data[self.player.name][i][1]
        print(self.weight)
        return self.weight
        
    def add_item(self, item):
            with open("inventory.json","r", encoding="utf-8") as file:
                self.player.data = json.load(file)
            if self.weight + item.data[1] < self.max_weight:
                self.player.data[self.player.name][item.name] = item.data
                self.weight += item.data[1]
            else: print("инвентарь будет перегружен, не хватает:", item.data[1] - (self.max_weight - self.weight), " кг")
            with open("inventory.json","w", encoding="utf-8") as file:
                json.dump(self.player.data, file, ensure_ascii=False, indent=4)
    def remove_item(self,item: item):
        with open("inventory.json","r", encoding="utf-8") as file:
            self.player.data = json.load(file)
        s = self.player.data[self.player.name]
        self.player.data[self.player.name] = {i: s[i] for i in s if i != item.name}
        with open("inventory.json","w", encoding="utf-8") as file:
            json.dump(self.player.data, file, ensure_ascii=False, indent=4)
    def find_by_type(self, type: str):
        with open("inventory.json","r", encoding="utf-8") as file:
            self.player.data = json.load(file)
        for i in self.player.data[self.player.name]:
            if type in self.player.data[self.player.name][i][0]:
                print(i)
        with open("inventory.json","w", encoding="utf-8") as file:
            json.dump(self.player.data, file, ensure_ascii=False, indent=4)
    def inventory_value(self):
        with open("inventory.json","r", encoding="utf-8") as file:
            self.player.data = json.load(file)
        value = 0
        for i in self.player.data[self.player.name]:
            value += self.player.data[self.player.name][i][2]
        print(value)
        with open("inventory.json","w", encoding="utf-8") as file:
            json.dump(self.player.data, file, ensure_ascii=False, indent=4)
    def mostvalue(self):
        with open("inventory.json","r", encoding="utf-8") as file:
            self.player.data = json.load(file)
        value = 0
        name = ""
        for i in self.player.data[self.player.name]:
            if value < self.player.data[self.player.name][i][2]:
                value = self.player.data[self.player.name][i][2]
                name = i
        print("самый дорогой предмет:", name, "стоимость:", value)
        with open("inventory.json","w", encoding="utf-8") as file:
            json.dump(self.player.data, file, ensure_ascii=False, indent=4)

class player:
    def __init__(self, name: str,helth: float, money: float,max_weight):
        self.name= name
        self.helth = helth
        self.money = money
        with open("inventory.json","r", encoding="utf-8") as file:
            content = file.read()
            if content.strip(): 
                self.data = json.loads(content)
            else:  
                self.data = {}
        if name in self.data:
            items = self.data[name]
        else:
            items = {}
            self.data[name] = items
    
        self.inventory = inventory(self, max_weight)
        self.inventory.items = items
        with open("inventory.json","w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
    
    def take(self, item: item):
        self.inventory.add_item(item)
    def sell(self,item: item):
        self.money += self.inventory.items[item.name][2]
        self.inventory.remove_item(item)
    def show_item(self):
        for i in self.inventory.items:
            print(i)


        



# Создаем игрока
print("=== СОЗДАНИЕ ИГРОКА ===")
hero = player("Артур", 100, 500, 20)
print(f"Игрок: {hero.name}")
print(f"Здоровье: {hero.helth}")
print(f"Деньги: {hero.money}")
print(f"Макс. вес инвентаря: {hero.inventory.max_weight}")
print()

# Создаем предметы
print("=== СОЗДАНИЕ ПРЕДМЕТОВ ===")
sword = item("Экскалибур", "оружие", 3.5, 1000)
potion = item("Зелье здоровья", "зелье", 0.2, 50)
armor = item("Стальная броня", "броня", 8, 500)
shield = item("Щит", "броня", 4, 300)
apple = item("Яблоко", "зелье", 0.1, 5)

print(f"Создан меч: {sword.name}, вес: {sword.data[1]}, цена: {sword.data[2]}")
print(f"Создано зелье: {potion.name}, вес: {potion.data[1]}, цена: {potion.data[2]}")
print(f"Создана броня: {armor.name}, вес: {armor.data[1]}, цена: {armor.data[2]}")
print()

# Добавляем предметы в инвентарь
print("=== ДОБАВЛЕНИЕ ПРЕДМЕТОВ ===")
hero.take(sword)
hero.take(potion)
hero.take(armor)
hero.take(shield)  # Пытаемся добавить щит (вес должен превысить лимит)
print()

# Показываем инвентарь
print("=== ИНВЕНТАРЬ ===")
hero.show_item()
print()

# Подсчитываем вес
print("=== ВЕС ИНВЕНТАРЯ ===")
hero.inventory.podschet_weight()
print()

# Ищем предметы по типу
print("=== ПОИСК ПО ТИПУ ===")
print("Поиск оружия:")
hero.inventory.find_by_type("оружие")
print("Поиск брони:")
hero.inventory.find_by_type("броня")
print()

# Считаем стоимость инвентаря
print("=== СТОИМОСТЬ ИНВЕНТАРЯ ===")
hero.inventory.inventory_value()
print()

# Находим самый дорогой предмет
print("=== САМЫЙ ДОРОГОЙ ПРЕДМЕТ ===")
hero.inventory.mostvalue()
print()

# Продаем предмет
print("=== ПРОДАЖА ПРЕДМЕТА ===")
print(f"Денег до продажи: {hero.money}")
hero.sell(potion)
print(f"Денег после продажи зелья: {hero.money}")
print()

# Проверяем инвентарь после продажи
print("=== ИНВЕНТАРЬ ПОСЛЕ ПРОДАЖИ ===")
hero.show_item()
print()

# Создаем второго игрока для проверки мультипользовательности
print("=== ВТОРОЙ ИГРОК ===")
hero2 = player("Геральт", 150, 1000, 30)
print(f"Игрок: {hero2.name}")
print(f"Здоровье: {hero2.helth}")
print(f"Деньги: {hero2.money}")
print()

# Добавляем предметы второму игроку
print("=== ДОБАВЛЕНИЕ ПРЕДМЕТОВ ВТОРОМУ ИГРОКУ ===")
hero2.take(shield)
hero2.take(apple)
hero2.show_item()
print()

# Показываем финальное состояние JSON
print("=== СОДЕРЖИМОЕ JSON ФАЙЛА ===")
with open("inventory.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(json.dumps(data, ensure_ascii=False, indent=2))
    
class Inventory:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []
    
    # Реализуйте магические методы ниже
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return f"max size is {self.max_size}, items: {" ".join(self.items)}"
    
    def __repr__(self):
        return f"max size is {self.max_size}, items: {len(self.items)}"
    
    # Дополнительные методы
    def add_item(self, item):
        if self.max_size == len(self.items):
            False
        else: 
            self.items += item



    
    
    def remove_item(self, item):
        nov = []
        for i in self.items:
            if i != item:
                nov.append(i)
        self.items = nov


# Тестовые примеры (раскомментируйте после реализации)
inv = Inventory(max_size=5)
inv.add_item("Меч")
inv.add_item("Щит")
inv.add_item("Зелье")
print(len(inv))
print(str(inv))
print(repr(inv))
inv.remove_item("Щит")
print(len(inv))
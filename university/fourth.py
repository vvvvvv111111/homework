class AlarmClock:
    def __init__(self, current_time: str, alarm_time: str):
        self._current_time = current_time
        self._alarm_time = alarm_time
        self._validate_time(self._current_time)
        self._validate_time(self._alarm_time)

    @staticmethod
    def _validate_time(value: str):
        if not isinstance(value, str):
            print("Ошибка: время должно быть строкой в формате HH:MM")
            return False
        if len(value) != 5 or value[2] != ":":
            print("Ошибка: неверный формат времени. Используйте HH:MM")
            return False

        hours = value[:2]
        minutes = value[3:]
        if not (hours.isdigit() and minutes.isdigit()):
            print("Ошибка: неверный формат времени. Используйте HH:MM")
            return False
        
        hour_value = int(hours)
        minute_value = int(minutes)
        if not (0 <= hour_value <= 23 and 0 <= minute_value <= 59):
            print("Ошибка: неверный формат времени. Используйте HH:MM")
            return False

        return True
    @property
    def time(self):
        return self._current_time
    @time.setter
    def time(self, value: str):
        if self._validate_time(value):
            self._current_time = value
            
    @property
    def alarm_time(self):
        return self._alarm_time
    def set_time(self, time: str):
        self.time = time
    def set_alarm(self, time: str):
        if self._validate_time(time):
            self._alarm_time = time
    def check_alarm(self):
        return self.time == self._alarm_time
    
chasi = AlarmClock("07:00", "07:30")
print(chasi.time)  
print(chasi.alarm_time) 
chasi.set_time("07:30")
print(chasi.check_alarm())


class LibraryBook:
    _id = 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._status = "доступна"
        self.__book_id = LibraryBook._id
        LibraryBook.id += 1

    @property
    def status(self):
        return self._status

    def get_book(self):
        if self._status == "выдана":
            print("Книга уже выдана")
            return False
        self._status = "выдана"
        print("Книга выдана")
        return True
    def return_book(self):
        if self._status == "доступна":
            print("Книга уже в библиотеке")
            return False
        self._status = "доступна"
        print("Книга возвращена")
        return True
    def get_info(self):
        return (
            f"ID: {self.__book_id}, Автор: {self.author}, "
            f"Название: {self.title}, Статус: {self.status}"
        )

    @classmethod
    def from_string(cls, data):
        parts = data.split(" - ")
        if len(parts) != 2:
            print("Неверный формат. Используйте: Автор - Название")
            return None

        author = parts[0].strip()
        title = parts[1].strip()
        if author == "" or title == "":
            print("Автор и название не должны быть пустыми")
            return None
        return cls(title, author)


book1 = LibraryBook("1984", "Джордж Оруэлл")
print(book1.get_info())
book1.get_book()
print(book1.get_info())
book1.return_book()
print(book1.get_info())

book2 = LibraryBook.from_string("Рэй Брэдбери - 451 градус по Фаренгейту")
print(book2.get_info())
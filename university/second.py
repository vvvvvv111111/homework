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
                
   

               
          

          


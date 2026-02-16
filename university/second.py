data = [
    "Ivan,Math,78",
    "Anna,Math,92",
    "Ivan,Physics,85",
    "Anna,Physics,90",
    "Ivan,Math,81"
]


def analyze_students(data):
    students = {}
    for i in data:
        name, subject, score = i.split(',')
        score = int(score)
        if name not in students:
            students[name] = {}
        if subject not in students[name]:
            students[name][subject] = []
        students[name][subject].append(score)
    print(students)
    
    
    for a in students:
        summa = 0
        kolvo = 0
        for i in students[a]:
            summa += sum(students[a][i]) / len(students[a][i])
            kolvo += 1
        summa = summa / kolvo
        print("средний балл студента", a , "это", summa)
    for a in students:
        maxx = 0
        for i in students[a]:
            if maxx < max(students[a][i]):
                maxx = max(students[a][i])
        print("лучший балл студента", a, "это", maxx)
    subjectaverages = {}
    for a in students:
        for i in students[a]:
            avgscore = sum(students[a][i]) / len(students[a][i])
            if i not in subjectaverages:
                subjectaverages[i] = []
            subjectaverages[i].append(avgscore)
    worstsubject = min(subjectaverages, key=subjectaverages.get)
    worstscore = sum(subjectaverages[worstsubject]) / len(subjectaverages[worstsubject])
    
    print("Самый неудавшийся предмет:", worstsubject, "со средним баллом", worstscore)

analyze_students(data)
tasks = ["нет задач"]
def tasks_queue(tasks):
    print("\n        Программа *TASKS*\n\n", 
          "           первая задача:",tasks[0],
    """\n
            список возможных команд:

            1) add
            2) next
            3) list
            4) priority
            5) exit
        
        Введите команду:
    """
    )
    komand=""
    komand =input(komand)
    if komand == "1":
        print("Введите задачу")
        zadacha = "" 
        zadacha = input(zadacha)
        add(tasks,zadacha) 
    elif komand == "2":
        next(tasks)
    elif komand == "3":
        list(tasks)
    elif komand == "4":
        if tasks[0] != "нет задач":
            nomer = ""
            print("напишите номер какой задачи вы хотите поставить в приоритет")
            nomer = input(nomer)
            priority(tasks, nomer)
        else: 
            print("задач нет")
            tasks_queue(tasks)
    elif komand == "5":
        print("Выход из программы")
        return tasks
    else: 
        print("такой команды нет")
        tasks_queue(tasks)
    return tasks

def add(tasks, zadacha):
    if tasks[0] == "нет задач":
        tasks[0] = zadacha
    else:   tasks.append(zadacha)
    print("Задача добавлена")
    return tasks_queue(tasks)
def next(tasks):
    if tasks[1] == None:
        print("следующей задачи нет")
    else: del tasks[0]
    return tasks_queue(tasks)
def list(tasks):
    if tasks[0] != "нет задач":
        print("Список задач:\n")
        nomer = 1
        for i in tasks:
            print(nomer,")",i, "\n")
            nomer +=1
    else: print("Нет задач")
    return tasks_queue(tasks)
def priority(tasks, nomer):
    nomer = int(nomer) - 1
    if nomer == 0: 
        print("задача уже в приоритете")
        return tasks_queue(tasks)
    zadacha = tasks.pop(nomer)
    tasks.insert(0, zadacha) 
    print("задача", zadacha, "теперь в приоритете")
    return tasks_queue(tasks)





    

tasks_queue(tasks)
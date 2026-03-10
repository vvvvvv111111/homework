class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_sinfo(self):
        print("Name:", self.name, "Salary:", self.salary)

class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_sinfo(self):
        super().get_sinfo()
        print("Department:", self.department)

class Developer(employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_sinfo(self):
        super().get_sinfo()
        print("Programming Language:", self.programming_language)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount, "New Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawn:", amount, "New Balance:", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print("Interest:", interest)

    def withdraw(self, amount):
        if amount * 0.9 > self.balance:
            print(f"Insufficient funds, you can only withdraw {self.balance * 0.9}")
        else:
            self.balance -= amount
            print("Withdrawn:", amount, "New Balance:", self.balance)

class Apliance:
    def __init__(self, power_consumption, conect_now):
        self.power_consumption = power_consumption
        self.conect_now = conect_now

    def turn_on(self):
        print("Appliance is turned on")

class Refrigerator(Apliance):
    def __init__(self, status):
        self.status = status

    def turn_on(self):
        if Apliance.power_consumption == Apliance.conect_now:
            super().turn_on()
            Apliance.conect_now += Apliance.conect_now
        else:
            print("Not enough power to turn on the refrigerator")
        

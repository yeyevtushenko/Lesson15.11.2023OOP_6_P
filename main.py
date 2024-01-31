class Employer:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display_info(self, position):
        return f"{self.name} is a {self.sex} and has {self.age} years old. He/She is a {position}"

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

    def __int__(self):
        return self.age

class President(Employer):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def display_info(self):
        return super().display_info("president")

class Manager(Employer):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def display_info(self):
        return super().display_info("manager")

class Worker(Employer):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def display_info(self):
        return super().display_info("worker")

president = President("Clinton", "male", 65)
manager = Manager("Tomas", "male", 33)
worker = Worker("Anna", "female", 25)

print(str(president))
print(int(manager))
print(worker.display_info())
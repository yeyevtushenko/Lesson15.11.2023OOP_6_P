class Employer:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display_info(self, position):
        print(f"{self.name} is a {self.sex} and has {self.age} years old. He/She is a {position}")

class President(Employer):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def display_info(self):
        super().display_info("president")

class Manager(Employer):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def display_info(self):
        super().display_info("manager")

class Worker(Employer):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)

    def display_info(self):
        super().display_info("worker")

president = President("Clinton", "male", 65)
manager = Manager("Tomas", "male", 33)
worker = Worker("Anna", "female", 25)

president.display_info()
manager.display_info()
worker.display_info()
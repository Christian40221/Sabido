class Animal:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display_info(self):
        print(f"Name: {self.name} {self.age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    def display_breed(self):
        print(f"Breed: {self._breed}")

    def update_age(self, new_age):
        self._age = new_age

dog1 = Dog ("Buck", 3, "German Sheperd")

Dog.display_info()
Dog.display_breed()
Dog.update_age(12)
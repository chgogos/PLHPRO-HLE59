class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, lazy_level=10):
        # super().__init__(name)
        self.lazyness = lazy_level
        
    def make_sound(self):
        return "Meow!"

def make_animals_speak(animals):
    for animal in animals:
        print(f"{animal.make_sound()}")

dog = Dog("Fido")
cat = Cat("felix", 7)

make_animals_speak([dog, cat])

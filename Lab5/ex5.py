
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        print(f"{self.name} lives in {self.habitat}")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth.")

class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def fly(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def __init__(self, name, habitat, water_type):
        super().__init__(name, habitat)
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} is swimming with Nemo.")

def main():
    mammal = Mammal(name="Lion", habitat="Savannah", fur_color="Golden")
    mammal.display_info()
    mammal.give_birth()
    mammal.eat()

    bird = Bird(name="Eagle", habitat="Mountains", feather_color="Brown")
    bird.display_info()
    bird.fly()
    bird.sleep()

    fish = Fish(name="Clownfish", habitat="Aquarium", water_type="Saltwater")
    fish.display_info()
    fish.swim()

if __name__ == "__main__":
    main()
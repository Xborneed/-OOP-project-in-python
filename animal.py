#creating class with animals

class Cheetah:
    def move(self):
        print("Running")

class Lion:
    def move(self):
        print("Walking")

class Elephant:
    def move(self):
        print("Stomping")

class Bird:
    def move(self):
        print("Flying")

class Fish:
    def move(self):
        print("Swimming")

animals = [Cheetah(), Lion(), Elephant(), Bird(), Fish()]
for animal in animals:
    animal.move()
        
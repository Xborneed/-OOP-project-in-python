#creating a class known as superHero
# Base class
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self.__power_level = power_level  # Private attribute

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}!")

    def get_power_level(self):
        return self.__power_level

    def use_power(self):
        print(f"{self.alias} uses a generic power.")

# Subclass: FlyingHero
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.alias} takes off and flies through the sky! ")

# Subclass: StrongHero
class StrongHero(Superhero):
    def use_power(self):
        print(f"{self.alias} lifts a car with ease!")

# Create objects
skyhawk = FlyingHero("Liam Cole", "Skyhawk", 85)
ironfist = StrongHero("Maya Tan", "Ironfist", 90)

# Use methods
skyhawk.introduce()
skyhawk.use_power()
print("Power Level:", skyhawk.get_power_level())

print()

ironfist.introduce()
ironfist.use_power()
print("Power Level:", ironfist.get_power_level())

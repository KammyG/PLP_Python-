class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.__health = health  # encapsulated (private)

    def get_health(self):
        return f"{self.name}'s health: {self.__health}"
    
    def attack(self):
        return f"{self.name} uses {self.power}!"
    
    def take_damage(self, damage):
        self.__health = max(0, self.__health - damage)
        return f"{self.name} takes {damage} damage. Health is now {self.__health}."


# Child Class 1: Flying Hero
class FlyingHero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    # Polymorphism (override attack)
    def attack(self):
        return f"{self.name} swoops down at {self.flight_speed} km/h using {self.power}! 🦅"


# Child Class 2: Strength Hero
class StrongHero(Superhero):
    def __init__(self, name, power, health, strength_level):
        super().__init__(name, power, health)
        self.strength_level = strength_level

    # Polymorphism (override attack)
    def attack(self):
        return f"{self.name} smashes with strength level {self.strength_level}! 💪"


# -------------------------------
# Test the Classes
# -------------------------------
if __name__ == "__main__":
    hero1 = FlyingHero("Falcon", "Wind Strike", 100, 300)
    hero2 = StrongHero("Titan", "Earthquake Punch", 150, 900)

    print(hero1.attack())
    print(hero1.take_damage(30))
    print(hero1.get_health())

    print(hero2.attack())
    print(hero2.take_damage(50))
    print(hero2.get_health())

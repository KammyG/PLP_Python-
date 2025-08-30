# Base Class
class Vehicle:
    def move(self):
        return "Vehicle is moving"


# Child Class 1: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"


# Child Class 2: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"


# Child Class 3: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🛳️"


# Child Class 4: Horse (not a vehicle, but still moves!)
class Horse(Vehicle):
    def move(self):
        return "Galloping on land 🐎"


# -------------------------------
# Test Polymorphism
# -------------------------------
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Horse()]

    for v in vehicles:
        print(v.move())

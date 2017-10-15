import random


class Animal:
    # constructor
    def __init__(self, food_need, water_need):
        # weight represents growth of animal
        self._weight = random.randint(1,3)
        self._days_growing = 0
        self._growth_rate = 1
        self._food_need = food_need
        self._water_need = water_need
        self._status = "new-born"
        self._type = "normal"
        self._name = "name"
        self.health = int((random.triangular()*10))

    def report(self):
        age = round(self._days_growing//365.25, 1)
        return {'type': self._type, 'status': self._status, 'growth': self._weight, 'days growing': self._days_growing, 'age': age}

    def update_status(self):
        age = round(self._days_growing / 365.25, 1)
        if age > 15:
            self._status = 'senile'
        elif age > 10:
            self._status = 'mature'
        elif age > 5:
            self._status = 'adolescent'
        elif age >= 0:
            self._status = 'calf'
        elif age == 0:
            self._status = 'new-born'

    def needs(self):
        return {'food_need': self._food_need, 'water_need': self._water_need}

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
            self._days_growing += 1

    # will try to have auto grow and manual grow in the class
    def auto_grow(self, days):
        for i in range(days):
            self.grow(random.randint(1, 10), random.randint(1, 10))
            self.update_status()

    def manual_grow(self):
        valid = False
        while not valid:
            try:
                food = input("food (1-10): ")
                if 0 < food <= 10:
                    valid = True
                else:
                    print("Invalid: please enter a value between 1 and 10")
            except ValueError:
                print("Invalid: please enter a number")
        valid = False
        while not valid:
            try:
                water = input("food (1-10): ")
                if 0 < water <= 10:
                    valid = True
                else:
                    print("Invalid: please enter a value between 1 and 10")
            except ValueError:
                print("Invalid: please enter a number")
        self.grow(food, water)

# test code
def main():
    # generate animal
    generic_animal = Animal(5, 5)
    # report
    print(generic_animal.report())
    # grow for one day




if __name__ == "__main__":
    main












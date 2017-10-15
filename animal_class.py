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
        # triangular generates a bell curve random distribution
        self.health = int((random.triangular()*10))
        # automatically grows one day
        self.grow(10, 10)

    def report(self):
        age = round(self._days_growing//365.25, 1)
        if self.health > 0:
            return {'type': self._type, 'status': self._status, 'growth': self._weight, 'days growing': self._days_growing, 'age': age}
        else:
            return "away on vacation"


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
        # if the animal
        if self.health < 0:
            # Holy meow, guys - that's so dark. Why would you add this???
            print("this animal has been located to a nice farm in the countryside")

        # if the animal has enough health to continue
        elif food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1

    # will try to have auto grow and manual grow in the class

    # It would be ideal if the days were actually input inside to allow for validation
    # but it's just easier for testing at the moment
    def auto_grow(self, days):
        for i in range(days):
            self.grow(random.randint(1, 10), random.randint(1, 10))
            self.update_status()

    def manual_grow(self):
        valid = False
        while not valid:
            try:
                food = int(input("food (1-10): "))
                if 0 < food <= 10:
                    valid = True
                else:
                    print("Invalid: please enter a value between 1 and 10")
            except ValueError:
                print("Invalid: please enter a number")
        valid = False
        while not valid:
            try:
                water = int(input("food (1-10): "))
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

    # let's manually grow it
    generic_animal.manual_grow()
    # report
    print(generic_animal.report())

    # auto grow- 6 months
    generic_animal.auto_grow(30*3)
    # report
    print(generic_animal.report())

    # auto grow- a year
    generic_animal.auto_grow(366)
    # report
    print(generic_animal.report())





if __name__ == "__main__":
    main()












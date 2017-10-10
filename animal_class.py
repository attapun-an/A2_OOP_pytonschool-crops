class Animal():
    # constructor
    def __init__(self, food_need, water_need):
        # weight represents growth of animal
        self._weight = 2
        self._days_growing = 0
        self._growth_rate = 1
        self._food_need = food_need
        self._water_need = water_need
        self._status = "new-born"
        self._type = "normal"
        self._name = "name"

    def report(self):
        return {'type': self._type, 'status': self._status, 'growth': self._weight, 'days growing':  'age': round(self._days_growing//365.25, 1)}

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
            self.update_status()




dog = Animal(2, 2)
print(dog.report())
dog.grow(3, 3)
print(dog.report())


import random


class Crop:
    """A generic food crop"""

    # the line above is a doc string (gives python info about what the class does)

    # constructor (method that runs automatically to instantiate the class)
    def __init__(self, growth_rate, light_need, water_need):
        # set the attributes with initial value
        """self allows it to refer to itself; thus allow us change values within
         it's attributes within different methods"""
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "seed"
        self._type = "generic"

        # attributes with ._ are considered private (can only be accessed by methods)
        # which means they can't be accessed directly from outside the class

        """ if it's something that can generally be changed - then it's okay being 
        public, but if it's something that your methods deal with anyways have it private...
        
        If someone just came in, and changed your height .. 
        but someone can change your diet, and how much food you eat - Mr. M 
        
        Name, Favourite color can be changed
        But you can't just say tommorrow I will be 2ft taller"""

    def display_status(self):
        return {"growth": self._growth, "days_growing": self._days_growing}

    # returns amount of light and water that crop requires to grow
    def needs(self):
        # returns a dictionary with light and water needs. Yay.
        return{'light need': self._light_need, 'water need': self._light_need}

    # provides overview of current state
    def report(self):
        # returns a dictionary containing type, status, growth, days growing
        return{'type': self._type, 'status': self._status, 'growth': self._growth, 'days growing': self._days_growing}

    def _update_status(self):
        current_growth = self._days_growing
        if current_growth > 15:
            self._status = "old"
        elif current_growth > 10:
            self._status = "mature"
        elif current_growth > 5:
            self._status = "young"
        elif current_growth > 0:
            self._status = "seedling"
        elif current_growth == 0:
            self._status = "seed"

    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        # increment days growing
        self._days_growing += 1
        # update status
        self._update_status()


def auto_grow(crop, days):
    for days in range (days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crop.grow(light, water)


def manual_grow(crop):
    # get light and water values
    light_check = True
    while light_check:
        try:
            light_check = int(input("light (1-10): "))
            if 0 <= light_check <= 10:
                light_check = False
        except ValueError:
            print("Invalid")

    # using the variable
    valid = False:
    while not valid





def main():
    # instantiate the class
    new_crop = Crop(2, 5, 5)
    # lets see if it works
    print(new_crop._status)
    """whoa, we just accessed a private attribute! as a programmer, it is okay for testing
    but once we compile it - that's when it truly becomes private"""
    print(new_crop._days_growing)
    print(new_crop._growth_rate)
    print(new_crop._light_need)
    print(new_crop._water_need)

    """
    new_crop2 = Crop(1, 2 , 4)
    print(new_crop2._days_growing)
    print(new_crop2._growth_rate)
    print(new_crop2._light_need)
    print(new_crop2._water_need)
    """

    print(new_crop.needs())
    print(new_crop.report())

    #printing only a portion
    print(new_crop.needs()['light need'])

    new_crop.grow(4, 4)
    print(new_crop.report())

    auto_grow(new_crop, 30)
    print(new_crop.report())

# no idea how this is different from just main(). but it looks cool
if __name__ == "__main__":
    main()

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

def main():
    # instantiate the class
    new_crop = Crop(10,5,5)
    # lets see if it works
    print(new_crop._status)
    """whoa, we just accessed a private attribute! as a programmer, it is okay for testing
    but once we compile it - that's when it truly becomes private"""

main()

from animal_class import *

class Sheep(Animal):
    """fluffy goat"""

    # constructor
    def __init__(self):
        #call parent class
        super().__init__(4, 3, 15)
        self._type = "Sheep"

sheep1 = Sheep()
print(sheep1.report())


if __name__ == "__main__":
    main()

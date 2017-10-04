from crop_class import *

class Potato(Crop):
    """a potato crop"""
    # constructor
    def __init__(self):
        # call the parent class constructor with a default value
        # growth rate = 1; light need = 3; water need = 6
        super().__init__(1, 3, 6)
        self._type = "Potato"

    # an override/polymorphism grow method for subclass
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "seedling":
                self._growth += self._growth_rate * 1.5
            elif self._status == "young":
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


def main():
    # create a new potato crop
    potato_crop = Potato()
    print(potato_crop.report())

    manual_grow(potato_crop)
    print(potato_crop.report())


"""
if __name__ == "__main__":
    main()
"""

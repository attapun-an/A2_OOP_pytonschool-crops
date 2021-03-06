from crop_class import *

class Wheat(Crop):
    """a wheat crop"""

    def __init__(self):
        # call the parent class constructor with a default value
        # growth rate = 1; light need = 3; water need = 6
        super().__init__(1, 8, 3)
        self._type = "Wheat"

    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "seedling":
                self._growth = self._growth + self._growth_rate * 1.5
            elif self._status == "young":
                self._growth = self._growth + self._growth_rate * 1.25
            elif self._status == "old":
                self._growth = self._growth + self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


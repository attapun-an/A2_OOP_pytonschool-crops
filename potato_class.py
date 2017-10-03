from crop_class import *

class Potato(Crop):
    """a potato crop"""
    # constructor
    def __init__(self):
        # call the parent class constructor with a default value
        # growth rate = 1; light need = 3; water need = 6
        super().__init__(1, 3, 6)
        self._type = "Potato"


def main():
    # create a new potato crop
    potato_crop = Potato()
    print(potato_crop.report())

    manage_crop(potato_crop)
    print(potato_crop.report())


main()
"""
if __name__ == "__main__":
    main()
"""

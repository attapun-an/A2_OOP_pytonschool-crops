from wheat_class import *
from potato_class import *


def select(min_val, max_val):
    valid = False
    while not valid:
        try:
            user_input = int(input("""please select option: """))
            if min_val <= user_input <= max_val:
                valid = True
            else:
                print("Please enter value between {0} and {1} (inclusive)".format(min_val, max_val))
        except ValueError:
            print("Please enter a number between {0} and {1} (inclusive)".format(min_val, max_val))
    return user_input

# function is redundant
def display_main_menu():
    print("""
    1) Create Crop
    2) Manage Crop
    
    0) Exit Program""")

def display_crop_select_menu():
    print("""
    Select your crop:
    1) Potato
    2) Wheat
    """)

def create_crop():
    choice = select(1, 2)
    if choice == 1:
        thisCrop = Potato()
    elif choice == 2:
        thisCrop = Wheat()
    return thisCrop


def main():
    display_crop_select_menu()
    this_crop = create_crop()

    manage_crop(this_crop)

main()


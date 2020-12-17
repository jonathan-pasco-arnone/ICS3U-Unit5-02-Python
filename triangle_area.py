#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program calculates the area of a triangle

def area_of_triangle(base, height):
    # calculate area

    area = base * height / 2

    print("The area is {}cm²".format(area))


def main():
    # This function calls gets inputs, checks them for errors and
    # calls the specified functions

    print("")
    print("This program calculates the area of a triangle")
    print("")
    print("Please input the base and height")
    print("")
    base_from_user_str = input("Base: ")
    print("")
    height_from_user_str = input("Height: ")
    print("")

    try:
        base_from_user = int(base_from_user_str)
        height_from_user = int(height_from_user_str)
    except Exception:
        print("Please enter a real base and height")
    else:
        if base_from_user > 0 and height_from_user > 0:
            area_of_triangle(base_from_user, height_from_user)
        else:
            print("Please enter positive values for base and height")


if __name__ == "__main__":
    main()

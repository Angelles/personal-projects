import math

###
# The purpose of this program is to calculate the unknown side length of a triangle, or x, based on the Law of Cosines.
# In the Law of Cosines, for a triangle, side a equals the square root of the following:
# the sum of side b squared and c squared multiplied by 2 multiplied by sides b and c. In other words,
# side_a = math.sqrt((b**2) + (c**2)-2 * (b * c) * math.cos(math.radians(a_angle)))
# The formulas to get the length of sides b and c follow a similar pattern. This program allows the user to get the
# length of sides a, b, or c.
###

# VARIABLES


def var_a():
    variable_a = float(input("Enter side a.\n"))
    return variable_a


def var_b():
    variable_b = float(input("Enter side b.\n"))
    return variable_b


def var_c():
    variable_c = float(input("Enter side c.\n"))
    return variable_c


def angle_a():
    a = float(input("Enter angle A in degrees.\n"))
    return a


def angle_b():
    b = float(input("Enter angle B in degrees.\n"))
    return b


def angle_c():
    c = float(input("Enter angle C in degrees.\n"))
    return c


# Find side a with Law of Cosines.
def calculate_side_a():
    # Get inputs.
    b = var_b()
    c = var_c()
    a_angle = angle_a()
    # Calculate side a with the Law of Cosines formula.
    side_a = math.sqrt((b**2) + (c**2)-2 * (b * c) * math.cos(math.radians(a_angle)))
    print("The answer is:", side_a)


# Find side b with Law of Cosines.
def calculate_side_b():
    # Get inputs.
    a = var_a()
    c = var_c()
    b_angle = angle_b()
    # Calculate side b with the Law of Cosines formula.
    side_b = math.sqrt((a**2) + (c**2)-2 * (a * c) * math.cos(math.radians(b_angle)))
    print("The answer is:", side_b)


# Find side C with Law of Cosines.
def calculate_side_c():
    # Get inputs.
    a = var_a()
    b = var_b()
    c_angle = angle_c()
    # Calculate side c with the Law of Cosines formula.
    side_c = math.sqrt((a**2) + (b**2)-2 * (a * b) * math.cos(math.radians(c_angle)))
    print("The answer is:", side_c)


# Use a conditional statement in a function to choose the correct function to solve the problem.
def find_side():
    sides = ["a", "b", "c"]
    question = input("Enter the lowercase letter for the side you are trying to find.\n")
    for i in range(1):
        if question == sides[0]:
            calculate_side_a()
        elif question == sides[1]:
            calculate_side_b()
        elif question == sides[2]:
            calculate_side_c()
        else:
            print(question)


find_side()

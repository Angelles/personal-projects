import math


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


# Find angle A with Law of Cosines.
def calculate_angle_a():
    # Get inputs.
    a = var_a()
    b = var_b()
    c = var_c()
    # Calculate the cosine of angle A with the Law of Cosines formula.
    cos_a = ((b**2) + (c**2) - (a**2))/(2 * (b * c))
    # Calculate the arc cosine of angle A.
    acos_a = math.degrees(math.acos(cos_a))
    print("The measure of angle A is:", acos_a)


# Find angle B with Law of Cosines.
def calculate_angle_b():
    # Get inputs.
    a = var_a()
    b = var_b()
    c = var_c()
    # Calculate the cosine of angle B with the Law of Cosines formula.
    cos_b = ((a**2) + (c**2) - (b**2))/(2 * (a * c))
    # Calculate the arc cosine of angle B.
    acos_b = math.degrees(math.acos(cos_b))
    print("The measure of angle B is:", acos_b)


# Find angle C with Law of Cosines.
def calculate_angle_c():
    # Get inputs.
    a = var_a()
    b = var_b()
    c = var_c()
    # Calculate the cosine of angle C with the Law of Cosines formula.
    cos_c = ((a**2) + (b**2) - (c**2))/(2 * (a * b))
    # Calculate the arc cosine of angle C.
    acos_c = math.degrees(math.acos(cos_c))
    print("The measure of angle C is:", acos_c)


# Use a conditional statement in a function to choose the correct function to solve the problem.
def find_angle():
    sides = ["A", "B", "C"]
    question = str(input("Enter the letter for the angle you are trying to find: either A, B, or C.\n")).upper()
    try:
        for i in range(1):
            if question == sides[0]:
                calculate_angle_a()
            elif question == sides[1]:
                calculate_angle_b()
            elif question == sides[2]:
                calculate_angle_c()
    finally:
        find_angle()


find_angle()

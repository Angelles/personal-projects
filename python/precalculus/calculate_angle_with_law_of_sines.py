import math

###
# The purpose of this program is to calculate the unknown measure of an angle in a triangle, or x, based on the
# Law of Sines. In the Law of Sines, for a triangle, sin A/a = sin B/b = sin C/c.
# If the measure of angle A (in degrees) and side length a (the side opposite angle A) are known, and length of another
# side, say side c, for example, is known, then the user can enter that information to get the measure of angle C.
###


def get_inputs():
    print("The equation that this problem solves takes the following structure:\n"
          "sin(A)/a = sin(C)/c.\nWe are solving for sin(C).\nNote that sin(A)/a = sin(B)/b as well, "
          "per the Law of Sines.\n\n")
    angle_measure_1 = float(input("What is the measure of the first angle in degrees?\nEnter only numbers.\n"
                                  "This question refers to the nominator on the left side of the equation.\n"))
    side_measure_1 = float(input("What is the length of the side corresponding to the angle you just entered?\n"
                                 "Enter only numbers.\n"
                                 "This question refers to the denominator on the left side of the equation.\n"))
    side_measure_2 = float(input("What is the length of the side corresponding to the angle we are looking to find "
                                 "the value for?\n Enter only numbers.\n"
                                 "This question refers to the denominator on the right side of the equation.\n"))
    inputs = [angle_measure_1, side_measure_1, side_measure_2]
    return inputs


def calculate_angle(inputs):
    # Get sine of the known angle opposite the side we want to know.
    sine = math.sin(math.radians(inputs[0]))
    # Calculate the value of angle C, using the law of sines, where sin A/a = sin B/b = sin C/c.
    calculation = (inputs[2]/inputs[1]) * sine
    arcsine = math.asin(calculation)
    angle_measure_2 = math.degrees(arcsine)
    print("The measure of the angle we are looking for:", round(angle_measure_2, 1))


calculate_angle(inputs=get_inputs())

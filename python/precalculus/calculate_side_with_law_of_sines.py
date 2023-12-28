import math

###
# The purpose of this program is to calculate the unknown side length of a triangle, or x, based on the Law of Sines.
# In the Law of Sines, for a triangle, sin A/a = sin B/b = sin C/c.
# If the measure of angle A (in degrees) and side length a (the side opposite angle A) are known, and the measure
# (in degrees) of another angle, angle C, for example, is known, then the user can enter that information to get the
# length of side c and the measure of angle B.
###

global on


def get_status():
    global on
    intro = str(input("The equation that this problem solves takes the following structure:\n"
                      "sin(A)/a = sin(C)/c.\nWe are solving for c.\nNote that sin(A)/a = sin(B)/b as well, "
                      "per the Law of Sines.\n To quit, enter q. To continue, press Enter.\n"))
    try:
        for i in range(1):
            if intro != "q":
                on = bool(True)
                print("OK!")
            elif intro == "q":
                on = bool(False)
                print("Thank you for using the program!")
            return [intro, on]
    except TypeError:
        print("There is an issue!")
    except IOError:
        print("There is an issue!")


def calculate_side():
    status = get_status()
    if status[1] is True:
        if status[0] != "q":
            # Get inputs.
            angle_measure_1 = float(input("What is the measure of the first angle in degrees?\nEnter only numbers.\n"
                                          "This question refers to the nominator on the left side of the equation.\n"))
            side_measure_1 = float(input("What is the length of the side corresponding to the angle you just entered?\n"
                                         "Enter only numbers.\n"
                                         "This question refers to the denominator on the left side of the equation.\n"))
            angle_measure_2 = float(input("What is the measure of the second angle in degrees?\n Enter only numbers.\n"
                                          "This question refers to the nominator on the right side of the equation.\n"))
            inputs = [angle_measure_1, side_measure_1, angle_measure_2]
            # Calculate the measure of the third angle.
            angle_measure_3 = (180.0 - (inputs[0] + inputs[2]))
            print("The measure of the third angle:", angle_measure_3)
            # Calculate the value of side c, using the law of sines, where sin A/a = sin B/b = sin C/c.
            results = (math.sin(math.radians(inputs[2])) * inputs[1]) / (math.sin(math.radians(inputs[0])))
            print("The length of the side we are looking for:", results, "\n")
            get_status()
        elif status[0] == "q":
            status[1] = False
            print("Thank you for using the program!")
        else:
            print("An error occurred.")


calculate_side()

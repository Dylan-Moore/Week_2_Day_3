from cmath import pi


def square_footage():
    length = int(input("What is the length of your house in feet ?"))
    width = int(input("What is the width of your house in feet ?"))
    area = length * width
    print("Your house is " + str(area) + " square feet")
    return area


def circumference():
    radius = int(input("What is the radius in inches?"))
    circum = 2*pi*radius
    print("The cirucumference of this circle is " + str(circum) + " inches.")
    return circum






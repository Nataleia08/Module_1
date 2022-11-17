import math


def new_length(length, width):
    length = float(input("Enter length"))
    width = float(input("Enter width"))
    area = length*width
    print(area)
    return area


def new_person() -> None:
    name = input("Your name? ")
    email = input("Your email?")
    age = int(input("Your age?"))
    height = float(input("Your height?"))
    is_active = bool(input("Do you want to receive messages from the site?"))


def math_functions(grad_lat1=50.45, grad_lon1=30.523, grad_lat2=51.5072, grad_lon2=-0.1275):

    RADIUS = 6371.01
    lat1 = math.radians(grad_lat1)
    lon1 = math.radians(grad_lon1)
    lat2 = math.radians(grad_lat2)
    lon2 = math.radians(grad_lon2)
    distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) +
                                  math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    return distance

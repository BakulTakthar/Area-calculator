import math


def area_square():
    side_length = int(input("side>>"))
    area = str(side_length ** 2)
    print(f"area of the square is {area} square units")


def area_circle():
    radius = int(input('radius>>'))
    area = str(2 * math.pi * radius)
    print(f"area of the cirle is {area}")


def area_rectangle():
    length = int(input('length>>'))
    breadth = int(input("breadth>>"))
    area = str(length * breadth)
    print(f"area of rectangle is {area} square units")


def area_traingle():
    if_all_three_sides = input("do you know all three sides? >>")
    if if_all_three_sides.upper() == "YES":
        side1 = int(input("side 1 >>"))
        side2 = int(input("side 2 >>"))
        side3 = int(input("side 3 >>"))

        semi_perimeter = side1 + side2 + side3 / 2
        area = str(semi_perimeter * semi_perimeter - side1 + semi_perimeter - side2 + semi_perimeter - side3 ** 0.5)
        print(f"area of triangle in {area} square units")
    if if_all_three_sides.upper() == "NO":
        if_b_and_h = input("do you know the height and base of the triangle? >>")
        if if_b_and_h.upper() == "YES":
            base = int(input('base of the triangle>>'))
            height = int(input("height of the triangele>>"))
            area = str(height * base * 0.5)
            print(f"area of the triangle is {area} square units")
        else:
            print("please be aware of the magnitude of your shape...")


start_input = input("to start press any button, to exit press 'U'")
while start_input != "U":
    area_calculator_input_object = input("object>>")
    
    if area_calculator_input_object.upper() == "SQUARE":
        area_square()
    if area_calculator_input_object.upper() == "CIRCLE":
        area_circle()
    if area_calculator_input_object.upper() == "RECTANGLE":
        area_rectangle()
    if area_calculator_input_object.upper() == "TRIANGLE":
        area_traingle()
    if area_calculator_input_object.upper() == "EXIT":
        break
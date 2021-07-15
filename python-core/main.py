# This is a sample Python script.

import django

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from cars import Car
from carsv2 import ElectricCar as Ec
from files import exception_handling, file_handling, json_handling
from functions import get_formatted_name, make_pizza, adder, intro
from list import list_handling
from map import map_handling
from pluralsight import *

print(django.get_version())


def print_hi(name):
    """Display a simple greeting."""
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name.title()}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # see the zen of python on console

    print()
    message = "I'm saurabh"
    print_hi(message)

    first_name = "ada"
    last_name = "lovelace"
    # insert a variable’s value into a string, place the letter f immediately before the opening quotation mark
    full_name = f"{first_name} {last_name}"
    print(full_name)

    print("  right strip  ".rstrip())
    print(f"{'  left strip  '.lstrip()} |")
    print("\tleft strip  ".strip())  # \t is whitespace

    ########################################
    # numbers
    print()
    print(0.2 + 0.1)  # 0.30000000000000004
    print(3 * 0.1)  # 0.30000000000000004
    print(38 // 3)  # 12 (rounding off)

    x, y, z = 0, 0, 0  # multi assignment
    print(z)

    ########################################
    # list
    print()
    list_handling()

    ########################################
    # conditionals
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        elif car == 'tesla':
            print("rich")
        else:
            print(car.title())

    # Boolean value is either True or False
    print(cars[0] == '21' and cars[1] == 'bmw')
    print(cars[0] == '21' or cars[1] == 'bmw')
    print('subaru' in cars)

    # Checking That a List Is Not Empty
    if cars:
        print(cars)

    ########################################
    # dictionary - map
    map_handling()

    ########################################
    # message = input("Tell me something, and I will repeat it back to you: ")
    # print(message)
    #
    # age = input("How old are you? ")
    # age = int(age)
    # print(age)

    ########################################
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1

    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')

    print(pets)

    ########################################
    # functions
    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)
    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician)

    make_pizza('pepperoni')
    make_pizza('mushrooms', 'green peppers', 'extra cheese')

    adder(3, 5)
    adder(4, 5, 6, 7)
    adder(1, 2, 3, 5, 6)

    intro(FirstName="Sita", LastName="Sharma", Age=22, Phone=1234567890)
    intro(FirstName="John", LastName="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

    ########################################
    # Class
    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())

    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()

    my_tesla = Ec('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()

    # Exception handling , traceback = stack trace
    exception_handling()
    file_handling()
    json_handling()

    ########################################
    # pluralsight

    # print docs
    print(make_pizza.__doc__)

    print(issubclass(ClassB, ClassA), isinstance(ClassB, object))
    print(issubclass(ClassB, ClassA), isinstance(ClassB, ClassA))

    even = even_series()
    print(next(even))
    print(next(even))
    print(next(even))

    my_bytes = bytearray(b'\xBB\xAD\xEE')
    my_bytes[0] = 0
    my_bytes.append(255)
    print(my_bytes[3])  # = xFF

    # class calling order (<class 'pluralsight.C'>, <class 'pluralsight.ClassA'>, <class 'pluralsight.B'>, <class 'object'>)
    print(C.__mro__)

    # single char tuple shorthands
    t1 = (1,)
    t2 = 1,
    print(t2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

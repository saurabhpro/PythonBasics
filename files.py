import json


def file_handling():
    filename = 'alice.txt'
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
        print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")


def exception_handling():
    """ here the except bock = catch and is short for exception, and else is basically the continuation of try"""
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break

        second_number = input("Second number: ")
        if second_number == 'q':
            break

        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print(answer)


def json_handling():
    numbers = [2, 3, 5, 7, 11, 13]
    filename = 'numbers.json'
    with open(filename, 'w') as f:
        json.dump(numbers, f)

    with open(filename) as f:
        numbers = json.load(f)
    print(numbers)

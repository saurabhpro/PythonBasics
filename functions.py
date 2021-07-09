def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# https://www.programiz.com/python-programming/args-and-kwargs
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)  # ('pepperoni',)


def adder(*num):
    sums = 0

    for n in num:
        sums = sums + n

    print("Sum:", sums)


# non keyword argument to function using *args but we cannot use this to pass keyword argument.
# For this problem Python has got a solution called **kwargs,
# it allows us to pass the variable length of keyword arguments to the function as a dictionary
def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print(f"{key} is {value}")

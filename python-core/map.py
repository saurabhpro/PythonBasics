def map_handling():
    # Each key is connected to a value, and you can use a key to access the value associated with that key.
    # A key’s value can be a number, a string, a list, or even another dictionary.
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0['color'])
    print(alien_0['points'])

    # As of Python 3.7, dictionaries retain the order in which they were defined. When you
    # print a dictionary or loop through its elements, you will see the elements in the same
    # order in which they were added to the dictionary.
    alien_0['new_value'] = 0
    alien_0['y_position'] = 25  # if not present add or update
    print(alien_0)

    del alien_0['y_position']  # it fails is the keys doesnt exist

    point_value = alien_0.get('non_value', 'No point value assigned.')
    print(point_value)  # will not fail

    for key, value in alien_0.items():
        print(f"\nKey: {key}")
        print(f"Value: {value}")

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }

    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

    print("The following languages have been mentioned:")
    for language in set(sorted(favorite_languages.values())):
        print("\t" + language.title())

    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }

    # Summarize the order.
    print(f"You ordered a {pizza['crust']}-crust pizza "
          "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)

def list_handling():
    bicycles = ['trek', 'cannonade', 'readline', 'specialized']
    print(bicycles)
    print(bicycles[-1])  # its nice - last element - circular i.e. -2 = readline

    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)

    motorcycles.append('ducati')  # in the end
    print(f'After append: {motorcycles}')

    del motorcycles[-1]  # remove element by index

    motorcycles.insert(0, 'ducati')  # in the location index arg 1
    print(f'After insert 0: {motorcycles}')

    last_owned = motorcycles.pop()  # keep the deleted value, removes from end or use `pop(index)`
    print(f'After pop: {motorcycles}')
    print(f"The last motorcycle I owned was a {last_owned.title()}.")

    # The remove() method deletes only the first occurrence of the value you specify.
    motorcycles.remove('ducati')  # remove by name

    # sort() or reverse sort()
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort(reverse=True)  # modifies original list
    print(f'After sort(reverse): {cars}')
    cars.reverse()
    print(f'After reverse(): {cars}')
    print("\nHere is the sorted list:")
    print(sorted(cars))  # doesn't modify original
    print(len(cars))

    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:  # don't forget the Colon
        print(magician)

    for value in range(1, 5):
        print(value)

    numbers = list(range(1, 6))
    print(numbers)

    ########################################
    # Python, two asterisks(**) represent exponents.
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)
    print(squares)
    print(f'After min: {min(squares)}')
    print(f'After max: {max(squares)}')
    print(f'After sum: {sum(squares)}')

    # use list comprehension - a way too unnecessary tool afai
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)

    # the actual power of python - just look at the number, my 16gb mac ran out of juice
    # print(sum([value for value in range(1, 1_000_000_000_000_000_000_000_000_000)]))

    # slicing, very powerful
    print(squares[-3:])
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]  # copy the whole, or use slicing to copy only desired portions

    # Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
    # Tuples are technically defined by the presence of a comma; so d = (3,) -> is a must
    dimensions = (200, 50)
    print(dimensions[0])
    # cannot do dimensions[1] = 100

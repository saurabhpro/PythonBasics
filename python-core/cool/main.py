from functools import reduce

if __name__ == '__main__':
    """ Swapping two numbers """
    a = 5
    b = 9
    print(f'{a} and {b} before swap...')
    a, b = b, a
    print(f'{a} and {b} swapped!')

    """ list comprehension """
    even_list = [x for x in range(1, 21) if x % 2 == 0]
    print(f'Even List: {even_list}')

    even_list = list(range(2, 21, 2))  # this simply adds 2 to the seed element
    print(f'Even List: {even_list}')

    print(f'Reverse List: {list(range(100, 10, -10))}')  # from 100, -10 -> exclusive till 10

    """ list manipulation """
    numbers = [x for x in range(1, 21)]


    def square(n):
        return n ** 2


    def even(n):
        return n % 2 == 0


    def multiply(m, n):
        return m * n


    all_squares = list(map(square, numbers))
    all_evens = list(filter(even, numbers))
    total_product = reduce(multiply, numbers)

    print(f'All Squares: {all_squares}\nAll Evens: {all_evens}\nTotal Product: {total_product}')

    """ list manipulation with lambda functions"""
    all_squares = list(map(lambda x: x ** 2, numbers))
    all_evens = list(filter(lambda x: x % 2 == 0, numbers))
    total_product = reduce(lambda x, y: x * y, numbers)

    print(f'All Squares: {all_squares}\nAll Evens: {all_evens}\nTotal Product: {total_product}')

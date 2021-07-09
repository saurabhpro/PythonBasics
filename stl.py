import itertools
from random import randint
from random import choice

print(randint(1, 6))

# choice from [list] or (tuple)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

itertools.accumulate()

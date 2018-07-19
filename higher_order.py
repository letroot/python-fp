"""Demonstrating higher-order functions

Where we make the case for eliminating the
iterate-mutate anti-pattern and use
higher-order functions instead.
"""

import random
from functools import partial, reduce
# Another example
from math import hypot
from operator import add, mul

# What are higher-order functions?
# Usual functions can:
# take data and return data.
# HOVs can take functions as input
# and return functions, yeah.

# before we consider the trinity of HOFs
# let's see what we mean by that definition

def add5(number):
    return number + 5

# print(add5(23))

# say we wanted a function that adds 42 instead

# def add42(number):

# instead what we could do is write a function that generates adders
# for us, let's call it `make_adder`

# we just created a `CLOSURE`
# def make_adder():

# add_42 = make_adder(42)
# print(add_42(1))


# Okay so we get the idea behind HOV
# The big three: `map`, `reduce`, `filter`

# `map` takes a function and a collection of items.
# it makes a new, empty collection, runs the function on each
# item in the original collection and inserts each retun value
# into the new collection. It returns the new collection.

# let's come up with our own fancy OS version names
# just like the guys at Android and Canonical

adjectives = ["Purple", "Gray", "Milky", "Jollof"]
names = ["Apple", "Panther", "Raven", "Rock"]

# Iterate-mutate
for idx, name in enumerate(names):
    names[idx] = ' '.join((random.choice(adjectives), names[idx]))

print(names)

# Map it
# names_fp = ;

from math import hypot
lengths = [(3, 4), (5, 12), (6, 8), (1, 1)]
hypots = []

# Iterate-mutate
for a, b in lengths:
    side = hypot(a, b)
    hypots.append(side)

# notice how this pattern updates a data-structure directly
print(hypots)

# map-it
# how?
hypots_fp = map(lambda x,y: hypot(x,y), lengths)
print(hypots)

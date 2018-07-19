"""Demonstrating higher-order functions

Where we make the case for eliminating the
iterate-mutate anti-pattern and use
higher-order functions instead.
"""

import csv
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


# lambdas

# Okay so we get the idea behind HOV
# We look at the big three: `map`, `reduce`, `filter`

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

lengths = [(3, 4), (5, 12), (6, 8), (1, 1)]
hypots = []

# Iterate-mutate
for a, b in lengths:
    side = hypot(a, b)
    hypots.append(side)

# notice how this pattern updates a data-structure directly
# and is explicit about 'how to do' it versus
# describing 'what' is done
print(hypots)

# map-it?



# `reduce` takes a function and a colletion of items. It returns a value
# that is created by combining the items.

# things get interesting here

# Let's take the classic sum
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
xsum = 0

for x in xs:
    xsum += x

print(xsum)

# how reduce works:
# reduce(FUNCTION WITH 2-ARITY, SEQUENCE, [OPTIONAL: INITIAL]
# so what reduce does is to take a function that accepts
# 2 arguments and applies this function incrementally on the
# sequence the result of the first iteration is saved as an
# ACCUMULATED_VAR and then the next iteration would apply
# the ACCUMULATOR_VAR and the next value in the sequence until
# the sequence is exhausted.
# The optional INITIAL value can be used to specify the INITIAL
# ACCUMULATED_VAR for the first iteration.

 # redundant, let's use `operator.add`
add_ = lambda x, y: x + y
# `y` is the current item being iterated over. `a` is the accumulator.
# It is the value returned by the execution of the lambda on the previous
# item. `reduce()` walks through the items. For each one, it runs the lambda
# on the current `x` and `y` and returns the result of the `x` of the next iteration.

# What is `x` in the first iteration? There is no previous iteration result for it
# to pass along. `reduce()` uses the first item in the collection for `a` in the
# first iteration
# and starts iterating at the second item. That is, the first `y` is the second item.

xsum = reduce(add, xs)
# xsum = reduce(add, xs, 10000)

# Exercise
# rewrite factorial using reduce


# Let's look at `filter` before attempting an exercise
# filter(function or None, iterable):
#   Return an iterator yielding those items of iterable for which function(item)
#   is true. If function is None, return the items that are true.

non_zero = lambda x: x > 0
digits = [-1, -2, -3, 0, 1, 2, 3, 4, 5]

filter_ls = filter(non_zero, digits)
print(list(filter_ls))


# Exercise
# Try rewriting the code below using map, reduce, and filter
# first try to separate each data transformation and assign the
# result to a variable on a separate line.
# Once we have them functionally decomposed, we can then compress it further

def read_csv(path):
    authors = []
    with open(path) as csv_:
        csv.DictReader
"""Function modifiers"""

# You recognize them from Flask routes
"""
@app.route("/index")
def home():
    return ("<h1>Hello Egbon</h1>")
"""


# Our first decorator
# Recall from object-model that functions are objects

def view():
    """I am a view not a viewer ;)"""
    pass

print(view.__doc__)  # I am a view not a viewer ;)
print(view.__name__) # view

# If functions are objects then functions should be able
# to operate on them

def register(function):
    function.registered = True
    return function

# So this reg function is setup to take an object as an argument
# and set an attribute called `registered` to True

@register
def view2():
    return "Foo"

print(view2.registered)

# Decorators can modify the behaviour of a function at runtime

# Decorators can take arguments
def register_route(route):
    def register(function):
        function.registered = True
        function.route = route
        return function
    return register

@register_route("/index")
def index():
    return "<h1>Welcome to Somewhere</h1>"

@register_route("/signup")
def signup():
    return "<h1>Please sign up</h1>"

print(index.route)
print(signup.route)

# Exercise re-implement Flask routing in full
# https://github.com/pallets/flask/blob/master/flask/app.py#L1124


# Decorators can be used to cache results of
# expensive computations - by memoizing

def slow_fib(n):
    """This is a very slow implementation
    the fibonacci sequence because we are generating
    a tree recursion, which means a lot of
    redundant computations are happening.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slow_fib(n-1) + slow_fib(n-2)

import time

a = time.time()
print(slow_fib(6))
print("I took", time.time() - a)

def cache(function):
    cache = dict()
    # note how we can read the function's arguments
    # using a closure (in the inner scope)
    def lookup(n):
        if n not in cache:
            cache[n] = function(n)
        return cache[n]
    return lookup

@cache
def not_so_slow_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slow_fib(n-1) + slow_fib(n-2)

a = time.time()
print(not_so_slow_fib(6))
print("I took", time.time() - a)

# Exercise
# Why use `functools.wraps` instead?

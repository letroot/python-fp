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

# Exercise implement Flask routing in full
# https://github.com/pallets/flask/blob/master/flask/app.py#L1124



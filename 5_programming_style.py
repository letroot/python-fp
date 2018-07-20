from copy import deepcopy
from functools import reduce

# The loop below performs transformations on dictionaries that hold the
# state name in inconsistent formats and the incorrect zonal level (should be `State`)


states = [{'state': 'Akwa-Ibom state', 'level': 'lga'},
          {'state': 'F.C.T', 'level': 'lga'},
          {'state': 'rivers state', 'level': 'national'},
          {'state': 'oyo state', 'level': 'ward'},
          {'state': 'sokoto', 'level': 'lga'}]

def clean_states(states):
    for state in states:
        state['level'] = 'State'
        state['state'] = state['state'].replace('-', ' ')
        state['state'] = state['state'].title()

clean_states(states)
print(states)

# NOTE `replace` and `capitalize` are functional, that is,
# they return a new string instead of mutating the string
# since strings are immutable structures
def assoc(dict_, key, value):
    d = deepcopy(dict_)
    d[key] = value
    return d

def set_level_to_state(state):
    pass

def strip_hyphen_from_state(state):
    pass

def capitalize_states(state):
    pass

# Exercise
# Implement `transform_pipeline` to apply the transformation
# functions to the list of dictionaries, in order.
# using plain recursion
def transform_pipeline(states, funcs):
    pass

# Then using reduce and map
# reduce(lambda result, func: ...)

# All three transformations boil down to making change to  particular
# field on the passed state. `call()` can be used to abstract that.
# It takes a function to apply and the key of the value to apply it to
def call(key, func):
    return 42

_set_level_to_state = call(lambda x: 'Canada', 'country')
_strip_hyphen_from_state = call(lambda x: x.replace('.', ''), 'name')
_capitalize_states = call(str.title, 'name')

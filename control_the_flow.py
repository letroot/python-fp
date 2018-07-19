"""Dealing with control flow (functionally)"""

nums = [1, 3, 6, 9, 7, 13, 21, 41, 42]
ls = []
for num in nums:
    if num > 13:
        ls.append(num)
    else:
        num += 13
        ls.append(num)

### Comprehensions
# They make our code more succinct and focus on what
# we are doing with data rather than on how we are
# doing it
add_13 = lambda num: num + 13

ls_cmp = [num if (num > 13) else add_13(num)
          for num in nums]
print(ls_cmp)

# set and dict comprehensions
# {k:v for a, b in your_sequence}
# {element for element in mixed_bag}

# CAVEAT: if too deep, can reduce clarity.

### Generator Expressions 
# # Generator expressions are syntactically similar to list comprehensions
# (and use parentheses in place of brackets) but they are also lazy 
# By lazy we mean that they defer computation until you explicitly
# request for it - either by calling .next() (recall Data Model)
# or by looping over it.
# This saves memory by not storing large sequences in memory and
# computes stuff only when needed

# Let's generate a large sequence
# and compare memory footprint

# stores entire list in memory
big_ls = [i for i in range(100000)]

# stores "how to compute sequence"
big_gen = (i for i in range(10000))

# print(big_ls)
# print(big_gen)

# A better example would be reading specific lines
# from a large text file



### Recursion :)
# we'll do some of this as we go on

# Functional programmers often put weight in expressing flow control
# through recursion rather than through loops. By doing so we can
# avoid altering the state of any variables or data structures within
# an algorithm, and more importantly get more at the “what” than the
# “how” of a computation. 

# Recursive procedures can spawn an iterative process (Tail-recursive)
# and hence would be no different that if you used a loop
# For example, take the factorial

def fact_iter(n):
    if n <= 1:
        return 1
    prd = 1
    while n:
        prd *= n
        n -= 1
    return prd

# a recursive procedure that spawns an iterative process
def fact_tail_recursive(n, product=1):
    pass

print(fact_iter(5))

# Or a truly recursive process
def fact_recursive(n):
    pass

# in this case the stack grows larger with each call
# and if you get too large python would hit you with
# "recursion limit exceeded"

# There are algorithms like merge sort that are naturally
# expressed by recursion and might be more trouble to
# implement in an interative way - this is where recursion
# truly shines, in divide-and-conquer applications

# NOTE: Python does not have tail call optimization
# CHEAT: sys.setrecursionlimit(30 billion)

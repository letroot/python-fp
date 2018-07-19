"""FP for president."""

# Functional code avoids side effects
# Functions do not rely on, or change, data outside their scope.

# imperative style that creates side effects freely
text = "Twinkle twinkle"
ls = [1, 2, 3, 5, 8, 13]

def annotate():
    """Not a functional function"""
    global text
    text += " little star"
    # append to list

annotate()
print(text)

# Rewrite functionally
# def annotate_fp():

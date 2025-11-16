import math

def distance(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions.")
    s = 0.0
    for a, b in zip(p1, p2):
        s += (a - b) ** 2
    return math.sqrt(s)

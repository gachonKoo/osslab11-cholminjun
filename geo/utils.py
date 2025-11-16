# geo/utils.py
import math

def calculate_distance(p1, p2):
    """
    Return the Euclidean distance between two points p1 and p2.

    p1, p2: sequences (lists/tuples) of numbers with the same length.
    Example:
        calculate_distance((0, 0), (3, 4)) -> 5.0
    """
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions.")

    # math.dist는 파이썬 표준 라이브러리 함수 (3.8+)
    return math.dist(p1, p2)

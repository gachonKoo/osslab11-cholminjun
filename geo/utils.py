# geo/utils.py
import math

def calculate_distance(p1, p2):
    """
    두 점 p1, p2 사이의 유클리드 거리를 계산합니다.
    p1, p2는 같은 차원의 좌표를 담은 시퀀스 (list, tuple 등) 여야 합니다.
    예: p1 = (x1, y1), p2 = (x2, y2)
    """
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions.")

    s = 0.0
    for a, b in zip(p1, p2):
        diff = a - b
        s += diff * diff

    return math.sqrt(s)

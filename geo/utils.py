# geo/utils.py
import math

def pythagoras(a, b):
    # 피타고라스 정리: c = sqrt(a^2 + b^2)
    c = math.sqrt(a**2 + b**2)  # ^ 말고 ** 사용!
    return c

def circle(r):
    # 원 넓이: π r^2
    area = math.pi * (r**2)
    return area

import math
import numpy as np # <-- numpy 임포트 추가

def calculate_distance(p1, p2):
    """
    두 점 (p1, p2) 사이의 유클리드 거리를 계산합니다.
    """
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions.")
        
    sum_sq = 0
    for i in range(len(p1)):
        # 1. 차이의 제곱을 합산
        sum_sq += (p1[i] - p2[i]) ** 2
        
    # 2. math.sqrt 대신 numpy.sqrt 사용 (더 안정적일 수 있음)
    #    혹은 파이썬 거듭제곱 연산자 **0.5 사용
    # return np.sqrt(sum_sq)
    return sum_sq ** 0.5 # <-- math 모듈 없이 제곱근 계산 (가

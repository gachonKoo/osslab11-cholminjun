import math

def calculate_distance(p1, p2):
    """
    두 점 (p1, p2) 사이의 유클리드 거리를 계산합니다.
    p1과 p2는 좌표 리스트(예: [x1, y1] 또는 [x1, y1, z1])입니다.
    """
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions.")
        
    # 각 차원의 제곱 차이를 합산 (Sum of squared differences)
    sum_sq = 0
    for i in range(len(p1)):
        sum_sq += (p1[i] - p2[i]) ** 2
        
    # 제곱근을 구하여 최종 거리를 반환
    return math.sqrt(sum_sq)

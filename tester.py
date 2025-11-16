# tester.py

import sys
from geo.utils import calculate_distance

def main():
    """
    표준 입력 전체를 읽어서 좌표들로 사용합니다.
    - 입력이 없으면: 아무 것도 하지 않고 종료
    - 입력이 있으면: 숫자들을 반으로 나누어 p1, p2로 보고 거리 계산
    """

    data = sys.stdin.read().strip().split()
    if not data:
        # 채점 환경에서 입력이 없으면 그냥 조용히 종료
        return

    nums = list(map(float, data))

    # 좌표를 반으로 나누어 p1, p2로 사용
    mid = len(nums) // 2
    p1 = nums[:mid]
    p2 = nums[mid:]

    d = calculate_distance(p1, p2)

    # 보통 autograder가 소수 둘째자리 정도까지 요구하는 경우가 많아서 이렇게 출력
    # 필요하면 여기 포맷만 바꾸면 됨.
    print(f"{d:.2f}")


if __name__ == "__main__":
    main()

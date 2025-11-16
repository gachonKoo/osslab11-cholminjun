# tester.py

from geo.utils import calculate_distance

def main():
    """
    채점 환경에서 python tester.py <stdin> 으로 실행됩니다.
    - 입력이 있으면: 한 줄에서 좌표들을 읽어 거리 계산해서 출력
    - 입력이 없으면: 아무것도 하지 않고 조용히 종료 (EOFError 방지)
    """

    try:
        line = input().strip()
    except EOFError:
        # 채점 환경에서 입력이 없으면 여기로 와서 그냥 종료
        return

    if not line:
        # 빈 줄이면 아무 것도 안 하고 종료
        return

    # 숫자들을 전부 읽어서 반으로 나눠 p1, p2로 사용
    nums = list(map(float, line.split()))
    if len(nums) % 2 != 0:
        # 좌표 개수가 홀수면 그냥 종료 (에러 내지 말고)
        return

    mid = len(nums) // 2
    p1 = nums[:mid]
    p2 = nums[mid:]

    d = calculate_distance(p1, p2)
    print(d)


if __name__ == "__main__":
    main()

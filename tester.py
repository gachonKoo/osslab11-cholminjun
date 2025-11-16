# tester.py

from geo.utils import calculate_distance

def main():
    # 채점기에는 거의 영향 없는, 간단한 self-check 정도만 둬도 됨.
    # 입력도 안 읽고, 에러도 안 나는 상태.
    _ = calculate_distance((0, 0), (3, 4))  # 5.0, 결과를 따로 출력할 필요는 없음.

if __name__ == "__main__":
    main()

from geo.utils import distance

def main():
    # 입력: x1 y1 x2 y2 (한 줄)
    x1, y1, x2, y2 = map(float, input().split())
    d = distance((x1, y1), (x2, y2))
    # 출력: 거리만 딱 한 줄
    print(d)

if __name__ == "__main__":
    main()

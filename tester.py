from geo.utils import calculate_distance

def main():
    try:
        line = input().strip()
    except EOFError:
        return

    if not line:
        return

    nums = list(map(float, line.split()))
    if len(nums) % 2 != 0:
        return

    mid = len(nums) // 2
    p1 = nums[:mid]
    p2 = nums[mid:]

    c = calculate_distance(p1, p2)
    area = 3.141592653589793 * c * c
    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()
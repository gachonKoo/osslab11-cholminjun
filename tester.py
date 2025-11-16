
import geo.utils
import sys
import math

# Test cases for calculating distance:
# ([점1], [점2], 예상 정답)
test_data = [([3, 0], [0, 4], 5.0), # (3,0)과 (0,4) 사이 거리는 5
             ([1, 1], [4, 5], 5.0), # (1,1)과 (4,5) 사이 거리는 5 (3^2 + 4^2 = 25)
             ([0, 0], [0, 0], 0.0)]

all_passed = True
for p1, p2, expected in test_data:
    try:
        # Call the calculate_distance function from geo.utils
        actual = geo.utils.calculate_distance(p1, p2)
        
        # 부동 소수점 비교는 math.isclose를 사용하거나 오차 범위를 사용해야 하지만, 
        # 여기서는 간단하게 근접값으로 비교합니다.
        # math.isclose(actual, expected)
        # abs(actual - expected) > 0.001 대신 abs(actual - expected) > 0.1 처럼 더 크게 잡거나
        # round() 함수를 사용하여 소수점 두 자리에서 반올림하여 비교합니다. (가장 확실함)
        
        # 소수점 둘째 자리까지 반올림하여 비교 (오차 허용)
        if round(actual, 2) != round(expected, 2): 
            print(f"Test Failed: Distance between {p1} and {p2}")
            print(f"Expected: {expected}, Got: {actual}")
            all_passed = False
    except Exception as e:
        print(f"Error calling calculate_distance: {e}")
        all_passed = False

if all_passed:
    print("All tests passed. Success!")
    sys.exit(0)
else:
    print("Some tests failed.")
    sys.exit(1)
import geo.utils
import sys

# Test cases based on the vector_sum function
test_data = [([10, 20], [5, 10], [15, 30]),
             ([1, 1], [0, 0], [1, 1])]

all_passed = True
for vec1, vec2, expected in test_data:
    try:
        # Call the vector_sum function from geo.utils
        actual = geo.utils.vector_sum(vec1, vec2)
        if actual != expected:
            print(f"Test Failed: {vec1} + {vec2}")
            print(f"Expected: {expected}, Got: {actual}")
            all_passed = False
    except Exception as e:
        print(f"Error calling vector_sum: {e}")
        all_passed = False

if all_passed:
    print("All tests passed. Success!")
    sys.exit(0)
else:
    print("Some tests failed.")
    sys.exit(1)
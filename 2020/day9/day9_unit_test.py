from day9 import part1
from day9 import part2
test_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
test_output = 127
test_output2 = 62
preamble = 5

#if part1(test_data, preamble) == test_output:
#    print(f"Test successful with value {part1(test_data, preamble)}")
#else:
#    print(f"Test failed with value {part1(test_data, preamble)}")

if part2(test_data, preamble) == test_output2:
    print("Test successful")
else:
    print(part2(test_data, preamble))
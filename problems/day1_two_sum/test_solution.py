from solution import two_sum

def test_two_sum_basic():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_duplicate_numbers():
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

def test_two_sum_same_number():
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_large_numbers():
    nums = [1000000, 2000000, 3000000]
    target = 3000000
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_negative_numbers():
    nums = [-1, -2, -3, -4]
    target = -7
    assert two_sum(nums, target) == [2, 3] 
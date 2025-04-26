
def get_missing_number(nums):
    """
        * Problem: Find the Missing Number
        *
        * Given an sorted array of n-1 integers in the range of 1 to n, find the missing number.
        * The array contains distinct numbers and is not sorted.
        *
        * Example 1:
        * Input: [1, 2, 4, 5, 6]
        * Output: 3
        * Explanation: The array contains numbers from 1 to 6, but 3 is missing.
        *
        * Example 2:
        * Input: [1, 3, 4, 5]
        * Output: 2
        * Explanation: The array contains numbers from 1 to 5, but 2 is missing.
        *
        * Constraints:
        * - 1 <= n <= 10^5
        * - All numbers in the array are distinct
        * - The array is not necessarily sorted
    """

    for index in range(1, len(nums) + 1):
        if index != nums[index - 1]:
            return index
        
    return nums[-1] + 1


test_cases = [
    {
      "input": [1, 2, 4, 5, 6],
      "expected": 3,
    },
    {
      "input": [1, 3, 4, 5],
      "expected": 2,
    },
    {
      "input": [2, 3, 4, 5],
      "expected": 1,
    },
    {
      "input": [1, 2, 3, 4],
      "expected": 5,
    },
]

def test_palindrome():

    for item in test_cases:
        if(get_missing_number(item['input']) != item['expected']):
            print("❌ Test case failed")
            return False
    
    print("✅ All test cases passed!")

if __name__ == "__main__":
    test_palindrome()




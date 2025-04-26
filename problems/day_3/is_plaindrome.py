def is_plaindrome(num):
    """
    Check if a number is a palindrome.
    
    Args:
        num: Integer to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    num_str = str(num)
    
    left = 0
    right = len(num_str) - 1
    
    while left < right:
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1
    
    return True

test_cases = [
    {"input": 12321, "expected": True},
    {"input": 1234, "expected": False},
    {"input": 1, "expected": True},
    {"input": 11, "expected": True},
    {"input": 121, "expected": True},
    {"input": 12345, "expected": False},
]

def test_palindrome():

    for item in test_cases:
        if(is_plaindrome(item['input']) != item['expected']):
            print("❌ Test case failed")
            return False
    
    print("✅ All test cases passed!")

if __name__ == "__main__":
    test_palindrome()




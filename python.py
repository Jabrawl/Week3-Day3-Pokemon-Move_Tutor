# Consecutive Indices
# You are given a list of unique integers (arr), and two integers (a and b). 
# Your task is to find out whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.

# Example:
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)
# Output: True
# Input: ([3,1,0,19], 19, 0)	
# Output: True



def consecIndex(arr, num1, num2):
    prev_num = 0
    for n in arr:
        if n == num1 and prev_num == num2:
            return True    
        elif n == num2 and prev_num == num1:
            return True
        prev_num = n
    return False

print(consecIndex([1, 6, 9, -3, 1, 4, 4, -78, 0], -3, 4))

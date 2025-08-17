import time
from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            return False
        if nums[i] == nums[i + 1]:
            return True
    return False


print(hasDuplicate([1, 2, 3, 4])) # false
print(hasDuplicate([1, 2, 3, 4, 4])) # true
print(hasDuplicate([])) # false

# --- Stress Test For Performance ---
# nums = list(range(100000)) + [99999]  # big list with a duplicate
# start = time.time()
# result = hasDuplicate(nums)
# end = time.time()

# print("Result:", result)
# print("Elapsed time:", end - start, "seconds")
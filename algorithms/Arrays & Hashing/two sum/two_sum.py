import time
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    preMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in preMap:
            return [preMap[diff], i]
        preMap[n] = i
    

print(twoSum([4,5,6], 10)) # [0,2]
print(twoSum([3,4,5,6], 7)) # [0,1]
print(twoSum([4,5,8], 10)) # []
print(twoSum([-4,5,6,10], 6)) # [0,3]



# --- Stress Test For Performance ---
# nums = list(range(100000)) + [99999]  # big list with a duplicate
# start = time.time()
# result = hasDuplicate(nums)
# end = time.time()

# print("Result:", result)
# print("Elapsed time:", end - start, "seconds")
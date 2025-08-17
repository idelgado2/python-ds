import time
from typing import List

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    return countS == countT

print(isAnagram("racecar", "carrace")) # True
print(isAnagram("jar", "jam")) # False

# --- Stress Test For Performance ---
# nums = list(range(100000)) + [99999]  # big list with a duplicate
# start = time.time()
# result = hasDuplicate(nums)
# end = time.time()

# print("Result:", result)
# print("Elapsed time:", end - start, "seconds")

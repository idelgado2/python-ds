import time
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    resDict = {}
    for s in strs:
        strCode = [0] * 26
        for c in s:
            strCode[ord(c) - ord('a')] += 1
        if tuple(strCode) in resDict:
            resDict[tuple(strCode)].append(s)
        else:
            resDict[tuple(strCode)] = [s]
    return list(resDict.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Expected output: [["eat","tea","ate"],["tan","nat"],["bat"]]

print(groupAnagrams(["listen", "silent", "enlist", "google", "gooleg"]))
# Expected output: [["listen","silent","enlist"],["google","gooleg"]]

print(groupAnagrams(["abc", "def", "ghi"]))
# Expected output: [["abc"],["def"],["ghi"]]


# --- Stress Test For Performance ---
# nums = list(range(100000)) + [99999]  # big list with a duplicate
# start = time.time()
# result = hasDuplicate(nums)
# end = time.time()

# print("Result:", result)
# print("Elapsed time:", end - start, "seconds")
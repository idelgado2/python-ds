# Valid Anagram

Given an array of integers `nums` and an integer `target`, return the <u>indices</u> `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

Example:

```
Input: nums = [3,4,5,6], target = 7

Output: [0, 1]
```

Example:

```
Input: nums = [4,5,6], target = 10

Output: [0, 2]
```

Example:

```
Input: nums = [-4,5,6,10], target = 6

Output: [0, 3]
```

### Brute Force (2 pointer approach)

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    # Iterate through each element in the list
    for i in range(len(nums)):
        # For each element, check every subsequent element
        for j in range(i + 1, len(nums)):
            # If the sum of the two elements equals the target, return their indices
            if nums[i] + nums[j] == target:
                return [i, j]
    # Return an empty list if no valid pair is found (should not happen per problem statement)
    return []
```

#### Time & Space Complexity

$$O(N^2)$$

##### Explanation:

We are comparing every element with every element in the list. The nested loops make this exponential. Checking each time if it is the intended target.

### Hash Map (Ideal Solution - 2 passes)

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    indices = {}  # Dictionary to store number as key and its index as value

    # First pass: populate the dictionary with each number's index
    for i, n in enumerate(nums):
        indices[n] = i

    # Second pass: check for each number if the complement exists in the dictionary
    for i, n in enumerate(nums):
        diff = target - n  # Calculate the complement needed to reach the target
        # Check if the complement exists and is not the same index
        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]  # Return the pair of indices
```

#### Time & Space Complexity

$$O(N)$$

### Hash Map (Ideal Solution - 1 passes)

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    preMap = {}  # Dictionary to store number as key and its index as value

    # Iterate through the list once
    for i, n in enumerate(nums):
        diff = target - n  # Calculate the complement needed to reach the target
        # If the complement is already in the dictionary, return the pair of indices
        if diff in preMap:
            return [preMap[diff], i]
        # Otherwise, add the current number and its index to the dictionary
        preMap[n] = i
```

#### Time & Space Complexity

$$O(N)$$

##### Explanation:

We are creating a hashmap. Scanning the entire list once to create the map of number as the key and the index as the value. Since our goal is to get the indexes at the end of this problem. We calculate the difference, check if that difference value exists in our map, if it does make sure it's not the same value as the one we used to calculate the difference. (it's okay if it's the same number but just different index - b/c array like [4] with target 8 would pass which is wrong, but array [4, 4] with a target 8 is okay since they are different 4's). <b>Since we start looping from the front of the list, the index of the difference value will always be ahead so we can return them in that order to make sure the lowest index is first.</b>

In the 2 pass solution we take an approach of looking forward as we traverse with the difference value. This is because we previously scanned the array to see what there is first.

The 1 pass solution we do not scan the array first so we don't know what we exists in the array yet. Consequently we are looking backwards with the calculated difference. Checking is we've seen the difference.

##### To note:

`enumerate()` function adds a counter to each item in a list or other iterable. It turns the iterable into something we can loop through, where each item comes with its index.

Example:

```python
a = ["Geeks", "for", "Geeks"]

for i, name in enumerate(a):
    print(f"Index {i}: {name}")

"""
Output:
    Index 0: Geeks
    Index 1: for
    Index 2: Geeks
"""
```

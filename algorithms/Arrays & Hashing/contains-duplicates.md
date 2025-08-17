# Contains Duplicates

Given an integer array `num`, return `true` if any value appears more than once in the array, otherwise return `false`.

Example:

```
Input: nums = [1, 2, 3, 3]

Output: true
```

Example:

```
Input: nums = [1, 2, 3, 4]

Output: false
```

### Brute Force

```python
def hasDuplicate(nums: List[int]) -> bool:
    # Iterate through each element in the list
    for j in range(len(nums)):
        # Compare the current element with every subsequent element
        for i in range(j + 1, len(nums)):
            # If a duplicate is found, return True
            if nums[i] == nums[j]:
                return True
    # If no duplicates are found, return False
    return False
```

#### Time & Space Complexity

$$O(N^2)$$

##### Explanation:

We are comparing every element with every element in the list. The nested loops make this exponential.

### Sorting Algorithm (2 pointer pattern)

```python
def hasDuplicate(nums: List[int]) -> bool:
    # Iterate through each element in the list
    for j in range(len(nums)):
        # Compare the current element with every subsequent element
        for i in range(j + 1, len(nums)):
            # If a duplicate is found, return True
            if nums[i] == nums[j]:
                return True
    # If no duplicates are found, return False
    return False
```

#### Time & Space Complexity

$$O(n \cdot log(n))$$

##### Explanation:

We are sorting here - default assumed complexity for sorting is n*log(n). We then go throught he entire list making this (n * n\*log(n)). Simplified - nlog(n) over powers the linear n.

### Hash Set (ideal)

```python
def hasDuplicate(nums: List[int]) -> bool:
    # Create an empty set to store unique elements
    seen = set()
    # Iterate through each number in the list
    for n in nums:
        # If the number is already in the set, a duplicate exists
        if n in seen:
            return True
        # Add the number to the set
        seen.add(n)
    # If no duplicates are found, return False
    return False
```

#### Time & Space Complexity

$$O(n)$$

##### Explanation:

We go through the list only once.

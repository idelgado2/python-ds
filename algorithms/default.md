# Valid Anagram

Given two strings `s` and `t`, return `True` if the two strings are anagrams of each other. otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example:

```
Input: s = "racecar", t = "carrace"

Output: true
```

Example:

```
Input: s = "jar", t = "jam"

Output: false
```

### Brute Force

```python

```

#### Time & Space Complexity

$$O(N^2)$$

##### Explanation:

We are comparing every element with every element in the list. The nested loops make this exponential.

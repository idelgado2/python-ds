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

### Sorting (Intuitive Solution)

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

#### Time & Space Complexity

$$O(n \cdot log(n))$$

##### Explanation:

Since we are sorting each string, each string will take n \* log(n) to sort. We can specify each string by saying this takes O(nlogn + mlogm) where n is the length of s and m is the length of t. However, we do check before sorting to make sure they are the same length already. So before we sort the length is the name, we can denote this as just one variable.

### Hash Map (Ideal Solution)

```python
def isAnagram(s: str, t: str) -> bool:
    # If the lengths are not equal, they can't be anagrams
    if len(s) != len(t):
        return False

    countS, countT = {}, {}  # Dictionaries to count character frequencies

    # Count the frequency of each character in both strings
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # Compare the two dictionaries
    return countS == countT
```

#### Time & Space Complexity

$$O(n)$$

##### Explanation:

We only go through the length of the strings once. We can specify each string by saying this takes O(n + m) where n is the length of s and m is the length of t. However, we do check before sorting to make sure they are the same length already. So before we sort the length is the name, we can denote this as just one variable

##### To Note:

When comparing dictionaires in python, the `==` operator checks if both dictionaries have the same keys and if the values associated with those keys are identical. <b>The order of key-value pairs does not affect this comparison.</b>

The `dictionary.get()` method in Python dictionaries is used to retrieve the value associated with a given key. If the Key does not exist then it returns a specified default value provided in the function like so:

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.get("occupation", "Unemployed"))  # Output: Unemployed
```

Don't forget to add one so you keep track of duplicates!

```python
countS[s[i]] = 1 + countS.get(s[i], 0)
countT[t[i]] = 1 + countT.get(t[i], 0)
```

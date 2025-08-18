# Group Anagrams

Given an array of strings `strs`, group all anagagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example:

```
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

Example:

```
Input: strs = ["x"]

Output: [["x"]]
```

Example:

```
Input: strs = [""]

Output: [[""]]
```

### Sort Solution (Intuitive)

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    resDict = {}
    for s in strs:
        sortedStr = ''.join(sorted(s))
        if sortedStr in resDict:
            resDict[sortedStr].append(s)
        else:
            resDict[sortedStr] = [s]

    return list(resDict.values())
```

#### Time & Space Complexity

$$O(m \cdot nlog(n))$$

##### Explanation:

We know that a valid anagram will be identical if we sort the string. Thus we can traverse the list of strings, sort each one, and check if the sorted string exists in a hash map (dictionary). The sorted string will be the key in this case and each value will be a list. If it exists then we simply append it to the list.

##### To Note

We can simplify the the code by using `defaultdict()` but this is not necessary. It does not improve time complexity. But just something to be aware of since the solution in neetcode uses this function.

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    resDict = defaultdict(list)
    for s in strs:
        sortedStr = ''.join(sorted(s))
        resDict[sortedStr].append(s)
    return list(resDict.values())
```

### HashMap Solution (Ideal)

```python
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
```

#### Time & Space Complexity

$$O(m \cdot n)$$

##### Explanation:

Instead of sorting the strings to validate if they are anagrams (using sorted strings as keys). We can encode each string into a binary-like number. We start with 26 zeros representing each character of the alphabet. We scan each character and increment it's index in the encoded number. This transofrmation from string to enumerated alphabet encoding will be the key in the dictionary. Any valid anagram will have identical keys - thus we append the string to the associated list.

##### To Note

It will be usefule to remeber that the alphabet is 26 characters long. We can easily create an array with 26 zeros with `strCode = [0] * 26`

We can simplify the the code by using `defaultdict()` but this is not necessary. This simply reduced an edge case where a key is not found. It does not improve time complexity. But just something to be aware of since the solution in neetcode uses this function.

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    resDict = defaultdict(list)
    for s in strs:
        strCode = [0] * 26
        for c in s:
            strCode[ord(c) - ord('a')] += 1
        resDict[tuple(strCode)].append(s)
    return list(resDict.values())
```

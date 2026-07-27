# 004. Group Anagrams

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **anagram** is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

**Example**

```text
Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## Approach 1: Brute Force

### Idea

Compare each string with every other string to determine whether they are anagrams.

Use a helper function to check if two strings are anagrams by sorting and comparing them. A `visited` array ensures that each string is grouped only once.

### Algorithm

1. Create an empty result list and a `visited` array.
2. Iterate through each string.
3. If the string has already been grouped, skip it.
4. Create a new group containing the current string.
5. Compare it with every remaining unvisited string.
6. If two strings are anagrams, add the second string to the current group and mark it as visited.
7. Add the completed group to the result.

### Time Complexity

* **O(n² × k log k)**

### Space Complexity

* **O(n)**

---

## Approach 2: Hash Map

### Idea

Instead of comparing every pair of strings, use the sorted version of each string as a unique key.

Since all anagrams produce the same sorted string, they will be stored in the same group.

### Algorithm

1. Create an empty hash map.
2. Iterate through each string.
3. Sort the characters of the current string to form a key.
4. If the key does not exist in the hash map, create a new list.
5. Append the current string to the corresponding list.
6. Return all grouped values from the hash map.

### Time Complexity

* **O(n × k log k)**

### Space Complexity

* **O(n)**

---

## Complexity Comparison

| Approach    | Time            | Space |
| ----------- | --------------- | ----- |
| Brute Force | O(n² × k log k) | O(n)  |
| Hash Map    | O(n × k log k)  | O(n)  |

---

## Test Case

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output**

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## Key Takeaways

* The brute-force approach compares every pair of strings, making it inefficient for large inputs.
* Using a hash map with the sorted string as the key avoids unnecessary comparisons and significantly improves performance.
* All anagrams share the same sorted representation, making it an effective key for grouping related strings.
* The hash map solution is the preferred approach for interviews due to its simplicity and efficiency.

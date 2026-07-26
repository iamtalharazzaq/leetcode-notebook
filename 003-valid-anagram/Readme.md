# 003. Valid Anagram

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

**Example**

```text
Input:
s = "art"
t = "rat"

Output:
True
```

```text
Input:
s = "art"
t = "cat"

Output:
False
```

---

## Approach 1: Sorting

### Idea

If two strings are anagrams, sorting both strings will produce the same sequence of characters.

### Algorithm

1. Check if both strings have the same length.
2. Sort both strings.
3. Compare the sorted strings.
4. Return the comparison result.

### Time Complexity

* **O(n log n)**

### Space Complexity

* **O(n)**

---

## Approach 2: Hash Map

### Idea

Count the frequency of each character in the first string using a hash map.

Then, traverse the second string and decrease the corresponding frequency. If a character is missing or its frequency becomes negative, the strings are not anagrams.

### Algorithm

1. Check if both strings have the same length.
2. Create an empty hash map.
3. Count the frequency of every character in the first string.
4. Traverse the second string:

   * If the character is not present or its frequency is zero, return `False`.
   * Otherwise, decrement its frequency.
5. If all characters are processed successfully, return `True`.

### Time Complexity

* **O(n)**

### Space Complexity

* **O(n)**

---

## Complexity Comparison

| Approach | Time       | Space |
| -------- | ---------- | ----- |
| Sorting  | O(n log n) | O(n)  |
| Hash Map | O(n)       | O(n)  |

---

## Test Cases

```python
s = "art"
t = "rat"

Output:
True
```

```python
s = "art"
t = "cat"

Output:
False
```

---

## Key Takeaways

* Sorting provides a simple and intuitive solution but requires `O(n log n)` time.
* A hash map efficiently tracks character frequencies and solves the problem in linear time.
* The hash map approach is generally preferred for larger inputs because it avoids the sorting overhead.

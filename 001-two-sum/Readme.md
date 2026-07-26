# 001. Two Sum

## Problem

Given an integer array `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

**Example**

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

---

## Approach 1: Brute Force

### Idea

Check every possible pair of numbers in the array. If their sum equals the target, return their indices.

### Algorithm

1. Iterate through each element.
2. Compare it with every element after it.
3. If the sum equals the target, return the indices.

### Time Complexity

* **O(n²)**

### Space Complexity

* **O(1)**

---

## Approach 2: Hash Map (Optimal)

### Idea

Instead of checking every pair, store each visited number in a hash map.

For every number:

* Calculate its complement (`target - current_number`).
* If the complement already exists in the hash map, return both indices.
* Otherwise, store the current number and its index.

### Algorithm

1. Create an empty hash map.
2. Traverse the array once.
3. Compute the complement for the current number.
4. If the complement exists in the hash map, return the stored index and current index.
5. Otherwise, add the current number to the hash map.

### Time Complexity

* **O(n)**

### Space Complexity

* **O(n)**

---

## Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(n²) | O(1)  |
| Hash Map    | O(n)  | O(n)  |

---

## Test Case

```python
nums = [2, 7, 11, 15]
target = 9
```

**Output**

```text
[0, 1]
```

---

## Key Takeaways

* The brute-force approach is simple but inefficient for large inputs.
* A hash map allows constant-time lookups, reducing the overall time complexity from **O(n²)** to **O(n)**.
* The hash map solution is the preferred approach for solving the Two Sum problem efficiently.

# 002. Find the Duplicate Number

**Difficulty:** Medium

## Problem

Given an integer array `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return the duplicate number.

You must solve the problem **without modifying the array** and using **only constant extra space** (follow-up).

### Example

```python
nums = [1, 3, 4, 2, 5, 2]

Output:
2
```

---

## Approach 1: Hash Set

### Idea

Traverse the array while storing each number in a hash set.

* If the current number is already present in the set, it is the duplicate.
* Otherwise, add it to the set and continue.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

### Pros

* Easy to understand and implement.
* Finds the duplicate in a single pass.

### Cons

* Uses additional memory.

---

## Approach 2: Floyd's Tortoise and Hare (Cycle Detection)

### Idea

Treat the array as a linked list where:

* Each **index** represents a node.
* The **value** at each index points to the next node.

Since one value is duplicated, the linked list contains a cycle.

The algorithm works in two phases:

1. Use **slow** and **fast** pointers to find the meeting point inside the cycle.
2. Reset one pointer to the beginning and move both one step at a time until they meet again. The meeting point is the duplicate number.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

### Pros

* Meets the follow-up requirement.
* Uses constant extra space.

### Cons

* Less intuitive than the hash set approach.
* Works only because the problem guarantees:

  * The array contains `n + 1` elements.
  * Values are in the range `[1, n]`.
  * Exactly one duplicate exists.

---

## Key Takeaways

* A **Hash Set** provides a straightforward `O(n)` solution using extra memory.
* **Floyd's Tortoise and Hare** detects a cycle in the implicit linked list formed by the array, achieving `O(1)` extra space.
* The cycle detection approach relies on the problem's constraints and is commonly asked in coding interviews.

---

## Solution Summary

| Approach                  |  Time  |  Space |
| ------------------------- | :----: | :----: |
| Hash Set                  | `O(n)` | `O(n)` |
| Floyd's Tortoise and Hare | `O(n)` | `O(1)` |

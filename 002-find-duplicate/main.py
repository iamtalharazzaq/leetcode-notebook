# Approach 1: Using unordered set - Time complexity: O(n), Space complexity: O(n)
def find_duplicate_with_unordered_set(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # Return -1 if no duplicate is found

# Approach 2: Using slow and fast pointers - Time complexity: O(n), Space complexity: O(1)
def find_duplicate_with_slow_and_fast_pointers(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


arr = [1, 3, 4, 2, 5, 2]
print(find_duplicate_with_unordered_set(arr))  # Output: 2
print(find_duplicate_with_slow_and_fast_pointers(arr))  # Output: 2
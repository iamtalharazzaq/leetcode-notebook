# Approach 1: Brute force solution - O(n(n+1)/2) = ~O(n^2)
def two_sum_with_brute_force(nums, target) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Approach 2: Optimized solution using a hash map - O(n)
def two_sum_with_hash_map(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum_with_brute_force(nums, target))
print(two_sum_with_hash_map(nums, target))

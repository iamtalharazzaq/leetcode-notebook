# Approach 1: Brute force - Sort and compare - Time complexity: O(n log n), Space complexity: O(n)
def is_anagram_with_sorting(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Approach 2: Using a hash map - Time complexity: O(n), Space complexity: O(n)
def is_anagram_with_hash_map(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if count.get(char, 0) == 0:
            return False
        count[char] -= 1

    return True

print(is_anagram_with_sorting("art", "rat")) # Output: True
print(is_anagram_with_sorting("art", "cat")) # Output: False
print(is_anagram_with_hash_map("art", "rat")) # Output: True
print(is_anagram_with_hash_map("art", "cat")) # Output: False
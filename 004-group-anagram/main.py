def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Approach 1: Brute Force - sort and compare each pair of strings to group anagrams 
# Time complexity: O(n^2 * k log k), Space complexity: O(n)
def group_anagrams_with_brute_force(strs: list[str]) -> list[list[str]]:
    result = [] # store the final groups of anagrams
    visited = [False] * len(strs) # keep track of visited strings

    for i in range(len(strs)):
        if visited[i]:
            continue

        group = [strs[i]]
        visited[i] = True

        for j in range(i + 1, len(strs)):
            # compare each string with the current string to check if they are anagrams
            if not visited[j] and is_anagram(strs[i], strs[j]):
                group.append(strs[j])
                visited[j] = True

        result.append(group)

    return result


# Approach 2: Using a hash map - group anagrams by their sorted string representation
# Time complexity: O(n * k log k), Space complexity: O(n)
def group_anagrams_with_hash_map(strs: list[str]) -> list[list[str]]:
    anagrams = {} # dictionary to store groups of anagrams

    for str_word in strs:
        # sort the string to use as a key
        key = ''.join(sorted(str_word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(str_word)

    return list(anagrams.values())

array = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams_with_brute_force(array)) # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams_with_hash_map(array)) # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
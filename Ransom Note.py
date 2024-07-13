from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_counter = Counter(magazine)
        for char in ransomNote:
            if char not in my_counter or my_counter[char] == 0:
                return False
            my_counter[char] -=1
        return True
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         new_arr = s.strip().split()
         return len(new_arr[-1])

        
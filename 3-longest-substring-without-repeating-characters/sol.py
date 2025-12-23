"""
Longest Substring Without Repeating Characters
Created: 2025-12-21

Python 3.12.3
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()  # {"char": index}
        max_len = 0
        start = 0
        length = len(s)

        for i in range(length):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            d[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len

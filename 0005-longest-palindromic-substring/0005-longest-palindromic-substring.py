class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # When the loop ends, left and right are one step beyond the valid palindrome range
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes: center is at i
            palindrome1 = expand_around_center(i, i)
            # Even-length palindromes: center is between i and i+1
            palindrome2 = expand_around_center(i, i + 1)

            # Update the longest palindrome
            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i in range(1, n + 1):
            # Option 1: Don't take a palindrome ending at index i - 1
            dp[i] = dp[i - 1]

            # Option 2: Check for a palindrome of length k ending at index i - 1
            if i >= k and is_palindrome(i - k, i - 1):
                dp[i] = max(dp[i], dp[i - k] + 1)

            # Option 3: Check for a palindrome of length k + 1 ending at index i - 1
            if i >= k + 1 and is_palindrome(i - k - 1, i - 1):
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]
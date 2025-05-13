class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1  # Base case: empty or single-node tree

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                dp[nodes] += dp[left] * dp[right]

        return dp[n]

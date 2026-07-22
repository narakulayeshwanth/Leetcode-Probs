class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:
            # Update histogram heights
            for j in range(n):
                if row[j]:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Rearrange columns optimally
            sorted_heights = sorted(heights, reverse=True)

            # Compute maximum area for this row
            for i, h in enumerate(sorted_heights):
                ans = max(ans, h * (i + 1))

        return ans
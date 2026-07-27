from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n

        for i, row in enumerate(mat):
            if i % 2 == 0:
                shifted = row[k:] + row[:k]      # Left shift
            else:
                shifted = row[-k:] + row[:-k]    # Right shift

            if shifted != row:
                return False

        return True
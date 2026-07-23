class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(matrix):
            return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
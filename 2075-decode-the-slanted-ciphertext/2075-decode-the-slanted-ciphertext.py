from typing import List

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows

        mat = []
        idx = 0
        for _ in range(rows):
            mat.append(encodedText[idx:idx + cols])
            idx += cols

        ans = []

        for c in range(cols):
            i, j = 0, c
            while i < rows and j < cols:
                ans.append(mat[i][j])
                i += 1
                j += 1

        return "".join(ans).rstrip()
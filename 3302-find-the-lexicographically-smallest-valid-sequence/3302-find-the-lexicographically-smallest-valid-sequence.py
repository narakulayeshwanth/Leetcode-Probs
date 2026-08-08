from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suf[i] = earliest index in word1 from which word2[i:] can match
        suf = [-1] * (m + 1)
        suf[m] = n

        j = n - 1
        for i in range(m - 1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j -= 1
            if j < 0:
                break
            suf[i] = j
            j -= 1

        ans = []
        pos = 0
        used = False

        for i in range(m):
            while pos < n:
                if word1[pos] == word2[i]:
                    ans.append(pos)
                    pos += 1
                    break

                if (not used) and (i == m - 1 or (suf[i + 1] != -1 and suf[i + 1] > pos)):
                    used = True
                    ans.append(pos)
                    pos += 1
                    break

                pos += 1
            else:
                return []

        return ans
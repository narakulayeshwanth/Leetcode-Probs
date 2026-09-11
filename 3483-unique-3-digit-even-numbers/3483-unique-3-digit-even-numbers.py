class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()

        for a in range(len(digits)):
            for b in range(len(digits)):
                for c in range(len(digits)):
                    if a == b or b == c or a == c:
                        continue

                    if digits[a] == 0:
                        continue

                    if digits[c] % 2 != 0:
                        continue

                    num = digits[a] * 100 + digits[b] * 10 + digits[c]
                    nums.add(num)

        return len(nums)
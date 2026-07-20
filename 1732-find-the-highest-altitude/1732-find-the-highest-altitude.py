class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        ans = 0

        for g in gain:
            altitude += g
            ans = max(ans, altitude)

        return ans
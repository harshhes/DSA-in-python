class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high%2 != 0:
            high += 1
        return high//2 - low//2
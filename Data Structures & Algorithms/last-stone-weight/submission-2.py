class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()

            if (stone1 == stone2):
                continue

            stones.append(stone1 - stone2)

        if (len(stones) == 0):
            return 0

        return stones[0]
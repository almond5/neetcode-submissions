class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = list(stones)
        heapq.heapify_max(stoneHeap)

        while(len(stoneHeap) > 1):
            stone1 = heapq.heappop_max(stoneHeap)
            stone2 = heapq.heappop_max(stoneHeap)

            if (stone1 == stone2):
                continue
            
            heapq.heappush_max(stoneHeap, stone1 - stone2)

        if (len(stoneHeap) == 0):
            return 0

        return heapq.heappop_max(stoneHeap)
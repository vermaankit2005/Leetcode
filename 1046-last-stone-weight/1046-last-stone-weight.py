import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        if (len(stones) == 1):
            return stones[0]

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            
            heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)

            diff = heaviest - second_heaviest

            if diff == 0:
                continue
            
            heapq.heappush(stones, diff)

        if len(stones) == 0:
            return 0
        return stones[0] * -1




        
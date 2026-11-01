# DP - Top Down Approch.
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        mem = {}
        def min_cost(index: int) -> int:

            if index <= 0 or index <= 1:
                return 0

            if index in mem:
                return mem[index]

            way_one_to_reach_index = cost[index-1] + min_cost(index-1)
            way_two_to_reach_index = cost[index-2] + min_cost(index-2)

            min_cost_to_reach_index = min(way_one_to_reach_index, way_two_to_reach_index)
            mem[index] = min_cost_to_reach_index
            return min_cost_to_reach_index

        return min_cost(len(cost))



        
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # init adj list
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for s, d, w in times:
            adj[s].append((d, w))
        
        heap = []
        shortest_dst = {}

        heapq.heappush(heap, (0, k))
        maximum_dst = -1

        while heap:
            cur_wt, cur_node = heapq.heappop(heap)
            if cur_node in shortest_dst:
                continue
            
            shortest_dst[cur_node] = cur_wt
            maximum_dst = max(maximum_dst, cur_wt)

            for nbr_node , nbr_wt in adj[cur_node]:
                if nbr_node in shortest_dst:
                    continue
                heapq.heappush(heap, (cur_wt + nbr_wt, nbr_node))

        if len(shortest_dst) < n:
            return -1

        return maximum_dst
            

        
        
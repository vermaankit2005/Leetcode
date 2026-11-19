import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []
        
        for src, des, wt in times:
            adj[src].append((des, wt))
        
        max_distance = float('-inf')
        shortest_distance = {}
        heap = []
        
        heapq.heappush(heap, (0, k))

        while heap:
            cnw, cn = heapq.heappop(heap)

            # Shortest path already found
            # Discard the edge
            if cn in shortest_distance:
                continue

            shortest_distance[cn] = cnw
            max_distance = max(max_distance, cnw)
            

            # Checking all the neigbors of the current node (cn)
            for des, wt in adj[cn]:
                if des in shortest_distance:
                    continue
                heapq.heappush(heap, (cnw + wt, des))
        
        if len(shortest_distance) != n:
            return -1
        
        return max_distance
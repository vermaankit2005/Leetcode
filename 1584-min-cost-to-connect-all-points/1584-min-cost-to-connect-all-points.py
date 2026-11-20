import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        
        min_distance = 0
        heap = []
        visited = set()
        adj = {}

        # init the adj list
        for i in range(len(points)):
            adj[i] = []

        # fill in all the neighbours
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # adding neighour and distance to the list
                adj[i].append((j, distance))

        # heap - (dst, node)
        heapq.heappush(heap, (0, 0))

        while heap:
            dst , cn = heapq.heappop(heap)

            if cn in visited:
                continue
            
            visited.add(cn)
            min_distance += dst

            # adding  the neighbors to the heap.
            for node, distance in adj[cn]:
                if node in visited:
                    continue
                heapq.heappush(heap, (distance, node))
            
        return min_distance



        
        
        
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adj = {}
        result = False
        answer = []

        # init the adj list.
        for i in range(numCourses):
            adj[i] = []

        for prereq, course in prerequisites:
            adj[course].append(prereq)

        path = set()

        for query in queries:
            src = query[1]
            dst = query[0]
            result = self.dfs(src, dst, path, adj)
            answer.append(result)
        
        return answer

    
    def dfs(self, src, dst, path, adj):
        if src in path:
            return False
        
        if src == dst:
            return True
        
        path.add(src)

        for prereq in adj[src]:
            if self.dfs(prereq, dst, path, adj):
                path.remove(src)
                return True
        
        path.remove(src)
        return False
        
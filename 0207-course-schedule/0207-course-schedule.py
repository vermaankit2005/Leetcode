class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        adj = {}
        result = False

        # init the adj list.
        for i in range(numCourses):
            adj[i] = []

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        path = set()

        for i in range(numCourses):
            if i in visited:
                continue
            result = self.dfs(i, path, visited, adj)
            if not result:
                return False
        
        return result

    
    def dfs(self, course, path, visited, adj):

        if course in path:
            return False
        
        if course in visited:
            return True
        
        visited.add(course)
        path.add(course)

        for prereq in adj[course]:
            if not self.dfs(prereq, path, visited, adj):
                return False
        
        path.remove(course)
        return True
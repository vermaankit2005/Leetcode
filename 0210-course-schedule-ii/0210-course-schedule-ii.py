class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adj = {}
        result = False
        order = []

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
            result = self.dfs(i, path, visited, adj, order)
            if not result:
                return []
        
        return order


    def dfs(self, course, path, visited, adj, order):

        if course in path:
            return False
        
        if course in visited:
            return True
        
        visited.add(course)
        path.add(course)

        for prereq in adj[course]:
            if not self.dfs(prereq, path, visited, adj, order):
                return False
        
        order.append(course)
        path.remove(course)
        return True
        
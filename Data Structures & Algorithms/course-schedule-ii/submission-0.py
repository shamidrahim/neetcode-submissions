class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        visit = set()
        path = set()
        topSort = []
        def dfs(src: int):
            if src in visit:
                return True
            if src in path:
                return False
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            topSort.append(src)
            visit.add(src)
            path.remove(src)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return topSort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        hm = defaultdict(list)
        visited = set()
        visiting = set()

        courseOrdering = []

        def dfs(course):
            if course in visiting:
                return True

            if course in visited:
                return False

            visiting.add(course)
            for neighbors in hm[course]:
                if dfs(neighbors):
                    return True

            courseOrdering.append(course)
            visiting.remove(course)
            visited.add(course)

            return False




        for course in prerequisites:

            hm[ course[1] ].append(course[0])
        

        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return []
       

        courseOrdering.reverse()

        return courseOrdering
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hm = defaultdict(list)
        visiting = set()
        visited = set()


        def dfs(course):
            if course in visiting:
                return True
            if course in visited:
                return False
            
            visiting.add(course)
            for neighbor in hm[course]:
                if dfs(neighbor):
                    return True   

            visiting.remove(course)   
            visited.add(course)
            return False  
            


        for edge in prerequisites:

            #prereq : list of courses it unlocks
            hm[ edge[1] ].append(edge[0])

        for course in prerequisites:
            if course[0] not in visited:
                if dfs(course[0]):
                    return False

        

        

        return True 
        
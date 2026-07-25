class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maximumArea = 0
        l = 0
        r = len(heights) - 1

        while(l < r):
            newArea =  (r - l) * min(heights[l], heights[r])
            print(newArea)
            if(maximumArea < newArea):
                maximumArea = newArea
            print("Max Area" , maximumArea, "l:", heights[l], "r:", heights[r])
            if(heights[r] > heights[l]):
                l+=1
            else:
                r -= 1
            

        return maximumArea
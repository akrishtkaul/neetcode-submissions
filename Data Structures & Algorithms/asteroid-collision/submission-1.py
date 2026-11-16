class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:

            if a < 0:
                alive = True
                while stack and stack[-1] > 0:
                    if abs(a) == abs(stack[-1]): #both asteriods destory
                        stack.pop()
                        alive = False
                        break
                    elif abs(a) > abs(stack[-1]):
                        stack.pop()
                        alive = True
                    else:
                        alive = False
                        break
                
                if alive:
                    stack.append(a)
                            
            else:
                stack.append(a)

        
        return stack
            

            


        
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

       
        cars = [[pos , ( (target - pos) / sp) ] for pos , sp in zip(position, speed)]
        sorted_cars = sorted(cars, key=lambda x: x[0])
        fleets = 0

        while(len(sorted_cars) > 0):
            currentCar = sorted_cars.pop()
            while(len(sorted_cars) > 0):
                if(currentCar[1] >= sorted_cars[-1][1]):
                    sorted_cars.pop()
                else:
                    break
            fleets += 1
    
        return fleets








           
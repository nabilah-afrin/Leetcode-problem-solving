#Leetcode daily challenge: day 06
# 04/11/2023

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        fall = [] #add ants falling off

       # ants on the left to fall
        for ant in left:
            fall.append(ant)

        #ants on the right to fall
        for ant in right:
            fall.append(n - ant)

        max_time = max(fall) #maximum time

        return max_time



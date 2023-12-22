class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # get the x coordinates and sort them
        coord = sorted([x[0] for x in points])
        
        # initialize max_width to zero
        max_width = 0
        
        # find the maximum width while iterating through the sorted x-coordinates
        for i in range(1, len(coord)):
            max_width = max(max_width, coord[i] - coord[i-1])
        
        return max_width

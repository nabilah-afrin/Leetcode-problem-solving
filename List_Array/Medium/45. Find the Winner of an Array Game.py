# leetcode daily challenge: day 07
# 05/11/23

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]  # Initialize the winner with the first element
        win_count = 0  # total win for corresponding element
        
        for position in range(1, len(arr)):
            # Compare the current element with the winner
            if arr[position] > winner:
                winner = arr[position]
                win_count = 1  # initialize the win count for new number
            else:
                win_count += 1  #if consecutively wins
            
            if win_count == k:
                return winner
        
        return winner

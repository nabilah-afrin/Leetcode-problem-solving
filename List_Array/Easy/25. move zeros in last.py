class Solution(object):
    def movezeroes(self, nums):
        # Initialize a pointer to keep track of the position to place the next non-zero element
        non_zero_index = 0
        # Traverse the array and move non-zero elements to the correct position
        for i in nums:
            if i != 0:
                nums[non_zero_index] = i
                non_zero_index += 1
        
        for remaining_numbers in range(non_zero_index, len(nums)):
            nums[remaining_numbers] = 0 #put all the element as 0
    
def test_non_zero_index():
    #take input from the user
    given_array = list(map(int,input("Enter the array elements separated by spaces: ").split()))
    solution = Solution() #create an instance of the class
    solution.movezeroes(given_array)
    print(f"Givenarray: {given_array}")

test_non_zero_index()
#test_non_zero_index([1,0,3,2])






#tribonacci series
#The Tribonacci sequence Tn is defined as follows: 
#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#Given n, return the value of Tn.

class Solution(object):
    def tribonacci(self,n):
        #handle the base case
        if n == 0:
            return 0
        elif n ==1 or n ==2:
            return 1
        #define the tribonacci sereis woth first three elements
        series = [0,1,1]
        for i in range(3,n+1):
            next_element = series[-1]+series[-2]+series[-3]
            series.append(next_element)
        return next_element
# Test code with user input
if __name__ == "__main__":
    solution = Solution()
    
    while True:
        try:
            n = int(input("Enter a non-negative integer (or a negative integer to exit): "))
            if n < 0:
                break
            output = solution.tribonacci(n)
            print(f"The {n}-th Tribonacci number is: {output}\n")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.\n")
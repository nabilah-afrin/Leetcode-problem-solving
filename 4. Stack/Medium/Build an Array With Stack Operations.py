class Solution:
    def buildArray(self, target: list[int]) -> list[str]:
        output = []
        current = 1  # Current integer in the stream n

        #iterate through numbers in target
        for num in target:
            print(f"number in target {num} and current {current}")
            #look for current stream existing in the target
            while num > current:
                output.append("Push") #if current stream not in the target
                print(f"Push {current}")
                output.append("Pop")
                print(f"Pop {current}")
                current += 1
            #current stream existing in the target
            output.append("Push")
            print(f"Push {current}")
            current += 1
        
        return output
    
solution = Solution()
target = [1,3]
result = solution.buildArray(target)
print(result)

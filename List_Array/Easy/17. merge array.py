class Solution(object):
    def merge(self,num1,m,num2,n):
        #initialize an empty array to store the merged data
        result = []
        i = 0
        j = 0
        while i<m and j<n:
            if num1[i] < num2[j]:
                result.append(num1[i])
                i += 1
            else:
                result.append(num2[j])
        #add the remaining elemensts
        if i<m:
            result.extend(num1[i:m])
        if j<n:
            result.extend(num2[j:n])
        for k in range(m+n):
            num1[k] = result[k]
            
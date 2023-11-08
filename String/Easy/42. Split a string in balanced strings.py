"""Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Constraints:
2 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string."""
class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        r = 0
        l = 0
        for char in s:
            if char =="R": r+=1
            elif char == "L": l+=1
            if l==r: count+=1
        return count
solution = Solution()
result = solution.balancedStringSplit("RLRRRLLRLL")
print(result)

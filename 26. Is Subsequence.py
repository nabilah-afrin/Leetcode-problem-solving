#Is Subsequence?
#Given two strings s and t, 
#return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
class solution(object):
    def subsequence(self, s:str, t:str):
        i, j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
            j += 1
        return i == len(s)  

#test case
def test_subsequence():
    s = solution()
    string_testing = int(input("Enter the number of test cases:"))
    for _ in range(string_testing): 
        s_string = input("S: ")
        t_string = input("T: ")
        result = s.subsequence(s_string, t_string)
        print(f"Result for s='{s_string}', t='{t_string}': {result}")

test_subsequence()

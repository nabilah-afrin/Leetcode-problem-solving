class Solution(object):
    def reverse_vowel(self, s):
        vowels = "AEIOUaeiou"
        s_list = list(s)
        # initialize two pointers, one from the start and one from the end
        start_pointer = 0
        end_pointer = len(s_list)-1
        while start_pointer < end_pointer:
            # if the left pointer is not a vowel, move it to the right
            #s_list[position number of]
            # if the left pointer is not a vowel, move it to the right
            if s_list[start_pointer] not in vowels:
                start_pointer += 1
            # if the right pointer is not a vowel, move it to the left
            elif s_list[end_pointer] not in vowels:
                end_pointer -= 1
            # if both pointers are vowels, swap them and move both pointers

            else:
                s_list[start_pointer] = s_list[end_pointer]
                s_list[end_pointer] = s_list[start_pointer]
                start_pointer += 1
                end_pointer -= 1

            # return the modified list as a string
            return "".join(s_list)


#test case
def test_reverse_vowel(given_string):
    solution = Solution()
    result = solution.reverse_vowel(given_string)
    print(f"Given string: {given_string}")
    print(f"Output: {result}\n")

# Test cases
test_reverse_vowel("hello")
test_reverse_vowel("LeetCode")
test_reverse_vowel("aA")
test_reverse_vowel("abcde")
test_reverse_vowel("rhythm")
test_reverse_vowel("I love Python")
test_reverse_vowel("aeiou")
test_reverse_vowel("AEIOU")
test_reverse_vowel("Test case")
test_reverse_vowel("")
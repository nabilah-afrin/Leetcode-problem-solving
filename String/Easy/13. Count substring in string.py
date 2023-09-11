def count_substring(string, sub_string):
    n = len(sub_string) #n= size of substring
    ans = 0
    for i in range(0,len(string)):
        ans+=string.count(sub_string,i,i+n)
    return ans
 if__name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

def count_substring(string, sub_string):
    newstring= string.find(sub_string)
    return newstring
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

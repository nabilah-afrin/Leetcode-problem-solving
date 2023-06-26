def split_and_join(line):
    line = "-".join(line)
Output: t-h-i-s- -i-s- -a- -s-t-r-i-n-g
def split_and_join(line):
    line= str(line)
    line= line.split(" ") # converted to a list of strings = ['this', 'is', 'a', 'string']
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

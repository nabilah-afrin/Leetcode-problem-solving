#digit count using recusrsion
"""
100
-> 3

50
-> 2

1999
-> 4
"""

# Base: [1-9] -> return 1
# Recursion:
"""
100 // 10 = 
"""
print(100//10)
print(10//10)

"""
1 + 
"""


def digitCount(number:int):
    total_digit =0
    if number <10: return 1
    else:
        number= str(number)
        total_digit+=1
        
        return total_digit+ digitCount(int(number[:-1]))
n=100
result = digitCount(n)
print(result)


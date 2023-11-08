"""
python
>> nohtyp

Reverse Order
"""
def reverseString(word:str):
    if len(word) ==0:
        return ""

# Recursive:
    return reverseString(word[:-1]) + word[-1]

print(reverseString(word="python"))
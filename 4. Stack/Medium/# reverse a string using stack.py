# reverse a string using stack
def string_reverse(word:str):
    stack = []
    for character in word:
        stack.append(character)
    
    reverse = ""
    while stack: #always set this condition for 
        reverse+= stack.pop()
    
    return reverse
result = print(string_reverse("abcde"))
def decimal_to_binary(n):
    if n == 0: return "0"
    elif n == 1: return "1"
    else:
        quotient = n//2 #we dont want float numbers, only whole numbers
        remainder = n%2
        return decimal_to_binary(quotient) + str(remainder)
decimal_number = 10
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)

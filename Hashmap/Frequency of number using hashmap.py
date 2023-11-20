def frequency_with_hashmap(arr):
    frequency_map = {}
    
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    return frequency_map
print(frequency_with_hashmap([1,2,2,7,4,7,8,7]))

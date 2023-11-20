# bubble sort has two operations: comparing between two consecutive indexes and putting the maximum value at the last index
# the comparison index will be dependent on the last_index
# the last index will start from len(list)-1  and go down to the second index(1)
# for the inner loop for comparison, i will start from 0 and it will go upto the index just before last index

"""def bubble_sort(lst):
    n = len(lst)
    for j in range(n):
        inner_loop = n-j-1
        print("Inner Loop for comparison range: ",inner_loop)
        for i in range(inner_loop):
            print(f"Outer Index J: {j} and Inner Index I: {i}")
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            print(lst)
lst = [-20, 450, 1, 101, -90]  # [-90, -20, 1, 101, 450]
bubble_sort(lst)"""


def bubble_sort_optimized(lst):
    n = len(lst)
    #start the outer loop to put maximum value
    #this one will interate for the entire list index
    for j in range(n): #iterate over the full lsit
        #initialize a flag variable to False whether any swaps were made in the current pass
        swapped = False
        
        #start the inner loop to compare between two indexes
        for i in range(0, n-1-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                #as swap p[eration happended, put the swap flag as True]
                swapped = True
                
        # If no swaps were made in this pass, the list is already sorted
        #so break the outer loop
        if not swapped: #swap has not been true, still false
            break
                
        

# Example usage
my_list = [-20, 300, 450, 1, 101]
my_list=[5, 2, 1, 8, 4]
bubble_sort_optimized(my_list)
print(my_list)

def bubble_sort(list): 
    unsorted_until_index = len(list) - 1 
    sorted = False
    while not sorted: 
        sorted = True 
        for i in range(unsorted_until_index): 
            if list[i] > list[i+1]: 
                list[i], list[i+1] = list[i+1], list[i] 
                sorted = False
        unsorted_until_index -= 1
    return list
print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))



[1441. Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=daily-question&envId=2023-11-03)

The given problem takes a list called "target" as an input, as well as an integer "n"; based on the numbers present in the list, the function will show an output with stack operation.
The problem is quite easy, but the poor description makes it complicated.

The stream of numbers will start from 1, and look for itself in the target list. If the number is present in the target, then we will have to push it in the output stack; otherwise, if the stream number is not present in the target list, then at first push it and pop it from the output stack. the streaming will continue until it reaches the maximum value of the target list.

It seemed quite unnecessary for the input integer "n" as the stream value's limit is dependent on the maximum value of the target element. Hence, the function runs smoothly with only one argument"target". So, while running it in the local environment, I ran the function with the target list only.

Algorithm Step:

1. Create an empty list to put the push/pop operation
2. Define a variable that will be compared with the target list
3. Iterate through the target array.
4. For each number in the target array,  check if the current number in the stream is equal to the target number.
5. If not, use a combination of "Push" and "Pop" operations until the current number matches the target number.
6. Once the current number matches the target number, add a "Push" operation to the output list.
7. Continue this process for all numbers in the target array.

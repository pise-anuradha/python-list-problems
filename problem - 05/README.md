# Problem - 05

Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings.

# Problem Statement

The task is to create a Python program that counts the number of strings in a given list where the string length is 2 or more and the first and last character are the same.

## Approach

The approach involves iterating through each string in the list and checking if its length is 2 or more and if the first and last characters are the same.

### Steps

1. Iterate through each string `i` in the given list.
2. Check if the length of the string `i` is greater than or equal to 2 using the `len()` function.
3. Check if the first character of the string `i` is equal to the last character of the string `i` using indexing (`i[0]` and `i[-1]`).
4. If both conditions are true, increment the count variable `total`.
5. After iterating through all strings in the list, print the total count of strings that satisfy the given conditions.

### Solution Explanation

This solution iterates through each string in the list. For each string, it checks if its length is 2 or more (`len(i) >= 2`) and if the first and last characters are the same (`i[0] == i[-1]`). If both conditions are met, it increments the count. Finally, it prints the total count of strings that satisfy the given conditions.



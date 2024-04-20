# Problem - 03

Write a Python program to get the largest number from a list.

# Problem Statement

The task is to create a Python program that finds the largest number from a given list. Four solutions are provided, each with its own approach.

# Solution - 1

### Approach:
Use the `max()` function to find the largest number in the list.

### Steps:
1. Define a list containing the elements.
2. Use the `max()` function to find the largest number in the list.
3. Print the largest number.

### Solution Explanation:
This solution is straightforward and efficient. It directly applies the `max()` function to the list to obtain the largest number.

# Solution - 2

### Approach:
Allow the user to input the number of elements and the elements themselves, then find the largest number.

### Steps:
1. Prompt the user to input the number of elements.
2. Use a loop to input each element and add it to the list.
3. Use the `max()` function to find the largest number in the list.
4. Print the largest number.

### Solution Explanation:
In this solution, the program interacts with the user to input the elements of the list dynamically. It then finds the largest number using the `max()` function. This approach is useful when the list elements are not known beforehand and need to be provided by the user.

# Solution - 3

### Approach:
Iterate through the list and compare each element with the current largest number found so far.

### Steps:
1. Define a list containing the elements.
2. Initialize a variable `largest` with the first element of the list.
3. Iterate through each element `num` in the list.
4. If `num` is greater than `largest`, update `largest` to `num`.
5. Print the largest number.

### Solution Explanation:
This solution iterates through the list and compares each element with the current largest number found so far. If an element is greater than the current largest, it updates the largest number.

# Solution - 4

### Approach:
Allow the user to input the number of elements and the elements themselves, then find the largest number without using the `max()` function.

### Steps:
1. Prompt the user to input the number of elements.
2. Use a loop to input each element and add it to the list.
3. Initialize a variable `largest` with the first element of the list.
4. Iterate through each element `num` in the list.
5. If `num` is greater than `largest`, update `largest` to `num`.
6. Print the largest number.

### Solution Explanation:
This solution is similar to Solution 3 but also allows the user to input the elements of the list dynamically. It finds the largest number without using the `max()` function.


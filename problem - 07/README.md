# Problem - 07

Write a Python program to remove duplicates from a list.

# Problem Statement

The task is to create a Python program that removes duplicate elements from a given list.

# Solution - 1

### Approach

The approach involves iterating through the list and maintaining a separate list to store unique elements. For each element in the original list, check if it is already present in the new list. If not, add it to the new list.

### Steps

1. Define a function `remove_duplicate()` to handle the removal of duplicates.
2. Prompt the user to input the number of elements.
3. Initialize an empty list `num_list` to store the elements.
4. Initialize an empty list `new_list` to store unique elements.
5. Use a loop to input each element and add it to the `num_list`.
6. Iterate through each element `i` in the `num_list`.
7. If `i` is not already in `new_list`, append it to `new_list`.
8. Return `new_list` containing unique elements.

### Solution Explanation

This solution defines a function `remove_duplicate()` that iterates through the list and maintains a separate list `new_list` to store unique elements. For each element in the original list, it checks if it is already present in `new_list`. If not, it adds it to `new_list`. Finally, it returns `new_list` containing unique elements.

# Solution - 2

### Approach

The approach involves using the `set()` function to remove duplicates directly from the list.

### Steps

1. Define a function `remove_dup()` to handle the removal of duplicates.
2. Prompt the user to input the number of elements.
3. Initialize an empty list `num_list` to store the elements.
4. Use a loop to input each element and add it to the `num_list`.
5. Use the `set()` function to remove duplicates from `num_list`.
6. Print the resulting set.

### Solution Explanation

This solution defines a function `remove_dup()` that uses the `set()` function to remove duplicates directly from the list. It converts the list to a set, which automatically removes duplicate elements, and then prints the resulting set.



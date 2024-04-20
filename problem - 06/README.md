# Problem - 06

Write a Python program to get a list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

##Problem Statement

The task is to create a Python program that sorts a list of non-empty tuples in increasing order based on the last element of each tuple.

# Solution - 1

## Approach

The approach involves using the `sort()` method with a custom key function to sort the list based on the last element of each tuple.

### Steps

1. Define the sample list of tuples.
2. Use the `sort()` method with a lambda function as the key to sort the list based on the last element of each tuple.
3. Print the sorted list.

### Solution Explanation

This solution sorts the sample list of tuples in increasing order by the last element of each tuple using the `sort()` method with a lambda function as the key. This lambda function extracts the last element of each tuple for comparison during sorting.

# Solution - 2

## Approach

The approach involves defining a custom key function and using the `sorted()` function to sort the list based on the last element of each tuple.

### Steps

1. Define the sample list of tuples.
2. Define a custom key function `sort_by_last_element(t)` that returns the last element of a tuple `t`.
3. Use the `sorted()` function with the custom key function to sort the list based on the last element of each tuple.
4. Print the sorted list.

### Solution Explanation

This solution defines a custom key function `sort_by_last_element(t)` that extracts the last element of a tuple `t`. It then uses the `sorted()` function with this custom key function to sort the sample list of tuples in increasing order based on the last element of each tuple.



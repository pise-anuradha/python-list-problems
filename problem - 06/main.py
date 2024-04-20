####################### SOLUTION - 1 ####################### 

sample_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]

sample_list.sort(key = lambda x: x[-1])

print(sample_list)

####################### SOLUTION - 2 ####################### 

# Sample list of tuples
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Define a custom key function to sort by the last element of each tuple
def sort_by_last_element(t):
    return t[-1]

# Sort the list based on the custom key function
result = sorted(sample_list, key=sort_by_last_element)

# Print the sorted list
print(result)

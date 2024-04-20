####################### SOLUTION - 1 ####################### 

list3 = [10,25,36,44,78,3.25,64,23]
print(f'The largest number is {max(list3)}')

####################### SOLUTION - 2 ####################### 

list3 = []
num_elements = int(input('Enter the number of elements: '))
for i in range(num_elements):
  element = float(input(f'Enter the {i+1} element: '))
  list3.append(element)

print(f'The largest number in the list is {max(list3)}')

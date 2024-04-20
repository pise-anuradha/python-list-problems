####################### SOLUTION - 1 ####################### 

list4 = [10,25,36,44,78,3.25,64,23]
print(f'The smallest number is {min(list4)}')

####################### SOLUTION - 2 ####################### 

list4 = []
num_elements = int(input('Enter the number of elements: '))
for i in range(num_elements):
  element = float(input(f'Enter the {i+1} element: '))
  list4.append(element)

print(f'The smallest number in the list is {min(list4)}')

####################### SOLUTION - 3 ####################### 

list4 = [10,25,36,44,78,3.25,64,23]

smallest = list4[0]

for num in list4:
  if num < smallest:
    smallest = num

print(f'The smallest number in the list is {smallest}')

####################### SOLUTION - 4 ####################### 

list4 = []
num_elements = int(input('Enter the number of elements: '))
for i in range(num_elements):
  element = float(input(f'Enter the {i+1} element: '))
  list4.append(element)

smallest = list4[0]

for num in list4:
  if num < smallest:
    smallest = num

print(f'The smallest number in the list is {smallest}')

####################### SOLUTION - 1 ####################### 

list1 = [20,14,3.6,8,65,22,2.014,2.36]
total = 0
for i in list1:
  total += i
print(f'The Sum of elements is {total}')

####################### SOLUTION - 2 ####################### 

list1 = []
num_elements = int(input('Enter the number of elements :'))  #no of elements in list

for i in range(num_elements):
  element = float(input(f'Enter the element {i+1}:'))     #take element as input
  list1.append(element)   #add elements in the list

total = sum(list1)   # sum of all elements in the list
print(f'The sum of all elements is {total}')

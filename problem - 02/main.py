####################### SOLUTION - 1 ####################### 

list2 = [20,14,3.6,8,65,22,2.014,2.36]
product = 1
for i in list2:
  product *= i
print(f'The product of elements is {product}')

####################### SOLUTION - 2 ####################### 

list2 = []
num_elements = int(input('Enter the number of elements:'))
product = 1
for i in range(num_elements):
  element = float(input(f'Enter the {i+1} element: '))
  list2.append(element)

for j in list2:
  product *= j

print(f'The product of elements is {product}')

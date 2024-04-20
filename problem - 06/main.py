####################### SOLUTION - 1 ####################### 

#num_list = [1,5,6,9,8,7,5,3,6,4,9,8,5,3,4] 

def remove_duplicate():
  num = int(input('Enter the number of elements : '))
  num_list = []
  new_list = []
  for n in range(num):
    element = float(input(f'Enter the {n+1} element :'))
    num_list.append(element)
  for i in num_list:
    if i not in new_list:
      new_list.append(i)

  return new_list

remove_duplicate()

####################### SOLUTION - 2 ####################### 

#num_list = [1,5,6,9,8,7,5,3,6,4,9,8,5,3,4]

def remove_dup():
  num_list = []
  number = int(input('Enter the number of elements : '))
  for n in range(number):
    element = float(input(f'Enter the {n+1} element : '))
    num_list.append(element)
  print(set(num_list))

remove_dup()

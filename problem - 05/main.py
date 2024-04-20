sample_list = ['abc', 'xyz', 'aba', '1221']
total = 0
for i in sample_list:
  if len(i) >= 2 and i[0] == i[-1]:
    total += 1
print(f'The count is : {total}')

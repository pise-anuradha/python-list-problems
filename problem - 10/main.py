list10 = ['Sakshi','Apurvaa','Shruti','Radha','Asha','Nutan','Pranjali']
def wordCount(listName):
  count = []
  length = int(input('Enter the length  : '))
  for l in listName:
    if len(l)>length:
      count.append(l)
  return count
wordCount(list10)

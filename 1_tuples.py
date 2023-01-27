####### PART 1 #######
# Defining function which takes element and determines whether it is in the values tuple
def find_element(values, element):
  if element in values:
    print(True)
  else:
    print(False)

# Calling the function
find_element((1, 2, 3, 4), 5)
print('\n-------- END PART 1 --------\n')

####### PART 2 #######
# Defining function which removes duplicates in values
def remove_duplicates(values):
  new_list = []

  # for loop which compares each value in values to new list
  for value in values:

    # if value is not in new_list then add value to new_list
    if value not in new_list:
      new_list.append(value)

  print(new_list)

# Assigning a list to values and calling the function
values = [1,2,3,3,4,5,5]
remove_duplicates(values)
print('\n-------- END PART 2 --------\n')

####### PART 3 #######
# Defining
def myNumbers(values):
  result = []
  for value in values:
    if value % 2 == 0:
      result.append((value, 'even'))
    else:
      result.append((value, 'odd'))
  print(result)
myNumbers([3,6,1,12])

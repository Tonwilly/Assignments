my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting into 2nd position
my_list.insert(1, 15)

# extending list
another_list = [50, 60,70]

#my_list += another_list
my_list.extend(another_list)

# removing last element
del my_list[-1]

# sorting
my_list.sort(reverse=True)

# find and print index of certain value
print(my_list.index(30))
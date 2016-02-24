# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# Let's store our counts in a list of length 11
# with zeros filled in.

# We can multiply a list construct to create a list with the same
# elements n number of times.

# Here's our code that we coded before

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0, 10))
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10.
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4,
# we assign count_list[4] = 3, if there are 5 occurrences of the
# number 6, we assign count_list[6] = 5

count_list = [0] * 11
index = 0

# Write code here to loop through every number in random_list and
# update count_list appropriately

count = 0
'''
while index < len(random_list):
    number = random_list[index]
    count_list[number] += 1
    index += 1
'''
for num in random_list:
    count_list[num] += 1

# Check the list we created
print random_list
print count_list
# If we coded everything correctly, the sum of all of the numbers
# in count_list should be 20
print sum(count_list)

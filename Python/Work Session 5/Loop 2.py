# Know we want to ask our self the question:
# How many occurrences of the number 9 appear in our randomly made list?
# For example if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to go loop through the list and count how many occurrences of the
# number 9. In this example, the number 9 occurs 3 times in the example
# list

import random

# 1. Create random list of integers using while loop
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0, 10))

# Write code here to loop through the list and count all occurrences
# of the number 9. If statements and While loops will help you solve
# this problem.
count = 0
index = 0

while index < len(random_list):
    if random_list[index] == 9:
        count += 1
    index += 1

'''
for number in random_list:
    if number == 9:
        count += 1
'''

# Test if our While loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list
print count

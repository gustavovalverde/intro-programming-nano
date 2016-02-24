# We now would like to summarize this data and make it more visually
# appealing.

# We want to go through count_list and print a table that shows
# the number and its corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""
# Here is our code we have written so far:

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0, 10))

# Aggregate the data -------------------------------------------------
count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] += 1
    index += 1

# Write code here to summarize count_list and print a neatly formatted
# table that looks like this:

"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""

print count_list
print sum(count_list)

# Hint: To print 10 blank spaces in a row, we can multiply a string
# by a number "n" to print this string n number of times:

print "number | ocurrence"
index = 0
while index <= 10:
    if index < 10:
        print " " * 5 + str(index) + " | " + str(count_list[index] * "*")
    else:
        print " " * 4 + str(index) + " | " + str(count_list[index] * "*")
    index += 1
print ""
print "-----------------"
print "Another approach"
print "-----------------"
print ""

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
    num_spaces = num_len - len(str(index))
    print " " * num_spaces + str(index) + " | " + str(count_list[index])
    index = index + 1

# BONUS!
# From your summarize code you just wrote, can you make the table even
# more visual by replacing the count with a string of asterisks that
# represent the count of a number. The table should look like:

"""
number | occurrence
     0 | *
     1 | **
     2 | ***
     3 | **
     4 | **
     5 | *
     6 | *
     7 | **
     8 | ***
     9 | *
    10 | **
"""

# Congratulations! You just created a distribution table of a list
# of numbers! This is also known as a histogram

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

num_list = [row[0] for row in texts]

numbers = set()

for i in range(2):
    text_list = [row[i] for row in texts]
    numbers.update(num_list)

    call_list = [row[i] for row in calls]
    numbers.update(call_list)

print("There are %d different telephone numbers in the records." % (len(numbers)))
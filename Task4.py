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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = [row[0] for row in calls]
receivers = [row[1] for row in calls]
not_spam = set()

for text, receiver, in zip(texts, receivers):
    for i in range(2):
        not_spam.add(text[i])
    not_spam.add(receiver)

telem_calls = sorted(set([num for num in callers if num not in not_spam]))

print("These numbers could be telemarketers: ")
for n in telem_calls:
    print(n)
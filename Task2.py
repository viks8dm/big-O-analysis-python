"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

only_received = dict()
caller = {row[0]: int(row[-1]) for row in calls}
receiver = {row[1]: int(row[-1]) for row in calls}
for (c,c_time), (r,r_time) in zip(caller.items(), receiver.items()):
    if c in receiver.keys():
        caller[c] = c_time + receiver[c]
    if r not in caller.keys():
        only_received[r] = r_time

caller.update(only_received)

tel_num = max(caller, key=caller.get)
max_time = caller[tel_num]

print("%s spent the longest time, %d seconds, on the phone during September 2016." % (tel_num, max_time))
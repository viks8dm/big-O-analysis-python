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

num_time_dict = dict()
for call in calls:
    num_time_dict[call[0]] = 0
    num_time_dict[call[1]] = 0

for num in num_time_dict:
    for call in calls:
        for i in range(2):
            if call[i] == num:
                num_time_dict[num] += int(call[3])

tel_num = max(num_time_dict, key=num_time_dict.get)
max_time = num_time_dict[tel_num]

print("%s spent the longest time, %d seconds, on the phone during September 2016." % (tel_num, max_time))

# Investigating Texts and Calls

## Overview

Completed five tasks based on a fabricated set of calls and texts exchanged. Use Python to analyze and answer questions about the texts and calls contained in the dataset. Perform run time analysis of solution and determine its efficiency.

Download and open the zipped folder [here](https://s3.amazonaws.com/udacity-dsand/P0.zip). In the folder you will find five python files `Task0.py`, `Task1.py`, ...,`Task4.py` and two csv files `calls.csv` and `texts.csv`

About the data
The text and call data are provided in csv files.

The text data (`text.csv`) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (`call.csv`) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

* Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
* Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
* Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".
Step 2 - Implement the Code
Complete the five tasks (Task0.py, Task1.py, ...,Task4.py). Do not change the data or instructions, simply add your code below what has been provided. Include all the code that you need for each task in that file.

The solution outputs for each file should be the print statements described in the instructions.

## Big-O analysis of implementation

#### Task-0

O(1):
* first record access = O(1)
* last record access = O(1)

result = 2*O(1) = O(1)

#### Task-1

O(n):
* for loop over texts: O(n)
* set() assignment: O(1)
* for loop over text_list and call_list: O(n) + O(m)

result = O(1) + 2*O(n) + O(m) = O(n)

#### Task-2

O(n<sup>2</sup>)
* dict() initialization: O(1)
* call for loops: O(n)
* nested for-loop over num and call: O(2* n * n)
* max computation: O(n)
* max_time: O(1)

result: 2* O(1) + 2* O(n)  + O(2* n * n) = O(n * n)

#### Task-3

O(n logn)
* for loop: O(n)
* set with for loop: O(n)
* set initialization: O(1)
* for with if statements: O(n)
* sorting: O(n logn)
* print with for-loop: O(n) + O(1)
* for with print and percent-calculation: O(n) + O(1)

result: O(n logn) + 5* O(n) + 3* O(1)

#### Task-4

O(n<sup>2</sup>)
* caller and receiver for loops: 2* O(n)
* set initialization: O(1)
* nested for-loop and add: O(n * n) + O(1)
* sorting: O(n logn)
* print and for-loop: O(1) + O(n)

result: 3* O(1) + 3* O(n) + O(n logn) + O(n * )

## Reference:

* [python time complexity](https://wiki.python.org/moin/TimeComplexity)

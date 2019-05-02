import csv
"""
# Reading from a CSV file is done using the reader object
#  using the with keyword (introduced in python 2.5)
#  to wrap our code for opening a file object, the internals of Python will do something similar to the following
#  code to ensure that no matter what the file object is closed after use
with open('1.txt') as fp:
    fp = csv.reader(fp, delimiter = ',')
    line_count = 0
    for row in fp:
        # row will be list of words separated by delimiter
        if line_count == 0:
            # f is used for format option
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    
"""

# Reading specific rows
with open('1.txt') as fp:
    fp = csv.reader(fp, delimiter = ',')
    included_cols = [1, 2]
    content = []
    for row in fp:
        #content = list(row[i] for i in included_cols)
        for i in included_cols:
            content = ([row[i], row[1]+row[2]])
        print(content)


import csv

with open('employee_file.csv', mode='w') as employee_file:
    # The special nature of your chosen delimiter is ignored in quoted strings; use quote char
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
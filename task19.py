import csv
input_f = "Input/grades.csv"
output = "Output/output19.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
with open(output, 'w') as w:
    w.write('\n'.join(folder))
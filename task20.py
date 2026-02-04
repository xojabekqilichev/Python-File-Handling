import csv
input_f = "Input/grades.csv"
output = "Output/output20.txt"
with open(input_f, 'r') as x:
    folder = csv.reader(x)
    head = next(folder)
    with open(output, 'w') as w:
        for i in folder:
            w.write(f'Talaba: {i[0]}, Ball: {i[1]}\n')
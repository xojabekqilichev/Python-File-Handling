import csv
input_f = "Input/grades.csv"
output = "Output/output21.txt"
with open(input_f, 'r') as x:
    folder = list(csv.reader(x))
    head = folder.pop(0)
    result = sorted(folder, key=lambda i: int(i[1]), reverse=True)
    with open(output, 'w') as w:
        w.write(f'Top reyting: {result[0]} ({result[1]} ball)')
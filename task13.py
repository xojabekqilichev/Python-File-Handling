input_f = "Input/students.txt"
output = "Output/output13.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
    reads = sorted(folder)
with open(output, 'w') as w:
    w.write('\n'.join(reads))
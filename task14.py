input_f = "Input/students.txt"
output = "Output/output14.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
    reads = sorted(folder, key=lambda x: x[-1])
with open(output, 'w') as w:
    w.write('\n'.join(reads))
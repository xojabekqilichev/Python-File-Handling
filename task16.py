input_f = "Input/students.txt"
output = "Output/output16.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
    l = []
    for i in folder:
        if len(i) > 5:
            reads = l.append(i)
with open(output, 'w') as w:
    w.write('\n'.join(l))
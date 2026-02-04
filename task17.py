input_f = "Input/students.txt"
output = "Output/output17.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
    li = []
    for i in folder:
        if i.startswith('A'):
            li.append(i)
            
with open(output, 'w') as w:
    w.write('\n'.join(li))
input_f = "Input/students.txt"
output = "Output/output15.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
   
with open(output, 'w') as w:
    for i in folder:
        res = len(i)
        w.write(f'{i} ismi {res} harfdan iborat\n')
input_f = "Input/students.txt"
output = "Output/output11.txt"
with open(input_f, 'r') as x:
    folder = x.read()
with open(output, 'w') as w:
    w.write(f'{folder}\n')
input_f = "Input/students.txt"
output = "Output/output12.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
    r = len(folder)
with open(output, 'w') as w:
    w.write(f'Ismlar soni {r} ta')
input_f = "Input/numbers.txt"
output = "Output/output09.txt"
with open(input_f, 'r') as file:
    asd = file.read().split()
    first = []
    second = []
    third = []
    for i in asd:
        if len(i) == 1:
            result = first.append(f'bir xonali sonlar:{i}')
        elif len(i) == 2:
            rd = second.append(f'ikki xonali sonlar:{i}')
        elif len(i) == 3:
            s = third.append(f'uch xonali sonlar:{i}')
with open(output, 'w') as files:
    files.write(f'{first}\n')
    files.write(f'{second}\n')
    files.write(f'{third}\n')
            
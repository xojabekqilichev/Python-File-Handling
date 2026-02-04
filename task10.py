input_f = "Input/numbers.txt"
output = "Output/output10.txt"
with open(input_f, 'r') as file:
    result = file.read().split()
    num = [int(i) for i in result]
sorted_num = sorted(num)
with open(output, 'w') as files:
    for i in sorted_num:
        files.write(f'{i}\n')

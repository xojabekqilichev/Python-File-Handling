input_f = 'input.txt'

with open(input_f, 'rb') as file:
    print(file.tell())
    print(file.read(90))
    print(file.tell())
    file.seek(-80, 1)
    print(file.read(10))
    print(file.tell())
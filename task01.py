with open('Input/numbers.txt', 'r') as f:
    c = f.read()
    with open('Output/output01.txt', 'w') as g:
        result = g.write(c)
        print(result)
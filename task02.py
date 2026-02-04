total = 0
with open('Input/numbers.txt', 'r') as f:
    
    for i in f:
        total = total + int(i.strip())
with open('Output/output02.txt', 'w') as g:
        d = g.write(str(total))
        print(d)
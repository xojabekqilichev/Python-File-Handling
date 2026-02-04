total = 0
with open('Input/numbers.txt', 'r') as f:
    
    for i in f:
        son = int(i.strip())
        if total < son:
            total = son
with open('Output/output03.txt', 'w') as g:
        d = g.write(str(total))
        print(d)
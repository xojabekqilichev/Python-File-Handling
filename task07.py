juft_sonlar = []

with open('Input/numbers.txt', 'r') as f:
    for line in f:
        son = int(line.strip()) **2 
        l = juft_sonlar.append(son)      
with open('Output/output07.txt', 'w') as g:
    g.write(str(l))
print(l)
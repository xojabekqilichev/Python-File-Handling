jami_summa = 0
soni = 0

with open('Input/numbers.txt', 'r') as f:
    for line in f:
        if line.strip():
            jami_summa += int(line.strip())
            soni += 1

ortacha = jami_summa / soni if soni > 0 else 0
with open('Output/output05.txt', 'w') as g:
    result = g.write(str(ortacha))
    print(result)
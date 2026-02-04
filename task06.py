toq_sonlar = []

with open('Input/numbers.txt', 'r') as f:
    for line in f:
        son = int(line.strip()) 
        if son % 2 == 1:       
            toq_sonlar.append(str(son)) 
with open('Output/output06.txt', 'w') as g:
    natija = "\n".join(toq_sonlar) 
    g.write(natija)

print("Toq sonlar ko'chirildi!")
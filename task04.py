juft_sonlar = []

with open('Input/numbers.txt', 'r') as f:
    for line in f:
        son = int(line.strip()) 
        if son % 2 == 0:       
            juft_sonlar.append(str(son)) 
with open('Output/output04.txt', 'w') as g:
    natija = "\n".join(juft_sonlar) 
    g.write(natija)

print("Juft sonlar ko'chirildi!")
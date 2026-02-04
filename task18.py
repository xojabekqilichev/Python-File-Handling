input_f = "Input/students.txt"
output = "Output/output18.txt"
with open(input_f, 'r') as x:
    folder = x.read().split()
    f = []
ism = input('Qidirilayotgan ism >>> ')
for i in folder:
    if ism.lower() in i.lower():
        f.append(i) 
with open(output, 'w') as w:
    if f: 
         w.write('\n'.join(f))
    else:
        print('Kechirasiz, bunday ism ro\'yxatda yo\'q.')
c = list()

for i in range(4):
    c.append([])
    for j in range(3):
        c[i].append(int(input(f'Digite um número para add na posição c[{i}][{j}]: ')))
        
ct = list()

for i in range(len(c[0])):
    ct.append([])
    for j in range(len(c)):
        ct[i].append(c[j][i])

for i in c: print(i)
print()
for i in ct: print(i)
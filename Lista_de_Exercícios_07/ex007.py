from random import randint

vetor_A = list()
vetor_B = list()

# ----- gerando vetor A ----- #

quant = randint(1,10)
cont = 0
while cont < quant:
    n = randint(0,99)
    if n not in vetor_A:
        vetor_A.append(n)
        cont += 1

# ----- gerando vetor B ----- #

quant = randint(1,10)
cont = 0
while cont < quant:
    n = randint(0,99)
    if n not in vetor_A:
        vetor_B.append(n)
        cont += 1

# ----- gerando vetor C ----- #

vetor_C = vetor_A + vetor_B

# ----- printando vetores --- #

print(vetor_A)
print(vetor_B)
print(vetor_C)
#crie um jogo da forca
from biblioteca import *

animal = ["h","i","p","o","p","o","t","a","m","o"]

A = [""]*6

for x in range(6):
    letra = input('Digite uma letra: ')
    A[x] = letra
    if letra in animal:
        print(A[x])
    else:
        print('Não tem essa letra!')


resultado = vetor(animal,A)

print(resultado)



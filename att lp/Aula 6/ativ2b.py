soma = 0

n = int(input("Digite a quantidade de números:"))

for i in  range(1, n + 1):
    num = int(input("Digite um número:"))
    soma += num

if soma % 2 == 0:
    print("A soma dos números é par.")
else :
    print("A soma dos números é ímpar.")
a = [] #Listas
b = {} # Dicionários
c = () # Tuplas

d=1
while d <= 100:
    a.append(d)
    b[d] = d
    c = c + (d,)
    d +=1
    

print(list(reversed(a)))

for valor in reversed(b.values()):
    print(valor)
    
print(tuple(reversed(c)))
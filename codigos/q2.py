import math

print("vamoos verificar se valores que você digitar formam um triangulo!")
a = int(input("digite o valor do primeiro segmento: "))
b = int(input("agora o valor do segundo segmento: "))
c = int(input("agora o valor o terceiro segmento: "))

if a<b+c and b<a+c and c<a+b:
    s = (a + b + c)/2 #semiperimetro
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) #formula de heron pra saber a area
    print("os valores formaram um triangulo de area igual a %.2f" % (area))
else:
    print("os valores nao formam um triangulo")

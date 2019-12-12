# 1- Soma
n1 = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
resultado_soma = n1+n2

print(resultado_soma)

# 2- Multiplicação
n1 = int(input("Digite um numero"))
n2 = int(input("Digite um número"))
resultado_mul = n1*n2

print(resultado_mul)

# 3- Par ou Impar
numero = float(input("Digite um número para saber se é ou não:"))
resto = numero %2

if resto == 0 :
    print("Número é par")
else:
    print("Número é impar")

# 4- Celsius para Fahrenheit
c = int(input("Digite a temperatura em celsius"))
coeficiente = (9/5)
f = c*coeficiente + 32
print(f, "temperatura em fahreinhet")






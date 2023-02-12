menor = "Nenhum"
media = "Nenhuma"
maior = "Nenhum"
qtdNumeros = 0
numero_valido = False
while numero_valido == False:
    try:
        entrada = input()
        menor = media = maior = soma = float(entrada)
        qtdNumeros = qtdNumeros + 1
        numero_valido = True
    except:
        print("Nenhum número foi lido - A primeira linha foi vazia!!")
while entrada != '':
    entrada = input()
    try:
        valor = float(entrada)
        qtdNumeros = qtdNumeros + 1
        soma += valor
        if valor < menor:
            menor = valor
        elif valor > maior:
            maior = valor
        media = soma / qtdNumeros
    except:
        if entrada != '':
            print("Nenhum número foi lido - A primeira linha foi vazia!!")
print("Menor :", menor)
print("Maior:", maior)
print("Média:", media)

'''from statistics import mean

num = []

while (number := input()) != '':
    num.append(int(number))

print('Menor:', min(num))
print('Maior:', max(num))
print('Média', mean(num))
'''


'''num = input()
if num == " ":
    print("Nenhum número foi lido - A primeira linha lida foi vazia!!")

else:
 menor = num
maior = num
soma = num
soma += num
qtd = 1
media = soma/qtd


for x in range(0):
    num = int(input())
    soma += num
if num < menor:
    menor = num
elif num > maior:
    maior = num



print()
print("Menor:" , menor)
print("Maior:" , maior)
print("Soma:" , soma)
print("Média: %.2f" % media)
'''






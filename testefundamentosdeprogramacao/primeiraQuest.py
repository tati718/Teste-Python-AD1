# AD1.1.2023.1 - Questão 1

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










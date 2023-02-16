# Somente o total das vogais

frase = input();
vogais = 'aeiou'
frase =frase.lower()
result = 0
nvogais = 'lkjhgfdmnbv'

if frase == nvogais:
     print('Não há vogais na entrada', nvogais)


    
for i in vogais:
            result += frase.count(i)

print('No total há' ,result  ,'vogais na entrada' ,frase)
print( 'Há:',{i:frase.count(i)for i in vogais if i in frase})

#Quantidade de cada vogal de forma individual


 
 





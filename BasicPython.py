# Maneiras de se trabalhar com variáveis em Python
nome = 'exemplo de string em python'                                                #Mais igual +=
print(nome)                                                                         #Menos igual -=
print('valor da variável nome = {}'.format(nome)) #metodo .format()                 #Vezes igual *=
print(f'valor da variável nome = {nome}')                                           #Dividido igual /=
print(f"valor da variável nome = {nome}")                                           #Resto da divisao igual %=
# todas resultaram em -> valor da variável nome = exemplo de string em python       #Potencia = **
# Atribuicao Múltipla em Python                                                     #Quociente inteiro = //
a,b = 1 , 2
print ('antes da troca')
print(f"valor das variáveis: a = {a}, b = {b}") #a=1,b=2
#primeira troca
temp = a   # é necessario uma terceira variavel(auxiliar)= temp
a = b
b = temp
print ("Primeira Troca")
print (f"valor das variáveis: a = {a},b = {b}") #a=2,b=1
#Segunda Troca
a,b = b,a
print("Segunda troca")
print(f"valor das variáveis: a = {a},b = {b}") #a=1,b=2
#Operadores Compostos
x = 10
print(f"x = {x}") #x=10
x += 2
print(f"x = {x}") #x=12
x -= 2
print(f"x = {x}") #x=10

#não podem ser usadas como identificadores de variáveis em Python.
#São elas: and, as, assert, break, class, continue, def, del, elif, else,
#except, exec, finally, for, from, global, if, import, in, is, lambda, not,
#or, pass, print, raise, return, try, while, with e yield.

# Váriaveis Lovais e Globais:
def multiplicador(numero):
        y = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável vale: {y}")
        return y * numero

y = 3 # esta variável tem escopo global
z = multiplicador(5)
print(f"Fora da função, y variável a vale: {y}")
#Outro Caso:
def multiplicador(numero):
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}") ## A Variavel b vale 15
# Na linha 5, ao se chamar a função do multiplicador(), a variável a será procurada.
# Como não existe uma variável a no bloco interno da função, ela é procurada como variável global.
# Uma vez encontrada, o valor recuperado é 3.

#Palavra global define uma variavel local como global:
def multiplicador(numero):
        global a # todas as referências à variável a são para a global
        a = 2      # a global será alterado
        print(f"Dentro da função,  variável  vale: {a}")
        return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")
#Dentro da função,  variável  vale: 2
#A variável b vale: 10
#Fora da função, a variável a vale: 2

#lower,Upper, split, list, Tuple , Range
curso = 'Ensino a Distância'
#'Ensino a Distância'
curso.upper()
#'ENSINO A DISTÂNCIA'
curso.lower()
#'ensino a distância'
curso.split()
#['Ensino', 'a', 'Distância']
list('abc')
#['a','b','c']
tuple([1,2,3])
#(1,2,3)
range(2,7)
#cria a sequencia (2,3,4,5,6,6)
range(3)
#cria a sequencia (0,1,2)
range(2,9,3)
# O tipo range representa uma sequência imutável de números e frequentemente
# é usado em loops de um número específico de vezes, como o for.
#Também é possível criar sequências mais complexas,
# indicando os parâmetros de início, fim e passo, nessa ordem.
# O passo é o valor que será incrementado de um termo para o próximo.
# Por exemplo, range(2, 9, 3) cria a sequência (2, 5, 8).
s = "blabla"
t = 'blublu'
n = 3
i = 0
x in s  #True se x for um subconjunto de s
x not in s  #False se x for um subconjunto de s
s + t  #Concatenação de s e t
n*s  #Concatenação de n cópias de s
s[i] #Caractere de índice i em s
len(s) #Comprimento de s
min(s) #Menor item de s
max(s)  #Maior item de s

# Dicionario:Poderíamos criar um dicionário
# em que cada pessoa fosse representada pelo seu CPF, com nome e sobrenome. Para isso, teríamos:
pessoas = {'111222333-44':['Joao','Silva'],'222333444-55':['Maria','Pedro']}
print(pessoas[111222333-44]) #['Joao','Silva']

#impressao de sequencias:
str = 'Hello World'
print(str[0:4]) #Hell
print(str[2:8]) #llo Wo
print(str[::-1]) #dlroW olleH
print(str[8:2:-1]) #roW ol

#A função input() tanto exibe na tela a string “XXX”,
# como permite que o valor informado pelo usuário seja armazenado na variável a.
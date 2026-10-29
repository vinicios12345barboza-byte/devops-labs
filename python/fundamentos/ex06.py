## Script inicial de estudos em Python

# exercício 01: escreva "Olá, Mundo" na tela
msg = "Olá, Mundo DevOps!"
print(msg)

# exercício 02: Respondendo o usuário
nome = "Vinicios"
print(f'É um prazer te conhecer, {nome}')

# exercício 03: somando dois números

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print(f'A soma entre {n1} + {n2} é: {soma}')

# exercício 04: Dissecando uma Variável
a = input('Digite algo: ')
print(f'O tipo é primitivo desse valor é: ', type(a))
print(f'Só tem espaços? {a.isspace}')
## Script inicial de estudos em Python

# exercício 04: Dissecando uma Variável
a = input('Digite algo: ')
print(f'O tipo é primitivo desse valor é: ', type(a))
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}' )
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}') 
print(f'Esta em maiúsculas? {a.isupper()}')
print(f'Esta em minúsculas? {a.islower()}')
print(f'Esta capitalizada? {a.istitle()}')
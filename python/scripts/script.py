nome = input("Qual é o seu nome? ")
idade = int(input("Qual a sua idade? "))
cargo = input("Qual é o seu cargo? ")
empresa = input("Qual empresa?")
salary = int(input("Digite seu salário: "))


print(f"Usuário: {nome}.\nIdade: {idade}.\nCargo: {cargo} na empresa {empresa}.\nSalário: {salary}")

if cargo == "DevOps":
    print ('Bem vindo ao Mundo DevOps :)')
else:
    print('Bem vindo ao cargo!')

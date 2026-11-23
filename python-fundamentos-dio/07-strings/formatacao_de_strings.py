nome = "André"
idade = 40
profissao = "Programador"
linguagem = "Python"
saldo = 45.435



dados = {"nome": "André", "idade": 40}

# print("Nome: %s Idade: %d" % (nome, idade)) #forma que não usam mais.
# print("Nome: {} Idade: {}".format(nome, idade)) 
# print("Nome: {1} Idade: {0}".format(idade, nome)) 
# print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome)) 
# print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# print("Nome: {name} Idade: {age}".format(age=idade, name=nome)) #você pode reapórveitar a variavel para colocar em outro nome, mas o valor continua o mesmo.
# print("Nome: {nome} Idade: {idade}".format(**dados)) #desempacotando o dicionário

print(f"Nome: {nome} Idade: {idade}") #forma mais moderna de fazer, a partir do python 3.6

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") #:.2f para formatar o float com 2 casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") #:10.1f para formatar o float com 1 casa decimal e 10 espaços reservados para o valor


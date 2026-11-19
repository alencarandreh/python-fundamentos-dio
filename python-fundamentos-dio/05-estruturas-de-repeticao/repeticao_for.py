texto = input("Informe um texto: ")

VOGAIS = "AEIOU"


# Exemplo ulitizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
        print() #adiciona uma quebra de linha para separar as vogais das consoantes


# Exemplo de uso do for com range

for numero in range(0, 51, 5):
        print(numero, end=" ")
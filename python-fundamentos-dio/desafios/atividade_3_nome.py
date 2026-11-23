# Atividade 3 (DIO): formata um nome com a primeira letra de cada palavra em maiúscula
entrada = input()

palavras = entrada.strip().split()
palavras_formatadas = [palavra.capitalize() for palavra in palavras]
nome_formatado = " ".join(palavras_formatadas)

print(nome_formatado)
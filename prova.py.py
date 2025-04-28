# AVALIAÇÃO DE FILMES
# Nome: Luana Tavares
# Data: 28/04/2025

import os  


filmes = ["TRON", "wargames", "hackers", "pirates of silicon valley", "the social network", 
          "jobs", "the imitation game", "ex machina", "snowden", "ready player one"]
anos_dos_filmes = [1982, 1983, 1995, 1999, 2010, 2013, 2014, 2014, 2016, 2018]


arquivo_filmes = 'arquivofilmes.txt'
nome_arquivo = 'avaliacao_filme.txt'

with open(arquivo_filmes, 'w') as arquivo:
    for filme, ano in zip(filmes, anos_dos_filmes):
        arquivo.write(f"{filme} ({ano})\n")
print(f"Lista de filmes salva no arquivo '{arquivo_filmes}'.")

try:
    
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('')  
        print(f"Arquivo '{nome_arquivo}' criado, pois não existia.")

    
    print("\nLista de filmes disponíveis para avaliação:")
    for i, (filme, ano) in enumerate(zip(filmes, anos_dos_filmes), start=1):
        print(f"{i}. {filme} ({ano})")

    
    filme_escolhido = input("\nDigite o nome do filme que deseja avaliar: ")
    if filme_escolhido not in filmes:
        raise ValueError("O filme digitado não está na lista.")

    nota = float(input("Digite a nota do filme (0 a 10): "))
    if nota < 0 or nota > 10:
        raise ValueError("A nota deve ser entre 0 e 10.")

    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"Filme: {filme_escolhido}\nNota: {nota}\n\n")
    print("\nAvaliação gravada com sucesso!")
#
   
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do arquivo de avaliações:")
        print(conteudo)

except FileNotFoundError:
    print("Arquivo não encontrado.")
except ValueError as ve:
    print(f"Erro de valor: {ve}")
except Exception as e:
    print(f"Outro erro ocorreu: {e}")
finally:
    print("\nPrograma finalizado.")
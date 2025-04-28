import pandas as pd  

while True:
    nome = input("Informe seu nome: ")
    n1 = input("Informe a N1: ")
    n2 = input("Informe a N2: ")
    n3 = input("Informe a N3: ")

    with open('notas.txt', 'a') as arquivo:
        arquivo.write(nome + ',' + n1 + ',' + n2 + ',' + n3 + '\n')
    
    continuar = input("Deseja adicionar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break


# Exportar p/ o  notas.xlsx
df = pd.read_csv('notas.txt', header=None, names=['Nome', 'N1', 'N2', 'N3'])
df.to_excel('notas.xlsx', index=False, sheet_name='Notas')

print("Os dados foram salvos em 'notas.txt' e exportados para 'notas.xlsx' com sucesso!")
import pandas as pd

def calcular_media(notas):
    return round(sum(notas) / len(notas), 2)

def processar_alunos(arquivo_notas):
    aprovados = []
    exame = []
    reprovados = []
    todos_alunos = []

    with open(arquivo_notas, 'r') as arq:
        linhas = arq.readlines()
    
    with open(arquivo_notas, 'w') as arq:
        for linha in linhas:
            aluno = linha.strip().split(",")
            if len(aluno) < 4:
                continue
            aluno[0] = aluno[0].strip().title()
            arq.write(",".join(aluno) + "\n")

    with open(arquivo_notas, 'r') as arq:
        for linha in arq:
            aluno = linha.strip().split(",")
            if len(aluno) < 4:
                continue
            try:
                nome = aluno[0]
                notas = list(map(float, aluno[1:4]))
                media = calcular_media(notas)
            except:
                continue
            situacao = ""
            if media >= 7:
                situacao = "Aprovado"
                aprovados.append({'Nome': nome, 'Média': media})
            elif media >= 5:
                situacao = "Exame"
                exame.append({'Nome': nome, 'Média': media})
            else:
                situacao = "Reprovado"
                reprovados.append({'Nome': nome, 'Média': media})
            todos_alunos.append({'Nome': nome, 'Nota 1': notas[0], 'Nota 2': notas[1], 'Nota 3': notas[2], 'Média': media, 'Situação': situacao})
    aprovados.sort(key=lambda x: x['Nome'])
    exame.sort(key=lambda x: x['Nome'])
    reprovados.sort(key=lambda x: x['Nome'])
    todos_alunos.sort(key=lambda x: x['Nome'])
    return aprovados, exame, reprovados, todos_alunos

def salvar_resultados(aprovados, exame, reprovados, todos_alunos, arquivo_saida):
    geral = []
    for aluno in aprovados:
        aluno['Situação'] = 'Aprovado'
        geral.append(aluno)
    for aluno in reprovados:
        aluno['Situação'] = 'Reprovado'
        geral.append(aluno)
    with pd.ExcelWriter(arquivo_saida) as writer:
        pd.DataFrame(aprovados).to_excel(writer, sheet_name='Aprovados', index=False)
        pd.DataFrame(exame).to_excel(writer, sheet_name='Exame', index=False)
        pd.DataFrame(reprovados).to_excel(writer, sheet_name='Reprovados', index=False)
        pd.DataFrame(geral).to_excel(writer, sheet_name='Resumo Geral', index=False)
        pd.DataFrame(todos_alunos).to_excel(writer, sheet_name='Notas', index=False)

def exibir_reprovados(reprovados):
    if reprovados:
        print("Reprovados:")
        print(pd.DataFrame(reprovados).to_string(index=False))

if __name__ == "__main__":
    notas = 'notas.txt'
    saida = 'resultados.xlsx'
    aprovados, exame, reprovados, todos_alunos = processar_alunos(notas)
    salvar_resultados(aprovados, exame, reprovados, todos_alunos, saida)
    exibir_reprovados(reprovados)


Eu tive mais dificuldade com o git do que com o trabalho em si, porque já uso a biblioteca pandas no trabalho manipulando arquivo do Excel. As alterações realizadas no código foram somente as obrigatórias e utilização da biblioteca pandas como sugerido .
•	Este script lê um arquivo de notas de alunos, calcula médias e classifica os alunos.
•	A função calcular_media(notas) recebe uma lista com 3 notas e retorna a média arredondada.
•	A função processar_alunos(arquivo_notas) faz toda a leitura e processamento do arquivo.
•	Primeiro, formata os nomes dos alunos e regrava o arquivo com os dados corrigidos.
•	Depois, percorre novamente o arquivo, calcula a média e classifica cada aluno.
•	Alunos com média >= 7 são aprovados, entre 5 e 6.9 vão para exame, e < 5 são reprovados.
•	Os dados são separados em listas: aprovados, exame, reprovados e todos_alunos.
•	Todos os dados são organizados em ordem alfabética pelo nome.
•	A função salvar_resultados(...) salva essas listas em um arquivo Excel com 4 planilhas.
•	As planilhas são: Aprovados, Exame, Reprovados e Notas (com todas as informações).
•	A função exibir_reprovados(reprovados) mostra no terminal quem foi reprovado.
•	O arquivo de entrada é 'notas.txt' e a saída é 'resultados.xlsx'.
•	O código usa a biblioteca pandas para manipular e salvar os dados em Excel.


import csv

with open("alunos.csv", "r", encoding="utf-8") as alunos:
    leitor = csv.reader(alunos)
    with open("alunos_copia.csv", "w", encoding="utf-8", newline="") as arquivos_copia:
        escritor = csv.writer(arquivos_copia)
        for linha in leitor:
            escritor.writerow(linha)
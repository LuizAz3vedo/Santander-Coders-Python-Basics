import csv

with open("alunos.csv", "r", encoding="utf-8") as alunos:
    leitor = csv.reader(alunos)
    header = next(leitor)
    with open("alunos_media.csv", "w", encoding="utf-8", newline="") as arquivos_copia:
        escritor = csv.writer(arquivos_copia)
        header.append('Media')
        escritor.writerow(header)
        for linha in leitor:
            for valor in range(3,7):
                linha[valor] = float(linha[valor])
            linha.append(sum(linha[3:7]) / len(linha[3:7]))
            escritor.writerow(linha)


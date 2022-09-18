import csv

with open("alunos.csv", "r", encoding="utf-8") as alunos:
    write = csv.reader(alunos)
    for linhas in write:
        print(linhas)

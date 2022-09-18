idade = int(input("Digite um valor para a idade entre 0 e 150 valor da idade: "))
salario = float(input("Digite um valor de salario: "))
sexo = str(input("Qual o seu sexo? [M/F/O] ")).upper()

if idade >= 0 and idade <= 150:
   print("Idade Correta")
else:
    print("Idade incorreta")

if salario > 0:
    print("Salario Correto")
else:
    print("Salario incorreto")

if sexo[0] == "M" or sexo[0] == "F" or sexo[0] == "O":
    print("Certo")
else:
    print("Insira umas das opções")

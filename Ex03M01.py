p1 = str(input("Mora perto da vitima? ")).strip().lower()
p2 = str(input("Já trabalhou com a vitima? ")).strip().lower()
p3 = str(input("Telefonou para a vitima? ")).strip().lower()
p4 = str(input("Esteve no local do crime? ")).strip().lower()
p5 = str(input("Devia para a vitima? ")).strip().lower()

suspeito = 0

if p1 == "sim":
    suspeito = suspeito + 1
    print(suspeito)
if p2 == "sim":
    suspeito = suspeito + 1
if p3 == "sim":
    suspeito = suspeito + 1
if p4 == "sim":
    suspeito = suspeito + 1
if p5 == "sim":
    suspeito = suspeito + 1
else:
    print("Analisando")

if suspeito == 5:
    print("Assasino")
elif suspeito ==4 or suspeito == 3:
    print(("Cumplice"))
elif suspeito == 2:
    print("Suspeito")
else:
    print("Liberado")
    print(suspeito)
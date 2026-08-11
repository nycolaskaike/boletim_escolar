#Caixa 0 1 2 3 4 5 6
QtdNotas = int(input("Digite a quantidade de notas:"))
Notas = []
for i in range(QtdNotas):
    Nota=float(input(f"Digite a nota {i+1}: "))
    Notas.append(Nota)
Total_notas= 0
for Nota in Notas:
    Total_notas+=Nota
    media=Total_notas/ len(Notas)
if media>= 7:
        print("Desempenho Satisfatório!")
else:
        print("Desempenho Insatisfatório...")

# Écrire un programme qui choisi le plus grand nombre parmi deux nombres saisies a partir du clavier

a = int(input("Entrer le premier nombre\n"))
b = int(input("Entrer le deuxieme nombre\n"))

if a < b:
    print("Le plus grand nombre est : ", b)
elif a == b:
    print("Les nombres sont égaux !")
else:
    print("Le plus grand nombre est : ", a)
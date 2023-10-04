# Écrire un programme qui va trouver le plus grand nombre parmi 3 nombres saisis a partir du clavier
a = int(input("Entrer le premier nombre\n"))
b = int(input("Entrer le deuxieme nombre\n"))
c = int(input("Entrer le troisieme nombre\n"))

if a > b and b > c:
    print("Le plus grand nombre est : ", a)
elif b > c :
    print("Le plus grand nombre est : ", b)
elif a == b and b == c:
   # print("Les nombres sont égaux !")
else:
    print("Le plus grand nombre est : ", c)
# Décrire un programme qui va lire les données d'un employé a partir du clavier
#Identifiant, nom, salaire, adresse, marie

id = int(input("saisir votre ID svp: "))
nom = input("saisir votre nom svp : ")
salaire = float(input("Veuillez saisir votre salaire : "))
adresse = input("Veuillez saisir votre adresse : ")
status = bool(input("etes vous marié ou non: "))
print("SVP, confirmer vos informations personnelles")
print("le ID de l'employé: ",id)
print("le nom de l'employé: ",nom)
print("le salaire de l'employé: ", salaire)
print("l'adresse de l'employé : ",adresse)
print("est ce que l'employé est marié: ",status)
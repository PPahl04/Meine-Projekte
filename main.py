print("Dieses Programm sortiert eine endliche Liste beliebige ganze Zahlen.")
eingabe = input("Bitte ganze Zahl eingeben. Wenn Sie fertig sind, bitte 'q' eingeben. \n")

liste = []

while eingabe not in ["q"]:
    liste.append(int(eingabe))
    eingabe = input("Zahl oder 'q' eingeben.\n")

print("Danke fÃ¼r die Eingabe. Die sortierte Liste ist ")
sortierte_liste = sorted(liste)
print(sortierte_liste)
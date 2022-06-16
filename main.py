#Erstelle ein Programm das dein Vorame, Nachname und dein Geburtstag ausgibt.

Vorname= input("Bitte geben Sie hier Ihren Vornamen ein:")
Zweitname= input("Bitte geben Sie hier Ihren Zweitnamen ein:")
Nachname= input("Bitte geben Sie hier Ihren Nachnamen ein:")
G_Jahr= input("Bitte geben Sie hier Ihr Geburtsjahr an:")
G_Tag= input("Bitte geben Sie hier Ihr Geburtsdatum ein:")
Alter= 2022 - int(G_Jahr)
print("Ihr Name lautet " + str(Vorname) +" "+ str(Zweitname)+ " " + str(Nachname) + " und Sie wurden am " + str(G_Tag) + "." + str(G_Jahr) + " geboren, welches Sie ungefähr " + str(Alter) + " Jahre Alt macht.")
if Alter >= 18:
    print("Sie sind volljährig.")
elif Alter > 13:
    print("Sie sind ein Teenager.")
else:
    print("Sie sind noch minderjährig.")
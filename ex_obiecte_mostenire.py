from cursul7.mostenire import  Persoana, Student, Angajat, Profesor

andrei = Persoana("Andrei", 27, "Bacau")
andrei.descriere()

maria = Student("Maria", 21, "Iasi", "AC", 3)
maria.descriere()
## e un return de aia pun in print:
# print(maria.anul_nasterii())
# print(maria.nume)

pavel = Angajat("Pavel", 45, "Bucuresti", "XYZ", 3000)
pavel.descriere()
print(f"Salariul anual: {pavel.salariu_anual()} ")

ioana = Profesor("Ioana", 35, "BN", "WXY", 7000, "Matematica", 20)
ioana.descriere()
print("salariu anual" + str(ioana.salariu_anual())) ##str e cand nu folosim f
print(f"Anul nasterii {ioana.anul_nasterii()}")
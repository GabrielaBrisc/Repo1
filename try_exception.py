# elevi = []
#
# while True:
#     nume_elevi = input("Nume elev: ")
#     elevi.append(nume_elevi)
#     if len(elevi) == 5:
#         break
# raise Exception("Puteti adauga max 5 elevi")  #codul nu mai ruleaza dupa raise

"""
Exceptii = clase speciale in Python fol atunci cand ceva nu merge bn in cod
Fol try-except pt a gestiona posibilele exceptii aruncate in codul nostru , PT A NU SE OPRI EXE PROGRAMULUI
"""

# lista_numere =[1,2,3,4]
# print(lista_numere[6]) #-> ne va arunca o eroare pt ca in lista nu exista elem cu indexul 6
# print("sunt aici")
#
# try:
#     print(lista_numere[6])
# except IndexError as error: # aici prindem eroarea de mai sus si afisam in consola textul erorii
#     print(error)
#     print("incerc index2=", (lista_numere[2]))
# print("sunt aici dupa indexerror")

### cand nu stim ce eroare poate sa apara
# try:
#     print(lista_numere[6])
# except Exception as error: # Exception prinde orice eroare poate aparea in blocul de try:
#     print(error)
# print("sunt aici dupa exception")

###Exemplu de eroare care nu e prinsa corect
# try:
#     print(lista_numere[6])
# except AssertionError as error:
    ### ASSERTION nu prinde aceeasi eroare ca index error
    ## #(generalizat, adica fiecare exceptie prinde doar un anumit tip de eroare,
    ### mai putin Exception care prinde orice eroare care poate aparea
    # print(error)

### nu putem merge mai departe
# assert 5 > 10, "5 nu e mai mare decat 10"
# print("sunt aici dupa assert") # nu o sa se exe

### codul ruleaza dupa acest bloc, adica, daca avem eroare,ne arunca eroarea, o prindem,merge mai deperte:
try:
    assert  5 >10, "5 nu e mai mare decat 10"
except AssertionError as error:
  # pass ###nu se intampla nimic, il punem doar daca nu vrem sa punem nimic dupa
    print(error)
print("sunt aici dupa try and except assertion")
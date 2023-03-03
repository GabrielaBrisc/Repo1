"""
-private -> metoda/atributul nu poate fi accesat decat in interiorul clasei in care este definit
            -> se scrie cu dublu under_score la inceputl numelui (__example)
-protected -> metoda/atributul poate fi accesat din clasa in care a fost definita,
dar si in calsele copil ale acesteia, INSA NU DIN EXTERIOR
            -> se defineste cu un singur undescore(_exemplu)
"""
class Car:

    # atribute din clasa
    __variabila_privata = "private"
    _variabila_protected = "protected"

    def __init__(self,var_protected):
        self._variabila_protected = var_protected

    def get_var_private(self):
        return self.__variabila_privata

    def set_var_private(self,value):
        self.__variabila_privata = value

    def __hidden_method(self):
        print("Hello, you can't call me")
car = Car(12)
# print(car._variabila_protected)
# print(car.__variabila_privata)
print(car.get_var_private())
car.set_var_private("Am fost modificat")
print(car.get_var_private())
# car.__hidden_method
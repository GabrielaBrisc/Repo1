# 2. ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria(self):
        pass
    #
    @classmethod
    def descrie(self):
        print(f"Cel mai probabil am colturi")

###  Mostenire
class Patrat(FormaGeometrica):

    __latura = None
    def __init__(self, latura):
        self.latura = latura

    ### implementam aria
    def aria(self):
        return self.latura * self.latura

    ### Encapsulation
    def get_latura_private(self):
        return self.__latura

    def set_latura_private(self, value):
        self.__latura = value

    def delete_latura_privata(self):
        return self.__latura
class Cerc():
    __raza = None ## prop privata
    def __init__(self, raza):
        self.raza = raza

    #implementam aria
    def aria(self):
        return 3.14 * (self.raza* self.raza)
    ##cum folosesc PI?
    def get_raza_private(self):
        return self.__raza

    def set_raza_private(self, value):
        self.__raza = value

    def delete_raza_privata(self):
        return self.__raza

    def descrie(self):
        print("Eu nu am colturi")


patrat = Patrat(15)
patrat.set_latura_private("set variabila")
# print(patrat.__latura)
patrat.descrie()
print("aria este:", patrat.aria())

cercul = Cerc(3)
print(cercul.aria())
cercul.descrie()

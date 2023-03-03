"""

Abstractizare = proces prin care putem ascunde o anumita functionalitate specificata de utilizator
si de asemenea de a putea forta un anumit comportamnet in clasele copil
Utilizatorul stie functionalitatea dar nu si cum e executata
= (o schita pt clasele copil)
Clasa parinte este o clasa abstracta deci nu putem sa cream obiecte din ea ci doar sa o folosim ca un template pt clasele copil
In abstractizare exista 2 concepte:
  -interfata: contine doar metode abstracte
  -clasa abstracta: contine metode abstracte cat si met proprii, cu logice
Clasa abstracta trb sa mosteneasca clasa ABC (abstract class method)
"""
"""
Polimorfism =suprascriere 
= poli (mai multe) morfis(forme) ->ceva care poate lua mai multe forme
In cazul nostru, in OOP, o met poate sa aibe acelasi nume in clase diferite 
"""
###Abstracta
from abc import ABC, abstractmethod

##punem ABC pt ai zice lui Python ca este o clasa
##in java se def: class abstract numeclasa())

class Vehicul(ABC):
    @abstractmethod ##am fol un decorator sa marcam aceasta metoda ca abstracta
    ##tot ce e cu @ e decorator
    def nr_locuri(self):
        raise

    @abstractmethod
    def nr_roti(self):
        pass
    ## in general metodele abs nu trebuie sa aibe logica
    ##si pt a nu avea errori avem 2 optiuni:
            ##scriem pass
            ##raise NotImplementedError

    @classmethod #am fol un decoratoe ca sa marcam met ca fiind una de clasa, cu logica proprie
    def metoda_logica_proprie(self):
        print(f"Este o met cu logica proprie. "
              f"Nu trebuie implementata obligatoriu in clasele copii")

class Masina(Vehicul):
    def __init__(self, culoare):
        self.culoare = culoare

    def get_culoare(self):
        return self.culoare

    def nr_roti(self):
        return 4
    def nr_locuri(self):
        return 5

class Bicicleta(Vehicul):
    def __init__(self, roti_ajutatoare = False):
        self.roti_ajutatoare = roti_ajutatoare

    def nr_roti(self):
        if self.roti_ajutatoare == True:
            return  4
        else:
            return 2
    def nr_locuri(self):
        return 1

audi = Masina("Gri")
# audi.metoda_logica_proprie()
print(audi.nr_locuri())


# vehicul = Vehicul() #nu putem crea ob fol clasa abstracta
bicicleta = Vehicul()
print(bicicleta.nr_locuri())
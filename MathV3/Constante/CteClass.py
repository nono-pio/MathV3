from PARAMETRE import FONCTION_ELEMENTAIRE
from .methode_basique import approximation, reduction


class Cte:
    def __init__(self, element) -> None:
        self.value = element
        self.app = approximation(element)

        #element racine (première fonction)
        self.racine = element[0]
        if element[0] == '+': self.racine_ordre = 1
        elif element[0] in ('*','/'): self.racine_ordre = 2
        elif element in ('^','rac'): self.racine_ordre = 3
        else: self.racine_ordre = None
    
    def reduction(self):
        return reduction(self.value)
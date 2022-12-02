class base:
    def __str__(self) -> str:
        return self.strFonction
    def __repr__(self) -> str:
        return self.strFonction

#fonction de base

class add(base):
    strFonction = '+'

class mult(base):
    strFonction = '*'

class div(base):
    strFonction = '/'

class pui(base):
    strFonction = '^'

#fonction logaritme et exponentielle

class exp(base):
    strFonction = 'exp'

class ln(base):
    strFonction = 'ln'

class log(base):
    strFonction = 'log'

#fonction  trigonométrique

class cos(base):
    strFonction = 'cos'

class sin(base):
    strFonction = 'sin'

class tan(base):
    strFonction = 'tan'

class acos(base):
    strFonction = 'acos'

class asin(base):
    strFonction = 'asin'

class atan(base):
    strFonction = 'atan'
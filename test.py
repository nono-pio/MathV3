from Constante.CteClass import Cte
from classFonctionElementaire import *
import math

x = [add(),2,[mult(),4,[tan(),math.pi]]]
x = Cte(x)
print(x.value,'=',x.app)
print(x)
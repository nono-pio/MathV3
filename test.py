from Constante.CteClass import Cte

x = ["+",1,2,["+",1,2],["+",1,2]]
x = Cte(x)
print(x.value)
print(x.reduction())
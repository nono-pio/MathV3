from Constante.CteClass import Cte

x = ["+",1,2,["*",2,3,["/",2,4],["^",2,3]]]
x = Cte(x)
print(x.value)
print(x.app)
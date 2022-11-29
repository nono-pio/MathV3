import math

global cte
cte = (int,float,complex)

def approximation(element):
    if type(element) in cte:
        return element
    
    match element[0]:
        case '+':
            return sum([approximation(val) for val in element[1::]])
        case '*':
            result = 1
            for val in element[1::]: result *= approximation(val)
            return result
        case '/':
            if element[2] == 0: return ZeroDivisionError("Impossible de diviser par 0")
            return element[1]/element[2]
        case '^':
            if element[1] == element[2] == 0: return ArithmeticError("Imposible de faire 0^0")
            return element[1]**element[2]

def reduction(element):
    pass
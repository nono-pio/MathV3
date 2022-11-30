import math
from collections import Counter

import numpy as np

global cte
cte = (int,float,complex)

def approximation(element):
    if type(element) in cte:
        return element

    if element == 'Error': return 'Error'
    newElement = [element[0]]
    for val in element[1:]:
        app = approximation(val)
        if app == 'Error': return 'Error'
        else: newElement.append(app)
    element = newElement

    fun_list = {
        '+': lambda element: sum(element[1::]),
        '*': lambda element: np.prod(element[1::]),
        '/': lambda element: 'Error' if element[2] == 0 else element[1]/element[2],
        '^': lambda element: 'Error' if element[1] == element[2] == 0 else element[1]**element[2],
    }

    return fun_list.get(element[0])(element)

    '''
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
    '''

def reduction(element):
    if type(element) in cte:
        return element
    
    if element == 'Error': return 'Error'
    newElement = [element[0]]
    for val in element[1:]:
        red = reduction(val)
        if red == 'Error': return 'Error'
        else: newElement.append(red)
    element = newElement

    fonc_red = {
        '+':lambda val: red_add(val),
    }

    return fonc_red.get(element[0],'Error')(element[1:])

#fonction de reduction
def red_add(element):
    cte_simple = 0
    coef_element = {}
    for val in element:
        print(val,coef_element)
        if type(val) in cte: cte_simple += val
        elif val in coef_element: coef_element[val] += 1
        else: coef_element[val] = 1
    result = ['add', cte_simple]
    for val, coef in coef_element.items():
        result.append(val) if coef == 1 else result.append(['*',coef,val])
    return result

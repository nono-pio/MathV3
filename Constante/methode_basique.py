import math

import numpy as np

from classFonctionElementaire import *

global cte
cte = (int,float,complex)

def approximation(element):
    if type(element) in cte:
        return element

    if element == 'Error': return 'Error'
    element = [element[0]] + [approximation(val) for val in element[1:]]
    if 'Error' in element: return 'Error'

    fun_list = {
        '+': lambda element: sum(element[1:]),
        '*': lambda element: np.prod(element[1:]),
        '/': lambda element: 'Error' if element[2] == 0 else element[1]/element[2],
        '^': lambda element: 'Error' if element[1] == element[2] == 0 else element[1]**element[2],
        
        'exp': lambda element: math.exp(element[1]),
        'ln': lambda element: 'Error' if element[1] == 0 else math.log(element[1]),
        'log': lambda element: 'Error' if element[1] in (1,0) or element[2] == 0 else math.log(element[2], element[1]),

        'cos': lambda element: math.cos(element[1]),
        'sin': lambda element: math.sin(element[1]),
        'tan': lambda element: 'Error' if element[1]%math.pi == 0 else math.tan(element[1]),
        'acos': lambda element: 'Error' if element[1]>1 and element[1]<1 else math.acos(element[1]),
        'asin': lambda element: 'Error' if element[1]>1 and element[1]<1 else math.asin(element[1]),
        'atan': lambda element: math.atan(element[1]),
    }

    return fun_list.get(element[0].strFonction)(element)

def reduction(element):
    if type(element) in cte: return element
    
    if element == 'Error': return 'Error'
    element = [element[0]] + [reduction(val) for val in element[1:]]
    if 'Error' in element: return 'Error'

    fonc_red = {
        '+':lambda val: red_add(val),
        '*':lambda val: red_mul(val),
    }

    red = fonc_red.get(element[0].strFonction,'Error')
    return 'Error' if red == 'Error' else red(element[1:])

#fonction de reduction
def red_add(element):
    cte_simple = 0
    coef_element = {}
    for val in element:
        if type(val) in cte: cte_simple += val
        elif val in coef_element: coef_element[val] += 1
        else: coef_element[val] = 1
    
    if coef_element == {}: return cte_simple
    elif cte_simple == 0: result = [add()]
    else: result = [add(), cte_simple]

    for val, coef in coef_element.items():
        result.append(val) if coef == 1 else result.append([mult(),coef,val])
    return result

def red_mul(element):
    cte_simple = 1
    coef_element = {}
    for val in element:
        if type(val) in cte: cte_simple *= val
        elif val in coef_element: coef_element[val] += 1
        else: coef_element[val] = 1
    
    if coef_element == {}: return cte_simple
    elif cte_simple == 1: result = [mult()]
    else: result = [mult(), cte_simple]

    for val, coef in coef_element.items():
        result.append(val) if coef == 1 else result.append([pui(),coef,val])
    return result
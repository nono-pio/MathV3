from classFonctionElementaire import *

global CTE
CTE = (int,float,complex)

def strValue(element):
    if isinstance(element,CTE): return str(element)

    element[1:] = [strValue(val) for val in element[1:]]

    StrTypeFonction = {
        '+': lambda vals: ' + '.join(vals),
        '*': lambda vals: ' * '.join(vals),
        '/': lambda vals: f'{vals[0]}/{vals[1]}',
        '^': lambda vals: f'{vals[0]}^{vals[1]}',

        'exp': lambda vals: f'exp({vals[0]})',
        'ln': lambda vals: f'ln({vals[0]})',
        'log': lambda vals: f'log_{vals[0]}({vals[1]})',

        'cos': lambda vals: f'cos({vals[0]})',
        'sin': lambda vals: f'sin({vals[0]})',
        'tan': lambda vals: f'tan({vals[0]})',
        'acos': lambda vals: f'acos({vals[0]})',
        'asin': lambda vals: f'asin({vals[0]})',
        'atan': lambda vals: f'atan({vals[0]})',
    }

    result = StrTypeFonction.get(element[0].strFonction,'Error')
    return 'Error' if result == 'Error' else result(element[1:])
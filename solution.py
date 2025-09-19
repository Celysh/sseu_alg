import math
import numpy as np
def solution(x, exp):
    math_dict = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'actg': math.atan2,
        'log': math.log,
        'ln': np.log,
        'root': math.sqrt,
        'mod': math.fabs,
        'fact': math.factorial,
        'e': math.e,
        'pi': math.pi,
        'x' : x
    }
    try:
        result = eval(exp, {}, math_dict)
        return result
    except None:
        return None

def comp(x,b1,b2,exp1,exp2,exp3):
    if eval(b1) == True:
        return exp1
    elif eval(b2) == True:
        return exp2
    else:
        return exp3
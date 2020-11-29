#!/home/edilson/anaconda3/bin/python3.8

import re
import sys
from project.dualsimplex import dual_simplex





objetive_function = sys.argv[1]
constraints = sys.argv[2:]
print(objetive_function)
print(constraints)
def get_variables_and_coefficients(eq):

    variables = re.findall(r'[a-z]+',eq)
    coefficients = re.split(r'[a-z]+',eq)
    integer_coefficients = list(map(lambda v : int(v), coefficients[0:-1]))
    equal = re.split(r'=|<|>|(<&=)|(>&=)'  ,eq)
    if len(equal) > 1:
        return variables, integer_coefficients, float(equal[-1])
    return variables , coefficients[0:-1]


def main():

    try:
        values_objetive_function = get_variables_and_coefficients(
                objetive_function
                )
        print(values_objetive_function)
        coefficients_objetive_function = values_objetive_function[1]
        constraints_coefficients = []
        constraints_values = []
        for c in constraints:
            _,coefficients , result = get_variables_and_coefficients(c)
            print(coefficients)
            constraints_coefficients.append(coefficients)
            constraints_values.append(result)
        print(constraints_coefficients, constraints_values)
    except Exception as e:
        print(e)
        print('Revisar las funciones de entrada')
    finally:
        result = dual_simplex(coefficients_objetive_function,constraints_coefficients,constraints_values)
        print(result)

if __name__ == '__main__':
    main()

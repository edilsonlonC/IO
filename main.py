#!/home/edilson/anaconda3/bin/python3.8

import re
import sys
from project.dualsimplex import dual_simplex


objective_function = sys.argv[1]
constraints = sys.argv[2:]


def get_variables_and_coefficients(eq):

    variables = re.findall(r"[a-z]+", eq)
    coefficients = re.split(r"[a-z]+", eq)
    integer_coefficients = list(map(lambda v: int(v), coefficients[0:-1]))
    equal = re.split(r"=|<|>|(<&=)|(>&=)", eq)
    if len(equal) > 1:
        return variables, integer_coefficients, float(equal[-1])
    return variables, coefficients[0:-1]


def main():

    try:
        values_objective_function = get_variables_and_coefficients(objective_function)
        coefficients_objective_function = values_objective_function[1]
        constraints_coefficients = []
        constraints_values = []
        for c in constraints:
            _, coefficients, result = get_variables_and_coefficients(c)
            constraints_coefficients.append(coefficients)
            constraints_values.append(result)
    except Exception as e:
        print("Revisar las funciones de entrada")
        return
    finally:
        result = dual_simplex(
            coefficients_objective_function,
            constraints_coefficients,
            constraints_values,
        )
        print(result)


if __name__ == "__main__":
    main()

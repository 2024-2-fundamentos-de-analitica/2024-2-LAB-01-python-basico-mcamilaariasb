"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
    
    col1_to_col5_sum = {}

    for line in lines:
        parts = line.strip().split('\t')  
        col1 = parts[0]  
        col5_values = parts[4].split(',')  

        for value_pair in col5_values:
            _, value = value_pair.split(':')  
            if col1 not in col1_to_col5_sum:
                col1_to_col5_sum[col1] = 0
            col1_to_col5_sum[col1] += int(value)

    return dict(sorted(col1_to_col5_sum.items()))

print(pregunta_12())
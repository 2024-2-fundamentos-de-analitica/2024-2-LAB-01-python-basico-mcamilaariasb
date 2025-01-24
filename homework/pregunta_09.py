"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
 
    col5_count = {}

    for line in lines:
        parts = line.strip().split('\t')  
        col5_values = parts[4].split(',')  

        for value_pair in col5_values:
            key, _ = value_pair.split(':')  
            if key not in col5_count:
                col5_count[key] = 0
            col5_count[key] += 1

    return dict(sorted(col5_count.items()))

print(pregunta_09())
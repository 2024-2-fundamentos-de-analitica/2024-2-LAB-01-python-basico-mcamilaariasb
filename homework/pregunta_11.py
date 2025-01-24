"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    col4_sums = {}

    for line in lines:
        parts = line.strip().split('\t')  
        col2 = int(parts[1])  
        col4_values = parts[3].split(',')  

        for letter in col4_values:
            if letter not in col4_sums:
                col4_sums[letter] = 0
            col4_sums[letter] += col2

    return dict(sorted(col4_sums.items()))

print(pregunta_11())
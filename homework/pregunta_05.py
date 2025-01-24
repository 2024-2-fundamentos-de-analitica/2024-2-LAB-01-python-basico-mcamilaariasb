"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    values = {}
    for line in lines:
        parts = line.split("\t")
        letra = parts[0]  
        valor = int(parts[1])  
        if letra in values:
            values[letra].append(valor)
        else:
            values[letra] = [valor]
    result = [(letra, max(valores), min(valores)) for letra, valores in sorted(values.items())]

    return result
print(pregunta_05())


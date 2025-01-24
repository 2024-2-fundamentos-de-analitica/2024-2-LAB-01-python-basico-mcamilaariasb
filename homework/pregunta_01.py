"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
    
    suma = 0
    for line in lines:
        suma += int(line.split("\t")[1])
    
    return suma

print(pregunta_01())


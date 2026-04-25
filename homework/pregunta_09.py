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
        master = dict()
        for record in [line.split('\t') for line in file.readlines()]:
            sub = record[-1].strip().split(',')
            for k in [k for k_s in sub for k, _ in [k_s.split(':')]]:
                master[k] = master.get(k,0) + 1
        
        return master

print(pregunta_09())

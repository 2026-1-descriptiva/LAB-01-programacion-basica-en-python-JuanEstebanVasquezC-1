"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
    ('bbb', 1, 9),
    ('ccc', 1, 10),
    ('ddd', 0, 9),
    ('eee', 1, 7),
    ('fff', 0, 9),
    ('ggg', 3, 10),
    ('hhh', 0, 9),
    ('iii', 0, 9),
    ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r") as file:
        master = dict()
        for record in [line.split('\t') for line in file.readlines()]:
            sub = record[-1].strip().split(',')
            for k, v in [k_v.split(':') for k_v in sub]:
                v=int(v)
                master[k] = (
                    min(master.get(k,(v,v))[0],v),
                    max(master.get(k,(v,v))[1],v)
                )
        final_list = sorted([(k,vs[0],vs[1]) for k,vs in master.items()])
        return final_list

print(pregunta_06())
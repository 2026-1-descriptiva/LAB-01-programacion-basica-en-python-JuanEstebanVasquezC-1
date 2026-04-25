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
        letters = dict()
        for record in [line.split('\t') for line in file.readlines()]:
            letter = record[0]
            amount = int(record[1])
            letters[letter] = (
                            max(letters.get(letter, (amount, amount))[0],amount),
                            min(letters.get(letter, (amount,amount))[1],amount))
        final_list = sorted([(letter, values[0], values[1]) for letter, values in letters.items()])
        return final_list

print(pregunta_05())

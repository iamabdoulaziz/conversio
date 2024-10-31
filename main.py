
"""
1- Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)

3 - Afficher la valeur convertie (et l'unité : cm ou pouces)

- fin du programme.
"""
INCH = 2.54
CM = 0.394

def conversio_in_cm(value_in_cm):
    inch_value = value_in_cm*INCH
    return inch_value


def conversio_in_inch(value_in_inch):
    cm_value = value_in_inch*CM
    return cm_value

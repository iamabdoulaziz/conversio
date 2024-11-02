
INCH = 2.54
CM = 0.394

def inch_to_centimeters(pouces):
    result = pouces * INCH
    return result


def centimeters_to_inch(cm):
    result = cm * CM
    return result


print("Tu souhaites convertir de :")
print("1. Pouces en centimètres.")
print("2. Centimètres en pouces.")

_choice = int(input("Entre ton choix 1 ou 2 : "))
if _choice == 1:
    inch_value = float(input("Entre la valeur de pouces à convertir en centimètres: "))
    cm_value = round(inch_to_centimeters(inch_value), 2)
    print(f"{inch_value} pouces donne {cm_value} cm.")
elif _choice == 2:
    cm_value = float(input("Entre la valeur de cm à convertir en pouces: "))
    inch_value = round(centimeters_to_inch(cm_value), 2)
    print(f"{cm_value} cm donne {inch_value} pouces.")

print("Fin !")

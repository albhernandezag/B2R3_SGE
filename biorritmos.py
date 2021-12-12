from math import sin, pi
import datetime

dia = int(input("Introduce el día en el que naciste: "))
mes = int(input("Introduce el mes en el que naciste: "))
año = int(input("Introduce el año en el que naciste: "))

dias = (datetime.datetime.now() - datetime.datetime(año, mes, dia)).days

ciclo_fisico = round(sin(2 * pi * dias / 23) * 100)
ciclo_emocional = round(sin(2 * pi * dias / 28) * 100)
ciclo_intelectual = round(sin(2 * pi * dias / 33) * 100)

print("El porcentaje de tu ciclo físico es: ", ciclo_fisico, "%")
print("El porcentaje de tu ciclo emocional es:", ciclo_emocional, "%")
print("El porcentaje de tu ciclo intelectual es:", ciclo_intelectual, "%")

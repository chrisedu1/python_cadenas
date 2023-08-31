#programa que pregunta al usuario la fecha de su nacimiento en formato dd/mm/aaaa
#luego muestre en pantalla el dia el mes y el año.

fecha = input("Escribe tu fecha de nacimiento: \n")

dia=fecha[:fecha.find("/")]

mes_año=fecha[fecha.find("/")+1:]

mes=mes_año[:mes_año.find("/")]

año=mes_año[mes_año.find("/")+1:]


print(dia)
print(mes)
print(año)


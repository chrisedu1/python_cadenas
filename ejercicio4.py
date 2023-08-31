#programa que pregunte el numero telefonico
# y muestra en pantalla el numero sin el prefijo y la extension

num = input("Introduzca un número telefónico en el siguiente formato: +xx-xxxxxxxxx-xx: ")
print("El numero es", num[4:-3])

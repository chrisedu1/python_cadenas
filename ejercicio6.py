#Pedir al usuario que introduzca una frase en la consola y una vocal
#Despues mostrar la frase en pantalla, pero con la vocal en mayúscula

frase = input("Por favor, introduce una frase: ")
vocal = input("Por favor, introduce una vocal en minúscula: ")


print(frase.replace(vocal, vocal.upper()))

#programa que pregunta el precio de un producto en euros con dos decimales
#y muestre en pantalla el numero de euros y el numero de centecimos del precio

precio = input("Introduzca el precio del producto: ")
print("Euros: ", precio[:precio.find(".")], "centimos: ", precio[precio.find(".")+1:])


#Programa que pregunte un correo electronico del usuario
#luego que muestre el mismo correo (la parte delante de la @)pero con el dominio ceu.es

email = input("Introduce un correo electrónico: ")
print(email[:email.find("@")]+ "@ceu.es")

# Podemos separar los strings y guardarlos individualmente usando ".split()"

new_user = "Ann John Alex"
usuarios = new_user.split()
print(usuarios)


Variable = "Todos comen pastel porque es delicioso"
split_V = Variable.split()


# Para separar los strings separados por una coma

Usuario = "Lauren,25,F,Architect"
usuario_1 = Usuario.split(",")



# Para separar los strings separados por una diagonal

path = "getmimo.com/glossary/pythin"
path_list = path.split("/")



area_codes = "1150 1190 1100 1700"
code_list = area_codes.split()


# Para actualizar un string sin crear una nueva variable usamos ".replace()"

Menu = "El especial de hoy es pasta"
nuevo_especial = Menu.replace("pasta", "tacos de canasta")



# También podemos guardar el cambio en la antigua variable
Menu = Menu.replace("pasta", "mole negro")

# .replace() cambia todas las palabras que sean iguales por el nuevo string

june = "June sales target update. Let's rock June"
july = june.replace ("June","July")


valor = "44.036"
cambio_valor = valor.replace("." , ",")

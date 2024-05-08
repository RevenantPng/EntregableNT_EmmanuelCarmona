

usuarios = []

usuario = []

while len(usuarios) < 5:



    
    nombre = input("Inserte el nombre del usuario ")
    usuario.append(nombre)

    apellido = input("A continuación, inserte el apellido ")
    usuario.append(apellido)

    telefono = input("Inserte el número telefonico ")
    usuario.append(telefono)

    correo = input("Inserte el correo ")
    usuario.append(correo)

    clave = input("Inserte la clave de la sesión ")
    usuario.append(clave)

    usuarios.append(usuario)


for i in usuarios:
    print(i)




user = "pp@mail.com"
key = 1234


usuario = input("Usuario")

clave = int(input("Clave"))

usuario = input("Sea bienvenido al sistema, digite su usario")
clave = int(input("Ingresaste con exito"))

# Usuario if-else cree un sistema de login que valida las credenciales, si cumple permita iniciar sesion
# y si no, que imprima un mensaje de validar credenciales


if usuario == user:
    print("¡Proporcionaste los datos con exito!")
elif usuario and not user:
    print("Su Correo es incorrecto")

if key == clave:
    print("¡Proporcionaste los datos con exito!")
elif clave and not key:
    print("Su clave es incorrecta")




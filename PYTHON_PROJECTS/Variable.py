
# Las variables en python son de tipado dinámico

name = "Pepito"
#Notacion snake
last_name = "Perez"
mail = "pepito@mail.com"
salary = 1300000
state = True
note = 4.5
gender = 'm'

print(mail)

# Hablemos de contenacion + 

print("Nombre" + name)

# Hablemos de contenacion ,

print("correo", mail)

# Hablemos de contenacion format

print(f"Nombre {name}\n Apellido {last_name}\n Correo {mail}\n Salario {salary}")

# type me érmite conocer de que equipo es una variable

print(type(salary))


# Como capturar datos desde la consola  input()

phone = input("Telefono: ")

print(f"Telefono:{phone}")

aux_transporte = int(input("Ingrese el aux de Transporte"))

total_salary = salary + aux_transporte

print(f"El salario total es {total_salary}")

per_loan_discount = 0.3

loan_discount = salary * per_loan_discount

total_salary = salary + aux_transporte - loan_discount

print(f"El salario total es {total_salary} \n Descuentos: \n Prestamos: {loan_discount}")


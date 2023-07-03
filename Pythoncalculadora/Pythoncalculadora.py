from asyncio.windows_events import NULL
from email.message import EmailMessage


while True:
    try:
        nombre=input("Cual es su nombre?")
    except ValueError:
        print("es obligatorio este campo")
        continue
    if  not nombre:
        print("es obligatorio este campo")
        continue
    else:
        break
while True:
     try:
        apedad=input("Cual es su primer apellido? ")
     except ValueError:
        print("es obligatorio este campo")
        continue
     if  not apedad:
        print("es obligatorio este campo")
        continue
     else:
        break

while True:
    try:
        apemom=input("Cual es su segundo apellido? ")
    except ValueError:
        print("es obligatorio este campo")
        continue
    if  not apemom:
        print("es obligatorio este campo")
        continue
    else:
        break
while True:
    try:
        edad=int(input("Cual es su edad?"))
    except ValueError:
        print("debe ser un numero entero")
        continue
    if  not edad:
        print("es obligatorio este campo")
        continue
    else:
        break
while True:
    try:
        estatura= float(input("Cual es su estatura?"))
    except ValueError:
        print("debe ser un numero")
        continue
    if  not estatura:
        print("es obligatorio este campo")
        continue
    else:
        break
while True:
    try:
        peso= float(input("Cual es su peso?"))
    except ValueError:
        print("debe ser un numero")
        continue
    if  not peso:
        print("es obligatorio este campo")
        continue
    else:
        break

imc=peso/estatura**2
print ("usted "+nombre+" "+apedad+" "+apemom+" de "+edad+" tiene un indice de masa corporal de: ")
print (imc)


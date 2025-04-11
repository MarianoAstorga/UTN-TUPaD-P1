#Actividad 1
edad = int(input("Ingresa su edad: "))

if edad > 18:
    print("Es mayor de edad")

#Actividad 2
nota = float(input("Ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad 3
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Ingresaste un número par")
else:
    print("Por favor, ingresa un número par")

#Actividad 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Actividad 5
contraseña = input("Ingresa una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ingresaste una contraseña correcta")
else:
    print("Por favor, ingresa una contraseña de entre 8 y 14 caracteres")

#Actividad 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
moda_valor = mode(numeros_aleatorios)


print("Lista de números aleatorios:")
print(numeros_aleatorios)
print("\nMedia:", media_valor)
print("Mediana:", mediana_valor)
print("Moda:", moda_valor)


if media_valor > mediana_valor > moda_valor:
    print("\nDistribución con sesgo positivo (a la derecha).")
elif media_valor < mediana_valor < moda_valor:
    print("\nDistribución con sesgo negativo (a la izquierda).")
elif media_valor == mediana_valor == moda_valor:
    print("\nDistribución sin sesgo.")
else:
    print("\nLa distribución no presenta un sesgo claro.")

#Actividad 7
texto = input("Ingresa una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"
    
print("Resultado:", texto)

#Actividad 8
nombre = input("Ingresa tu nombre: ")
opcion = int(input("Ingresa una opción (1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula): "))
    
if opcion == 1:
    resultado = nombre.upper()  
    print(f"tu nombre en mayúsculas es: {resultado}")
elif opcion == 2:
    resultado = nombre.lower()  
    print(f"tu nombre en minúsculas es: {resultado}")
elif opcion == 3:
    resultado = nombre.title()  
    print(f"tu nombre con la primera letra mayúscula es: {resultado}")
else:
    print("Error: Por favor, selecciona una opción válida (1, 2 o 3)")

#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día del mes es?: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha no válida"

if hemisferio == "N":
    print("Estás en", estacion_norte)
elif hemisferio == "S":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio no reconocido. Usa 'N' o 'S'.")
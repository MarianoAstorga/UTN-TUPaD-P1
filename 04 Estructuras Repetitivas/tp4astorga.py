#Actividad 1

for i in range(101):
    print(i)

#Actividad 2

numero = input("Ingresa un número entero: ")
print(f"El número tiene {len(numero)} dígitos")

#Actividad 3

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(min(inicio, fin)+1, max(inicio, fin)):
    suma += i

print(f"La suma es: {suma}")

#Actividad 4

total = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"Total acumulado: {total}")

#Actividad 5

import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break
    print("Intenta nuevamente.")

#Actividad 6

for i in range(100, -1, -2):
    print(i)

#Actividad 7

limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(limite + 1):
    suma += i
print(f"La suma es: {suma}")

#Actividad 8

pares = impares = positivos = negativos = 0

for _ in range(100):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}")
print(f"Positivos: {positivos}, Negativos: {negativos}")

#Actividad 9

total = 0
for _ in range(100):
    num = int(input("Ingrese un número: "))
    total += num

media = total / 100
print(f"La media es: {media}")

#Actividad 10

numero = input("Ingrese un número: ")
invertido = numero[::-1]
print(f"Número invertido: {invertido}")
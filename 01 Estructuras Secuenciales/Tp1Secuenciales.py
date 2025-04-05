#Actividad 1
print("Hola Mundo")

#Actividad 2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#Actividad 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#Actividad 4
radio = float(input("Ingresa el radio del círculo: "))
area = 3.14 * (radio * radio)
perimetro = 2 * 3.14 * radio
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)

#Actividad 5
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print("Eso equivale a", horas, "horas.")

#Activididad 6
numero = int(input("Ingresa un número: "))
print("Tabla de multiplicar del", numero)
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#Actividad 7
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)

#Actividad 8
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura * altura)
print("Tu IMC es:", imc)

#Actividad 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print("La temperatura en Fahrenheit es:", fahrenheit)

#Actividad 10
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio de los tres números es:", promedio)
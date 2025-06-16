from funcionesUtiles import *

#Actividad 1
def main():
    imprimir_hola_mundo()

#Actividad 2
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

#Actividad3
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

#Actividad 4
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

#Actividad 5
    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas.")

#Actividad 6
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

#Actividad 7
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

#Actividad 8
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

#Actividad 9
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f}°F")

#Actividad 10
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
    print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")

if __name__ == "__main__":
    main()

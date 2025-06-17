from funcionesUtiles import *
def main():
    
#Actividad 1
    limite = int(input("Ingresa un número: "))
    for i in range(1, limite + 1):
        print(f"{i}! = {factorial(i)}")

#Actividad 2
    n = int(input("Ingrese la posición máxima de la serie de Fibonacci: "))
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci(i)}")

#Actividad 3
    b = int(input("Base: "))
    e = int(input("Exponente: "))
    print(f"{b}^{e} = {potencia(b, e)}")

#Actividad 4
    numero = int(input("Ingrese un Número decimal a convertir en binario: "))
    binario = decimal_a_binario(numero)
    print(f"Binario: {binario if binario else '0'}")

#Actividad 5
    texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    print("Es palíndromo:" if es_palindromo(texto) else "No es palíndromo.")

#Actividad 6
    num = int(input("Ingrese un número: "))
    print(f"Suma de dígitos: {suma_digitos(num)}")

#Actividad 7
    niveles = int(input("Bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

#Actividad 8
    numero = int(input("Número entero positivo: "))
    digito = int(input("Dígito a contar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")


if __name__ == "__main__":
    main()

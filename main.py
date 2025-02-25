from ejercicio1.palindromo import palindromo
from ejercicio2.calculoEdad import calcular_edad
from ejercicio3.generadorContraseñas import generar_contrasena
from ejercicio4.ahorcado import ahorcado
from ejercicio5.fibonacci import fibonacci

def menu():
    while True:
        print("\n--- Menú de Ejercicios ---")
        print("1. Verificar Palíndromo")
        print("2. Generar Fibonacci")
        print("3. Calcular Factorial")
        print("4. Verificar Número Primo")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            palabra = input("Ingresa una palabra o frase: ")
            print(f'¿Es palíndromo?: {palindromo(palabra)}')

        elif opcion == "2":
            n = int(input("¿Cuántos términos de Fibonacci deseas?: "))
            print(f'Secuencia de Fibonacci: {calcular_edad(n)}')

        elif opcion == "3":
            num = int(input("Ingresa un número para calcular su factorial: "))
            print(f'El factorial de {num} es {generar_contrasena(num)}')

        elif opcion == "4":
            num = int(input("Ingresa un número: "))
            print(f'¿El número {num} es primo?: {ahorcado(num)}')

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()

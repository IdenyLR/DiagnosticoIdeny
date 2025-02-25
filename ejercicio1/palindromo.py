def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[-(i + 1)]:
            return False
    return True

entrada = input("Ingresa una palabra: ")
if palindromo(entrada):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")

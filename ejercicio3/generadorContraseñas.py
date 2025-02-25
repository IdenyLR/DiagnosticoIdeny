import random
import string

def generar_contrasena(longitud=8):
    if longitud < 8:
        print("La longitud mínima es de 8 caracteres")
        longitud = 8


    mayuscula = random.choice(string.ascii_uppercase)  
    numero = random.choice(string.digits) 
    simbolo = random.choice(string.punctuation)  

    caracteres_restantes = random.choices(string.ascii_letters + string.digits + string.punctuation, k=longitud-3)
    contrasena_lista = list(mayuscula + numero + simbolo + ''.join(caracteres_restantes))
    random.shuffle(contrasena_lista)

    contrasena = ''.join(contrasena_lista)
    return contrasena

if __name__ == "__main__":
    longitud = int(input("Ingresa la longitud de la contraseña (mínimo 8 caracteres): "))


    contrasena = generar_contrasena(longitud)
    print(f"\nTu contraseña generada es: {contrasena}")

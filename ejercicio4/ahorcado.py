#Se genera una palabra aleatoria (oculta al usuario) y el usuario debe ingresar letra por letra para
#intentar adivinar la palabra, se debe validar que las letras coincidan con la posición de las letras de la
#palabra generada. Máximo 5 errores.

import random

def ahorcado():
    
    palabras = ["hardware", "programacion", "frontend", "bocina", "algoritmo"]
    
    palabra_secreta = random.choice(palabras)
    
    palabra_oculta = ["_"] * len(palabra_secreta)
    
    intentos_maximos = 5
    errores = 0
    
    print("Bienvenido a este juegoo, espero te diviertas")
    print("Tienes que adivinar la palabra letra por letra. Solo puedes fallar 5 veces")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")
    
    while errores < intentos_maximos:
        print("Palabra actual: ", " ".join(palabra_oculta))
        letra = input("Ingresa una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa solo una letra")
            continue
        

        if letra in palabra_secreta:
            print(f"Bien, La letra {letra} sí se encuentra en la palabra.")
            
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra
        else:
            #chance a 5 errores
            errores += 1
            print(f"Incorrecto, La letra {letra} no pertenece a esta palabra.")
            print(f"Te quedan {intentos_maximos - errores} intentos.")
        

        if "_" not in palabra_oculta:
            print(f"Felicidades :) ! Adivinaste la palabra: {palabra_secreta}")
            break
    
    if errores == intentos_maximos:
        print(f"Lol q mal fallaste :( La palabra secreta era: {palabra_secreta}")
ahorcado()

#- Algoritmo de Cálculo de edad exacta (año, mes, semana, día, hora). (Básico).
# • Realizar un algoritmo que calcula la edad de una persona. El usuario debe ingresar su año de
# nacimiento, día y hora.

#nota: En la instrucción no menciona que tambien se pida los meses entonces hice este código
# def calcular_edad():
    
#     año_nacimiento = int(input("Ingresa el año de nacimiento: "))
#     dia_nacimiento = int(input("Ingresa el día de nacimiento (1-31): "))
#     hora_nacimiento = int(input("Ingresa la hora de nacimiento (0-23): "))
#     año_actual = int(input("Ingresa el año actual: "))
#     dia_actual = int(input("Ingresa el día actual (1-31): "))
#     hora_actual = int(input("Ingresa la hora actual (0-23): "))
    
#     edad_años = año_actual - año_nacimiento
#     edad_dias = dia_actual - dia_nacimiento
#     edad_horas = hora_actual - hora_nacimiento

    
#     if edad_dias < 0:
#         edad_dias += 30  #generalizo q los meses tiene 30 días
#         edad_años -= 1

#     if edad_horas < 0:
#         edad_horas += 24
#         edad_dias -= 1

#     print(f"Edad exacta:")
#     print(f"Años: {edad_años} años")
#     print(f"Días: {edad_dias} días")
#     print(f"Horas: {edad_horas} horas")
# calcular_edad()

#codigo en caso de que hubieran pedido que el usuario igual debe ingresar el mes:
def calcular_edad():
    
    año_nacimiento = int(input("Ingresa el año de nacimiento: "))
    mes_nacimiento = int(input("Ingresa el mes de nacimiento (1-12): "))
    dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
    hora_nacimiento = int(input("Ingresa la hora de nacimiento (0-23): "))
    minuto_nacimiento = int(input("Ingresa los minutos de nacimiento (0-59): "))
    
    año_actual = int(input("Ingresa el año actual: "))
    mes_actual = int(input("Ingresa el mes actual (1-12): "))
    dia_actual = int(input("Ingresa el día actual: "))
    hora_actual = int(input("Ingresa la hora actual (0-23): "))
    minuto_actual = int(input("Ingresa los minutos actuales (0-59): "))
    

    edad_años = año_actual - año_nacimiento
    edad_meses = mes_actual - mes_nacimiento
    edad_dias = dia_actual - dia_nacimiento 
    edad_horas = hora_actual - hora_nacimiento
    edad_minutos = minuto_actual - minuto_nacimiento

    if edad_meses < 0:
        edad_meses += 12
        edad_años -= 1

    if edad_dias < 0:
        edad_dias += 30  
        edad_meses -= 1


    if edad_horas < 0:
        edad_horas += 24
        edad_dias -= 1

    if edad_minutos < 0:
        edad_minutos += 60
        edad_horas -= 1
    
    print(f"Edad exacta:"),
    print(f"Años: {edad_años} años")
    print(f"Meses: {edad_meses} meses")
    print(f"Días: {edad_dias} días")
    print(f"Horas: {edad_horas} horas")
    print(f"Minutos: {edad_minutos} minutos")
calcular_edad()

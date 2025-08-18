#Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
import datetime
hora_actual = datetime.datetime.now().hour
hora_decimal = datetime.datetime.now().time() 
if hora_actual < 8 or hora_actual >=21:
    print(f"Son las {hora_decimal}, asi que es de noche")
elif hora_actual >= 8 and hora_actual < 13:
    print(f"Son las {hora_decimal}, asi que es de mañana")
else:
    print(f"Son las {hora_decimal}, asi que es de tarde")
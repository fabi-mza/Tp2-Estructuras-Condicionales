# Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
# Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# Ejercicio 3
numero = int(input("Ingrese número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a.")
elif (edad >= 12) and (edad < 18):
    print("Adolescente.")
elif (edad >= 18) and (edad < 30):
    print("Adulto/a joven.")
else:
    print("Adulto/a.")
# Ejercicio 5
password = input("Ingrese una contraseña: ")
largo = len(password)
if 8 <= largo <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
# Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
promedio = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except:
    moda = mode(numeros_aleatorios)
print(f"Valores calculados:")
print(f"Media (mean): {promedio:.2f}")
print(f"Mediana (median): {mediana}")
print(f"Moda (mode): {moda}")
print("-" * 30)
if promedio > mediana > moda:
    print("Resultado: Sesgo positivo o a la derecha")
elif promedio < mediana < moda:
    print("Resultado: Sesgo negativo o a la izquierda")
elif promedio == mediana == moda:
    print("Resultado: Sin sesgo")
else:
    print("Resultado: Los datos no presentan un sesgo definido según el criterio estricto.")
# Ejercicio 7
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
if frase and frase[-1] in vocales:
    resultado = frase + "!"
else:
    resultado = frase
print(resultado)
# Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("Opciones disponibles:")
print("1: Todo en mayúsculas.")
print("2: Todo en minúsculas.")
print("3: Primera letra en mayúscula.")
opcion = int(input("Selecciona una opción (1, 2 o 3): "))
if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre.title()
else:
    resultado = "Opción no válida"
print(f"El resultado es: {resultado}")
# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    categoria = "Muy leve (imperceptible)."
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)."
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daño)."
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)."
elif 6 <= magnitud < 7:
    categoria = "Muy fuerte (puede causar daños significativos)."
else:
    categoria = "Extremo (puede causar graves daños a gran escala)."
print(f"Clasificación: {categoria}")
# Ejercicio 10
hemisferio = input("¿En que hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Ingresá el número del mes (1-12): "))
dia = int(input("Ingresá el día (1-31): "))
fecha = (mes, dia)
if (12, 21) <= fecha <= (12,31) or (1, 1) <= fecha <= (3, 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (3, 21) <= fecha <= (6, 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (6, 21) <= fecha <= (9, 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (9, 21) <= fecha <= (12, 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = None
    print("Fecha no Válida")
if estacion_norte:
    if hemisferio == "N":
        print(f"Te encuentras en: {estacion_norte}")
    elif hemisferio == "S":
        print(f"Te encuentras en: {estacion_sur}")
    else:
        print(f"Hemisferio no reconocido, ingresa N o S.")
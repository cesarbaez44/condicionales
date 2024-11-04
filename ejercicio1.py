#################################################################################
#Programa 1

# Programa que pida dos números e indique Cuál es el mayor
# Si los dos son iguales que muestre el mensaje "Son iguales"
#################################################################################

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 > numero2:
    print("El mayor es:",numero1)
elif numero1 < numero2:
    print("El mayor es:",numero2)
else:
    print("Son iguales")

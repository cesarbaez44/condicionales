#####################################################################################
#Programa 7

# Realiza un programa que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
#####################################################################################


base = int(input("\nIntroduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print("\nLa potencia es:",resultado)
elif exponente == 0:
    print("\nEl resultado es: 1")
else:  
    resultado = 1 / (base ** abs(exponente))
    print("\nLa potencia es:",resultado)

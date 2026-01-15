import random

numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def elegir_numero_random():
    x = ""
    if repite:
        x = elige_con_numeros_repetidos()
    else:
        while len(x) < CANT_DIGITOS:
            digito = random.choice(numeros)
            if digito not in x:
                x = x + digito
    return x


def elige_con_numeros_repetidos():
    x = ""
    while len(x) < CANT_DIGITOS:
        x = x + random.choice(numeros)
    return x


def pedir_numero(x):
    contador = 1
    while True:
        guess = input("Ingresa un número: ")
        if not guess.isdigit():
            print(f"Perdiste. El número era {x}")
            return False
        if guess == x:
            print(f"""Ganaste! el número era {
                  x}! Lo has adivinado en {contador} intentos""")
            return True
        aciertos = 0
        coincidencias = 0
        x_sin_g = list(x)
        i = 0
        for g in guess:
            if g == x[i]:
                x_sin_g.remove(g)
                aciertos += 1
            i += 1
        for g in guess:
            if g in x and g in x_sin_g:
                x_sin_g.remove(g)
                coincidencias += 1
        print(f"Tienes {aciertos} aciertos y {coincidencias} coincidencias")
        contador += 1


print("""Bienvenido a NUMBLE! Tienes que adivinar un número secreto.
Los dígitos que aciertes se contaran como aciertos
Los dígitos que se encuentren dentro del número pero en otra posición serán coincidencias""")
CANT_DIGITOS = int(
    input("Elige la cantidad de cifras que quieres que tenga el número "))
yes_or_no = input("Quieres que los dígitos se puedan repetir o no? (Y/N) ")
repite = yes_or_no.lower() == "y"
numero_secreto = elegir_numero_random()
pedir_numero(numero_secreto)

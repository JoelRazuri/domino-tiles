""" 
    Escribir un programa que imprima por pantalla todas las fichas de dominó, de
    una por línea y sin repetir.
"""

n = 6
contador = 0

for i in range(n+1):
    for j in range(contador,n+1):
        print(f"({i},{j})")
    contador+=1    
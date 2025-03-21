# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.2

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random

'''
Enunciado:
Alumno: Crear la función "contar"

Utilice la función "lista_aleatoria" creada antes 
para generar una lista de 5 números en
un rango de 1 a 6 inclusive

lista_numeros = lista_aleatoria(inicio, fin, cantidad)

Generar una una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista (también pasada por parámetro)

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior


# --------------------------------
def lista_aleatoria (inicio, fin, cantidad):
    lista_final = []

    for i in range(cantidad):
        numero = random.randrange(inicio, fin +1)
        lista_final.append(numero)
    
    return lista_final
# --------------------------------
# Aquí dentro definir la función contar
def contar (lista_numeros, numero_repe):
    repeticion = lista_numeros.count(numero_repe)

    return repeticion

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 1
    fin = 6
    cantidad = 5
    numero_repe = 3

    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive

    # lista_numeros = lista_aleatoria()

    lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    print('La lista aleatoria es =', lista_numeros)
    
    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":

    # print(lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    # cantidad_tres = contar(lista_numeros, 3)

    cantidad_repe = contar(lista_numeros, numero_repe)
    print('La cantidad de veces que se repite el nº', numero_repe, 'es =', cantidad_repe )

    # print(cantidad_tres)

    print("terminamos")
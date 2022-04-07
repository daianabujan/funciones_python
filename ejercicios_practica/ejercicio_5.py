# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada

def generar_invitados(cant_invitados):
    lista_invitados = []

    for i in range(cant_invitados):
        print('Ingrese el nombre del invitado', i)
        invitado = str(input())
        lista_invitados.append(invitado)
    
    return lista_invitados
# --------------------------------

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada

def lista_ordenada(lista_inv):
    ordenados = sorted(lista_inv)
    
    return ordenados
# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    cant_inv = 3
    
    lista_inv = generar_invitados(cant_inv)
    print('El listado de invitados es =', lista_inv)

    # lista_invitados = generar_invitados()

    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    lista_ordenada_inv = lista_ordenada(lista_inv)
    print('La lista ordenada de invitados es =', lista_ordenada_inv)
    # lista_invidatos_ordenada = ordenar(lista_invitados)

    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("terminamos")

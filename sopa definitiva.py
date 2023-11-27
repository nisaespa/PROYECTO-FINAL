import random
import numpy as np  #Probando con numpy


# Abecedario y dimensión de la matriz ingresados por el usuario
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
N = int(input("Ingrese la dimensión de la matriz (Un numero que N tal que 10<= N <= 30): "))


if 10<= N <= 30:
    palabras = []
    cuantas_palabras = int(input("¿Cuantas palabras desea ingresar? (ingrese un numero entero): "))

    for i in range(cuantas_palabras): #Ingreso las palabras en una lista para luego acceder a estas 
        palabra = input("Ingrese la palabra: ")
        palabras.append(palabra)





    # Función pa generar el cursor aleatorio con posición y dirección
    def generar_cursor(dimension):# Se genera el cursor que es como un puntero que decide aleatoriamente donde va a ser la posicion inicial y luego la dirección 

        fila = random.randint(0, dimension - 1)
        columna = random.randint(0, dimension - 1)
        avanX = random.choice([-1, 0, 1])
        avanY = random.choice([-1, 0, 1])


        if avanX == 0 and avanY == 0:
            avanX = 1
        return fila, columna, avanX, avanY


        # Función pa verificar si una palabra cabe en la matriz desde una posición y dirección dadas
    def palabra_cabe(ajiaco, palabra, cursor):
        x, y, avanX, avanY = cursor #Indican la posicion inicial y la direccion en la que se intentará colocar 

        for letra in palabra:
            # Verificar si la posición está dentro de la matriz
            if not (0 <= x < len(ajiaco) and 0 <= y < len(ajiaco[0])):
                return False
            x += avanX #En cada uno se va a actualizar la posicion x ^ y segun la direccion dada por avanX ^ avanY
            y += avanY

        return True  


    # Función pa colocar una palabra en la matriz a partir de una posición y dirección dadas
    def colocar_palabra(ajiaco, palabra, cursor): #Cursor será algo cmo un puntero que selecciona aleatoriamente cual será la posicion inicial de la palabra

        x, y, avanX, avanY = cursor
        for letra in palabra:
            # Verificanding si la posición está dentro de la matriz
            if 0 <= x < len(ajiaco) and 0 <= y < len(ajiaco[0]): #Si x ^ y tan en el rango del tamaño de la fila y columna 
                ajiaco[x][y] = letra

                x += avanX #Le suma cada x que avance
                y += avanY #Le suma cada y que avance

            #Ahora, ¿la palabra cabe
                

            else:
                    break
        return ajiaco

    # Función para colocar una palabra en la matriz a partir de una posición y dirección dadas
    def colocar_palabra(ajiaco, palabra, cursor):
            x, y, avanX, avanY = cursor

            for letra in palabra:
                # Verificar si la posición está dentro de la matriz
                if 0 <= x < len(ajiaco) and 0 <= y < len(ajiaco[0]):
                    ajiaco[x][y] = letra
                    x += avanX   #Haciendolo con cada letra, almacena cada avance en x como en y
                    y += avanY
                else:
                    break

            return ajiaco







    # Función para generar la matriz final con palabras colocadas aleatoriamente
    def generar_matriz_palabras(palabras, dimension):
        ajiaco = [[' '] * dimension for _ in range(dimension)] #Se llenará de espacios vacíos la sopa para luego acceder a esos espacios llenando con palabras y después con letras

        for palabra in palabras:
            # Intentar colocar la palabra hasta encontrar un espacio válido
            while True:  #Utilizo una bandera para hacer mientras 
                cursor = generar_cursor(dimension)
                if palabra_cabe(ajiaco, palabra, cursor): # E intenta hasta que se pueda poner la palabra 
                    ajiaco = colocar_palabra(ajiaco, palabra, cursor)
                    break

        return ajiaco #Retorna la matriz o sopa 



    # Función pa imprimir la matriz más pintosa

    #Tutoría 
    def imprimir_matriz(ajiaco):                                                                   
        regla = f"   {('0 1 2 3 4 5 6 7 8 9 ' * int(len(ajiaco) / 10 + 1))[:len(ajiaco) * 2]}\n" #Regla es la variable que determinará el numero de las colummnas , la cantidad de repeticiones se determina dividiendo todo sobre 10 + 1 para asegurar que hayan siempre numeros suficientes sobre las columanas
        linea = regla                                                                            #Tomando la parte que es el doble de la longitud de la matriz para cubrir bien las columnas
        for i, fila in enumerate(ajiaco):  #Uso enumarate para añadir la columna de numeros y sea más aspera la matriz de la sopa, obteniendo el indice de la fila y la fila 
            linea += f"{i:2d} {' '.join(fila)}\n" # Se pretende imprimir el numero de fila con al menos dos digitos para mantener la alineacion y se une las letras de la fila con un espacio entre ellas  
        print(linea + regla)


    def rellenar_sopa (ajiaco):  #Por cada espacio que encuentre vacio en la matriz que ya tiene ingresada las palabras, ponga una letra aleatoria
        for x in range(len(ajiaco)):
            for y in range(len(ajiaco)):
                if ajiaco[x][y] ==" ":
                    ajiaco[x][y] = np.random.choice(abecedario)



    # Generar la matriz final y mostrarla
    matriz_resultante = generar_matriz_palabras(palabras, N)
    rellenar_sopa(matriz_resultante)
    imprimir_matriz(matriz_resultante)




    # Hacer que el usuario encuentre palabras hasta que todas sean encontradas
    palabras_restantes = set(palabras.copy())  #Utilizo set para volver la lista palabras en un arreglo similar a las listas pero mucho más practica la eliminacion de palabras restantes


    # Función para encontrar palabras en la sopa
    def encontrar_palabra(ajiaco, inicio, fin):
        print(f"Inicio: {inicio}, Fin: {fin}")

        if inicio[0] == fin[0]: #Aqui, si la palabra está en la misma fila, utilizo slicing pa extraer la palabra  
            palabra_encontrada = ''.join(ajiaco[inicio[0]][min(inicio[1], fin[1]):max(inicio[1], fin[1]) + 1])
        elif inicio[1] == fin[1]: #Si las coordenadas pertencen a la misma columna, utilizo una comprensión de lista para obtener las letras de la palabra correspondiente en las filas min y max  
            palabra_encontrada = ''.join(ajiaco[i][inicio[1]] for i in range(min(inicio[0], fin[0]), max(inicio[0], fin[0]) + 1))
        else: #De no ser como lo anterior, es una coordenada diagonal donde utilizo la finción zip para extraer las letras de la sopa desde la posicion inicio y fin y luego las concatena para formar la palabra   
            palabra_encontrada = ''.join(ajiaco[i][j] for i, j in zip(range(inicio[0], fin[0] + 1), range(inicio[1], fin[1] + 1)))

        print(f"Palabra encontrada: {palabra_encontrada}") #Con fines de depuracion 
        return palabra_encontrada



    # Función para encontrar palabras en la sopa
    #def encontrar_palabra(ajiaco, inicio, fin):   #Es algo así como una submatriz que representa la palabra 
        #palabra_encontrada = ''.join(ajiaco[i][j] for i, j in zip(range(inicio[0], fin[0] + 1), range(inicio[1], fin[1] + 1))) #En este caso uso zip() que crea una iterabnle de tuplas wue parte de otrs objetos iterables 
    # return palabra_encontrada    #Después uso join para concatenar cada letra de la palabra, es algo como descomponerla y volverla a unir  








    while palabras_restantes:
        # Obtener coordenadas del usuario
        inicio = input("Ingrese la coordenada inicial (fila columna)(separando por un espacio la fila de la columna  ¡Siga la especificación por favor!): ").split() #Por cada palabra ingresada por el usuario, la descomopne en letras usando split
        fin = input("Ingrese la coordenada final (fila columna)(separando por un espacio la fila de la columna  ¡Siga la especificación por favor!): ").split()

        # Convertir las coordenadas a números enteros
        inicio = tuple(map(int, inicio))   #Convierte las cordenadas porporcionadas a numeros enteros y luego vuelve a almacenarlos en la variable inicio y fin 
        fin = tuple(map(int, fin))  #Utilizo la funcion map(int) para realizar comparaciones numericas y acceder elementos en la matriz

        # Verificar si las coordenadas son válidas
        if not (0 <= inicio[0] < N and 0 <= inicio[1] < N and 0 <= fin[0] < N and 0 <= fin[1] < N): #Se verifica sdi están dentro de la dimension de la sopa
            print("Coordenadas inválidas. Inténtelo de nuevo.")
            continue

        # Verificar si las coordenadas forman una línea recta #Esta es la manera en la que accedo a la palabra para eliminarla de la mtriz
        if inicio[0] == fin[0] or inicio[1] == fin[1]:
            # Extraer la palabra de la matriz
            palabra_encontrada = encontrar_palabra(matriz_resultante, inicio, fin)

            if palabra_encontrada in palabras_restantes:
                palabras_restantes.remove(palabra_encontrada)
                print(f"¡Encontraste la palabra '{palabra_encontrada}'!")
                print(f"Palabras restantes: {', '.join(palabras_restantes)}")
            else:
                print("No es una palabra válida. Inténtelo de nuevo.")
        else:
            print("Las coordenadas deben formar una línea recta. Inténtelo de nuevo.")

    # Mensaje de felicitaciones al encontrar todas las palabras
    print("¡Felicidades! ¡Has encontrado todas las palabras!")


else:
    print("Fue advertido de que el numero debía estar entre 10 y 30, ahora vuelva a correr el programa")









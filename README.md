# 🔥 INDUSPLAYTHON - PROYECTO FINAL 🔥
*Nicolas Estupiñan* - *Santiago Avendaño*
## 👽 Logo IndusPlaython 👽
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/LOGO%20indusplaython.jpg" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## 🕹️SALÓN DE JUEGOS INDUSPLAYTHON🕹️
####  🎮 Nuestro proyecto final trata de un salón o menú de 3 juegos, los cuales son: Ahorcado, Piedra, papel o tijera y Sopa de letras. 🎮 
####  🎮 El jugador podrá seguir las instrucciones e interactuar con la consola para jugar. 🎮
## 📚 Librerias usadas: 📚
```python
import random # Importar random, para valores aleatorios
from colorama import init, Back, Fore, Style # Importar de colorama init, back, fore y style para los colores de letra, de fondo y el estilo.
import time # Para controlar los tiempos entre las acciones
import os # Para limpiar la consola
import numpy as np # Probando con numpy, para la sopa de letras
```
### 📕 Random: Para los datos que necesitemos aleatorios. 📕
```python
import random
# Ejemplo de uso, genera un número aleatorio entre un intervalo
numero_aleatorio = random.randint(1, 10)
print("Número aleatorio:", numero_aleatorio)
```
### 📗 Colorama: Para añadir el color de la letra, el color del fondo de la letra y el estilo. 📗
```python
# Ejemplo de uso, color de letra amarillo, color de fondo negro y el estilo en este caso hará que se vea un poco más brillante.
from colorama import init, Back, Fore, Style
print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Letra amarilla, fondo negro")
```
### 📘 Time: Para controlar el tiempo entre cada acción. 📘
```python
# Ejemplo de uso, que imprima 'tiempo' y a los 5 segundos imprima'Hola mundo'.
import time
print("tiempo")
time.sleep(5)
print('Hola mundo')
```
### 📒 Os: Para limpiar la consola. 📒
```python
# Ejemplo de uso, imprime en consola "Limpiar consola" y luego limpia consola.
import os
print("Limpiar consola")
os.system("cls")
```

## 🎨 Generador de arte ASCCI 🎨
#### Además, se usó un generador de arte ASCCI para para hacer el hangman en el juego del ahorcado, decoraciones y la letra más grande, por ejemplo, en la intro del juego cuando se muestra el nombre del grupo, cuando se muestra el menú y cuando el jugador gana o pierde.

[Generador arte ASCCI](https://patorjk.com/software/taag/)

## 🎮 JUEGO 🎮

#### 🎮 El juego inicia mostrando el nombre del grupo "INDUSPLAYTHON", y luego aparece el menú con las opciones de juego, o la opción de salirse. 🎮

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in1.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 🎮 El jugador podrá elegir entre las 3 opciones de juego, o salirse. 🎮

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in2.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 🖐️✌️👊 En el juego de piedra, papel y tijera se enfrentan dos oponentes, cada uno con una cantidad de vidas. Siguiendo las reglas de que Piedra aplasta a Tijera, Papel envuelve Piedra y Tijera corta Papel. 🖐️✌️👊

<div align='center'>
<figure> <img src="https://static.vecteezy.com/system/resources/previews/000/693/099/non_2x/rock-paper-scissors-rules-vector-illustration.jpg" alt="" width="350" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 💻👨‍💻Sí elige el juego de piedra, papel y tijera, entonces tendrá la opción de elegir el modo para un jugador (jugador vs computador) o dos jugadores.👨‍💻👨‍💻

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in3.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 💻 Sí elige el modo para un jugador, tendrá que elegir también que dificultad quiere, esto definirá las vidas que tendrá. 👨‍💻
#### ❤️❤️❤️ Siendo fácil iniciar con 3 vidas, normal iniciar con 2 vidas y dificil iniciar con 1 vida. ❤️❤️❤️

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in4.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 🎮 En este caso el jugador escogió el modo fácil, entonces el jugador y la computadora empiezan con 3 vidas. Además tenemos un contador de las rondas. 🎮

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in5.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 🎮 El jugador escoge Piedra 👊 y la computadora escoge Tijera ✌️, Piedra aplasta a Tijera, entonces el jugador gana la ronda y la computadora pierde una vida. 🎮

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in6.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### 🤝 En caso de que lleguen a sacar la misma opción es empate y nadie pierde vidas. 🤝

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in7.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### Entonces sí el jugador gana la ronda, la computadora pierde una vida y sí la computadora gana la ronda el jugador pierde una vida. Pierde el que primero se quede sin vidas.


#### Cuando la computadora se queda sin vidas:
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in9.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### Cuando el jugador se queda sin vidas:
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in11.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### Demostraciones del juego: 

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in8.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in10.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### Sí escoge el modo de dos jugadores, los dos jugadores comenzarán con 3 vidas y podrán escribir su opción

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in12.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in13.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
14
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in14.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
15
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in15.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
16
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in16.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
17
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in17.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
18
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in18.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
19
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in19.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
20
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in20.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
21
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in21.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
22
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in22.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
23
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in23.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
24
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in24.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
25
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in25.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
26
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in26.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
27
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in27.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
28
<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/in28.png" alt="" width="700" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

#### Estableciendo un condicional para verificar que la dimensión de la sopa de letras sea un número N tal que 10<= N <= 30 se empezará a desarrollar el código, que empezará almacenando palabras ingresadas por el usuario en una lista para luego acceder a estas.

```python
# Abecedario y dimensión de la matriz ingresados por el usuario
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
N = int(input("Ingrese la dimensión de la matriz (Un numero que N tal que 10<= N <= 30): "))


if 10<= N <= 30:
    palabras = []
    cuantas_palabras = int(input("¿Cuantas palabras desea ingresar? (ingrese un numero entero): "))

    for i in range(cuantas_palabras): #Ingreso las palabras en una lista para luego acceder a estas 
        palabra = input("Ingrese la palabra: ")
        palabras.append(palabra)
```

#### Para hacer más específico cada paso, utilicé funciones para cada cosa que necesitaba que hiciera el programa, partiendo por generar la función que simula un puntero que decidirá aleatoriamente la posición donde será puesta cada palabra ingresada por el usuario, asimismo este puntero decide la dirección en la que estará la palabra, definiendo los avances en x ^ y como una pareja de escalares o un vector en R2.

```python
# Función pa generar el cursor aleatorio con posición y dirección
    def generar_cursor(dimension):# Se genera el cursor que es como un puntero que decide aleatoriamente donde va a ser la posicion inicial y luego la dirección 

        fila = random.randint(0, dimension - 1)
        columna = random.randint(0, dimension - 1)
        avanX = random.choice([-1, 0, 1])
        avanY = random.choice([-1, 0, 1])


        if avanX == 0 and avanY == 0:
            avanX = 1
        return fila, columna, avanX, avanY
```

#### La función posterior a esta, es una verificación sobre el espacio suficiente para cada palabra, si bien no se usa len() para medir la longitud de la palabra, se verificará letra por letra si esta cabe en el siguiente, actualizando cada coordenada en x ^ y por cada letra, utilizando valores booleanos decidirá si es posible poner la palabra o no, decidiendo esto letra por letra. (Cabe la posibilidad de que se omitan palabras).


```python
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
```

  
#### La función posterior (colocar_palabra) tiene un funcionamiento similar a la anterior, ya que evalúa si es posible colocar cada letra y en dado caso la posición de la matriz: ajiaco, será la letra en cuestión.

```python
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
```
  
#### Para generar la matriz: ajiaco, se usarán listas que luego se llenarán de espacio de vacios,  y posterior a esto se llamarán las funciones anteriores para poner en la matriz las palabras y dejar espacios vacíos donde no haya palabras.  En la función: generar_matriz, se pretende hacer esto de una manera agradable , por lo que se imprimirán los índices de fila y de columna, asegurando también que por cada fila haya una columna . Posterior a esto se llenará cada espacio vacío restante con letras aleatorias.

```python
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
```

#### Para mostrar todo lo anterior en la consola, se accederán a las funciones establecidas previamente.

```python
# Generar la matriz final y mostrarla
matriz_resultante = generar_matriz_palabras(palabras, N)
rellenar_sopa(matriz_resultante)
imprimir_matriz(matriz_resultante)
```
#### Con fin de terminar el código, se establecen las funciones para encontrar las  palabras y la lógica que estas tendrán, donde se evaluará las coordenadas iniciales y finales de cada palabra, y en cada caso se usará un método de extracción de estas de la matriz ya que el código presentó constantes problemas mientras se usaba el mismo método de extracción para los tres casos.

```python
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
```

#### Finalizando el código, se utiliza un ciclo while para iterar mientras hayan palabras en la lista: [palabras_restantes], donde serán solicitadas al usuario, las coordenadas iniciales y finales de la palabra, convirtiendo estas a enteros y evaluando si estas coordenadas si corresponden a una palabra. En este punto el código presenta un problema que no encontramos cómo solucionar y es que al evaluar las coordenadas, en caso de que correspondan a una palabra, imprime: Encontraste la palabra, sin embargo también imprime: No es una palabra válida, inténtelo de nuevo, como si las coordenadas no coincidieran con una palabra en la matriz, por lo que fué editada la función: encontrar_palabras hasta que esto se solucionó, sin embargo fue una solución parcial, ya que funcionó en los primeros dos intentos de usar el código y se volvió al mismo problema

```python
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
```

+ Resultado

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/resultado1.png" alt="" width="1000" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

<div align='center'>
<figure> <img src="https://raw.githubusercontent.com/nisaespa/PROYECTO-FINAL/main/imagenes%20proyecto%20final/resultado2.png" alt="" width="1000" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

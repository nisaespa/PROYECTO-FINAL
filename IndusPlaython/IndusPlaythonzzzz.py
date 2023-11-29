import random # Importar random, para valores aleatorios
from colorama import Back, Fore, Style # Importar de colorama init, back, fore y style para los colores de letra, de fondo y el estilo.
import time # Para controlar los tiempos entre las acciones
import os # Para limpiar la consola
import numpy as np # Para la sopa de letras
# El programa trata de un salón o menú de tres juegos básicos de python: AHORCADO, SOPA DE LETRAS Y PIEDRA PAPEL O TIJERA. Con interacción con la consola.
# Desde el menú se puede elegir que juego jugar
# Cuando acabemos de jugar el juego que elegimos se devuelve al menú
# ---- COMENZEMOS ----
# CANTIDAD DE JUGADORES PIEDRA PAPEL O TIJERA
def juego_piedra_papel_o_tijera():  # Función para seleccionar cantidad de jugadores.
    # Impresión de un mensaje de bienvenida con formato y colores
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "")
    os.system("cls")
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + """
. _   ___ ___ ___ _  ___   _____ _  _ ___ ___   ___      _   _       .
.(_) | _ )_ _| __| \| \ \ / / __| \| |_ _|   \ / _ \    /_\ | |      .
.| | | _ \| || _|| .` |\ V /| _|| .` || || |) | (_) |  / _ \| |__    .
.|_| |___/___|___|_|\_|_\_/ |___|_|\_|___|___/_\___/ _/_/ \_\____|   .
.    _ _   _ ___ ___  ___    ___  ___    ___ ___ ___ ___  ___    _   .
. _ | | | | | __/ __|/ _ \  |   \| __|  | _ \_ _| __|   \| _ \  /_\  .
.| || | |_| | _| (_ | (_) | | |) | _|   |  _/| || _|| |) |   / / _ \ .
. \__/ \___/|___\___|\___/  |___/|___|__|_|_|___|___|___/|_|_\/_/ \_\.
.  ___  _   ___ ___ _       ___    _____ ___   _ ___ ___    _     _  .
. | _ \/_\ | _ \ __| |     / _ \  |_   _|_ _| | | __| _ \  /_\   | | .
. |  _/ _ \|  _/ _|| |__  | (_) |   | |  | | || | _||   / / _ \  |_| .
. |_|/_/ \_\_| |___|____|  \___/    |_| |___\__/|___|_|_\/_/ \_\ (_) .
                                                                      """)
    time.sleep(3)
    os.system("cls")
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "")
    # Bucle infinito para permitir al jugador elegir la cantidad de jugadores
    while True:
        # Mensaje para que el jugador elija la cantidad de jugadores
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "ELIJE LA CANTIDAD DE JUGADORES                                                                ")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "1. Un jugador                                                                                 ")
        print("2. Dos jugadores                                                                              ")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")

        # Solicitar al jugador para la cantidad de jugadores
        jugadores = input("Ingresa la cantidad de jugadores:                                                            ")

        # Verificar la elección del jugador y llamar a la función correspondiente
        if jugadores == '1':
            juego_piedra_papel_o_tijera_un_jugador()  # Llamar a la función para un jugador
            break
        elif jugadores == '2':
            juego_piedra_papel_o_tijera_dos_jugadores()  # Llamar a la función para dos jugadores
            break
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido. ('1','2')")  # Mensaje de error si la entrada no es válida
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
# DIFICULTAD MODO UN JUGADOR
def dificultad_un_jugador(): # Función para seleccionar la dificultad
    # Espaciado
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    # Inicialización de la variable que almacenará las vidas del jugador
    vidas_jugador = 0  
    # Bucle infinito para que el jugador seleccione la dificultad
    while True:
        # Mensaje para que el jugador elija el nivel de dificultad
        os.system("cls")
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "SELECCIONA EL NIVEL DE DIFICULTAD PARA UN JUGADOR")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print(Fore.RED + Back.BLACK + Style.BRIGHT +"")
        # Solicitar al jugador para la selección de dificultad
        seleccionar_dificultad_un_jugador = input("Escriba el número correspondiente a la dificultad que\ndesee contra la computadora, esto definirá las vidas \nque tendrá (1 = 3 vidas, 2 = 2 vidas, 3 = 1 vida):  ")
        # Verificar la elección del jugador y asignar las vidas correspondientes
        if seleccionar_dificultad_un_jugador == '1':
            vidas_jugador = 3
            break
        elif seleccionar_dificultad_un_jugador == '2':
            vidas_jugador = 2
            break
        elif seleccionar_dificultad_un_jugador == '3':
            vidas_jugador = 1
            break
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.('1','2','3')")
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
    return vidas_jugador  # Devolver el número de vidas seleccionado por el jugador
# UN JUGADOR PIEDRA PAPEL O TIJERA
def juego_piedra_papel_o_tijera_un_jugador(): # Función principal del juego
    # Espaciado
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    vidas_computadora = 3  # Inicialización de las vidas de la computadora
    rondas = 1  # Inicialización del contador de rondas
    vidas_jugador = dificultad_un_jugador()  # Obtener la cantidad de vidas del jugador mediante la función dificultad_un_jugador()

    # Bucle principal del juego
    while True:
        # Impresión de la presentación del juego en cada ronda
        time.sleep(1)
        os.system("cls")
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + f'       RONDAS!!!: {rondas}           ')
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'')

        # Impresión de las vidas de la computadora
        if vidas_computadora == 3:   
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas de la computadora: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤ ')
        elif vidas_computadora == 2:
            print('Vidas de la computadora: ' + Fore.RED + Back.BLACK + Style.BRIGHT + ' ❤ ❤ ')
        elif vidas_computadora == 1:
            print('Vidas de la computadora: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ') 
    
        # Impresión de las vidas del jugador
        if vidas_jugador == 3:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤ ')
        elif vidas_jugador == 2:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ')
        elif vidas_jugador == 1: 
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ') 
        
        rondas += 1  # Incremento del contador de rondas
        opcion_del_jugador, opcion_del_computador = seleccionar_opciones_uno()  # Obtener las opciones elegidas por el jugador y la computadora
        vidas_jugador, vidas_computadora = reglas_piedra_papel_o_tijera_un_jugador(opcion_del_jugador, opcion_del_computador, vidas_jugador, vidas_computadora)  # Aplicar las reglas del juego
        
        # Verificar si la computadora ha perdido todas sus vidas
        if vidas_computadora == 0:
            # Tiempo de espera
            time.sleep(2)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
          _____          _   _           _____ _______ ______        ___  
         / ____|   /\   | \ | |   /\    / ____|__   __|  ____|    _ / _ \ 
        | |  __   /  \  |  \| |  /  \  | (___    | |  | |__     (_) | | |
        | | |_ | / /\ \ | . ` | / /\ \  \___ \   | |  |  __|      | | | |
        | |__| |/ ____ \| |\  |/ ____ \ ____) |  | |  | |____    _| |_| |
        \_____/_/    \_ \_| \_/_/    \_\_____/   |_|  |______|   (_)\___/ 
                                                                 
                                                                 """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(3)
            # Limpiar
            os.system("cls")
            seleccionar_juego()  # Volver a la selección del juego
        
        # Verificar si el jugador ha perdido todas sus vidas
        if vidas_jugador == 0:
            # Tiempo de espera
            time.sleep(2)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
         _____  ______ _____  _____ _____  _____ _______ ______      __
        |  __ \|  ____|  __ \|  __ \_   _|/ ____|__   __|  ____|  _ / /
        | |__) | |__  | |__) | |  | || | | (___    | |  | |__    (_) | 
        |  ___/|  __| |  _  /| |  | || |  \___ \   | |  |  __|     | | 
        | |    | |____| | \ \| |__| || |_ ____) |  | |  | |____   _| | 
        |_|    |______|_|  \_\_____/_____|_____/   |_|  |______| (_) | 
                                                                    \_\.
                                                                             
                  """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(3)
            # Limpiar consola
            os.system("cls")
            seleccionar_juego()  # Volver a la selección del juego
# SELECCIÓN DE OPCIONES UN JUGADOR
def seleccionar_opciones_uno(): # Selección de opciones del computador y del jugador
    # Espaciado
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    # Opciones del juego en una tupla
    opciones = ('piedra', 'papel', 'tijera')
    # Bucle para que el jugador elija una opción válida
    while True:
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")
        opcion_del_jugador = input('Elige entre piedra, papel o tijera: ')
        # Convertir la opción del jugador a minúsculas
        opcion_del_jugador = opcion_del_jugador.lower()
        # Verificar si la opción del jugador está en la tupla de opciones
        if not opcion_del_jugador in opciones:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + 'Esa opción no es válida.')
        else:
            # Usar random.choice para que el computador escoja una opción aleatoria de la tupla
            opcion_del_computador = random.choice(opciones)
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + 'Opción del jugador: ', opcion_del_jugador)
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + 'Opción del computador: ', opcion_del_computador)
            time.sleep(2)
            return opcion_del_jugador, opcion_del_computador
# REGLAS UN JUGADOR
def reglas_piedra_papel_o_tijera_un_jugador(opcion_del_jugador, opcion_del_computador, vidas_jugador, vidas_computadora): # Función para definir las reglas
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"") 
    # Sí son la misma opción, entonces es empate
    if opcion_del_jugador == opcion_del_computador:
        # Mensaje de empate
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         EMPATE               ')
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
    # Opciones para que el jugador gane
    elif opcion_del_jugador == 'piedra':
        if opcion_del_computador == 'tijera':
            # Imprimir que opcion le gana a que opcion
            print('piedra gana a tijera')
            # Mensaje de que ganó el jugador
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR GANÓ        ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            # Se descuentan vidas
            vidas_computadora -= 1
        # Opciones para que el computador gane    
        else: 
            # Imprimir que opcion le gana a que opcion
            print('papel gana a piedra')
            # Imprimir que el computador ganó
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         COMPUTADOR GANÓ        ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            # Se descuentan vidas
            vidas_jugador -= 1
    # Opciones para que el jugador gane
    elif opcion_del_jugador == 'papel':
        if opcion_del_computador == 'piedra':
            # Imprimir que opcion le gana a que opcion
            print('papel gana a piedra')
            # Imprimir que jugador ganó
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            # Se descuentan vidas
            vidas_computadora -= 1
        # Opciones para que el computador gane
        else:
            # Imprimir que opcion le gana a que opcion
            print('tijera gana a papel')
            # Imprimir que el computador ganó
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         COMPUTADOR GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            # Se descuentan vidas
            vidas_jugador -= 1
    # Opciones para que el jugador gane
    elif opcion_del_jugador == 'tijera':
        if opcion_del_computador == 'papel':
            # Imprimir que opcion le gana a que opcion
            print('tijera gana a papel')
            # Imprimir que el jugador ganó
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            # Se descuentan vidas
            vidas_computadora -= 1
        # Opciones para que el computador gane
        else:
            # Imprimir que opcion le gana a que opcion
            print('piedra gana a tijera')
            # Imprimir mensaje del ganador
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         COMPUTADOR GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            # Se descuentan vidas
            vidas_jugador -= 1
    # Retornar vidas
    return vidas_jugador, vidas_computadora
# DOS JUGADORES PIEDRA PAPEL O TIJERA
def juego_piedra_papel_o_tijera_dos_jugadores(): # Función principal juego
    # Salto de línea y color
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    # Los jugadores comienzan con 3 vidas
    vidas_jugador_1 = 3
    vidas_jugador_2 = 3
    # Rondas comienza en 1
    rondas = 1
    # Bucle infinito
    while True:
        # Esperar un segundo para limpiar consola
        time.sleep(1)
        # Se limpia consola
        os.system("cls")
        # Se imprimen las rondas
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + f'       RONDAS!!!: {rondas}           ')
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
        # Sí las vidas son 3 imprimir los 3 corazones 
        if vidas_jugador_1 == 3:
            print('Vidas del jugador 1: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤ ')
        # Sí las vidas son 2 imprimir los 2 corazones 
        elif vidas_jugador_1 == 2:
            print('Vidas del jugador 1: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ')
        # Sí las vidas son 1 imprimir los 1 corazones 
        elif vidas_jugador_1 == 1:
            print('Vidas del jugador 1: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ')
        # Sí las vidas son 3 imprimir los 3 corazones 
        if vidas_jugador_2 == 3:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador 2: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤ ')
        # Sí las vidas son 2 imprimir los 2 corazones 
        elif vidas_jugador_2 == 2:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador 2: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ')
        # Sí las vidas son 1 imprimir los 1 corazones 
        elif vidas_jugador_2 == 1:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador 2: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ')
        # Opción del jugador dependiendo el jugador llama a la función con el argumento de 1 o 2 según el número del jugador
        # Para jugador 1
        opcion_jugador_1 = seleccionar_opciones_dos(1)
        # Para jugador 2
        opcion_jugador_2 = seleccionar_opciones_dos(2)
        # Dos variables que contienen la función de reglas
        vidas_jugador_1, vidas_jugador_2 = reglas2(opcion_jugador_1, opcion_jugador_2, vidas_jugador_1, vidas_jugador_2)
        rondas += 1
        # Gana jugador 2 sí:
        if vidas_jugador_1 == 0: 
            # Se muestra mensaje para el ganador
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
         ___ _    ___   _   _  _   _   ___   ___  ___    ___ ___ 
        | __| |  / __| /_\ | \| | /_\ |   \ / _ \| _ \  | __/ __|
        | _|| | | (_ |/ _ \| .` |/ _ \| |) | (_) |   /  | _|\__ \.
        |___|_|  \___/_/ \_\_|\_/_/ \_\___/ \___/|_|_\  |___|___/
        
                                                         """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(2)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
       _ _   _  ___   _   ___   ___  ___   ___   ___  ___   _   _   _ 
    _ | | | | |/ __| /_\ |   \ / _ \| _ \ |   \ / _ \/ __| | | | | | |
   | || | |_| | (_ |/ _ \| |) | (_) |   / | |) | (_) \__ \ |_| |_| |_|
    \__/ \___/ \___/_/ \_\___/ \___/|_|_\ |___/ \___/|___/ (_) (_) (_)
                                                                                      """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(3)
            # Limpiar consola
            os.system("cls")
            # Ir al menú
            seleccionar_juego()
        # Gana jugador 1 sí:
        if vidas_jugador_2 == 0: 
            # Se muestra mensaje para el ganador
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
         ___ _    ___   _   _  _   _   ___   ___  ___    ___ ___ 
        | __| |  / __| /_\ | \| | /_\ |   \ / _ \| _ \  | __/ __|
        | _|| | | (_ |/ _ \| .` |/ _ \| |) | (_) |   /  | _|\__ \.
        |___|_|  \___/_/ \_\_|\_/_/ \_\___/ \___/|_|_\  |___|___/
                                                                """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(2)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
       _ _   _  ___   _   ___   ___  ___   _   _ _  _  ___    _   _   _ 
    _ | | | | |/ __| /_\ |   \ / _ \| _ \ | | | | \| |/ _ \  | | | | | |
   | || | |_| | (_ |/ _ \| |) | (_) |   / | |_| | .` | (_) | |_| |_| |_|
    \__/ \___/ \___/_/ \_\___/ \___/|_|_\  \___/|_|\_|\___/  (_) (_) (_)
                                                                                        """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(3)
            # Limpiar consola
            os.system("cls")
            # Ir al menú
            seleccionar_juego()    
# SELECIÓN DE OPCIONES DOS
def seleccionar_opciones_dos(jugador): # El argumento jugador, luego será un '1' y '2'
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    # Opciones en una tupla
    opciones = ('piedra', 'papel', 'tijera')
    # Bucle infinito
    while True:
        print(Fore.RED + Back.BLACK + Style.BRIGHT +"")
        # Se muestran las opciones
        opcion_jugador = input(f'Elige entre piedra, papel o tijera jugador {jugador}: ')
        # Se pone en mayuscula la opcion del jugador
        opcion_jugador = opcion_jugador.lower()
        # Sí la opción del jugador 1 es valida retorna la opción
        # Sí la opción del jugador 2 es valida retorna la opción
        if opcion_jugador in opciones:
            return opcion_jugador
        # Vuelve y se repite el ciclo hasta que se ingrese validamente
        else:
            # Imprimir mensaje para volver a intentar
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Opción no válida. Por favor, elige "piedra", "papel" o "tijera".')
            # Esperar 2 segundos
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
# REGLAS DOS JUGADORES
def reglas2(opcion_jugador_1, opcion_jugador_2, vidas_jugador_1, vidas_jugador_2): # La función tiene como argumentos las opciones y las vidas de los jugadores
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    # Sí son la misma opción, entonces es empate
    if opcion_jugador_1 == opcion_jugador_2:
        # Imprimir mensaje de empate
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         EMPATE               ')
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___         
 |___|___|___|___|___|        
                              """)
    # Condición para que gane jugador 1
    elif opcion_jugador_1 == 'piedra':
        if opcion_jugador_2 == 'tijera':
            print('Piedra gana a tijera')
            print('Jugador 1 gana')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR 1 GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            vidas_jugador_2 -= 1
        else:
            print('Papel gana a piedra')
            print('Jugador 2 gana')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR 2 GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            vidas_jugador_1 -= 1
            
    elif opcion_jugador_1 == 'papel':
        if opcion_jugador_2 == 'piedra':
            print('Papel gana a piedra')
            print('Jugador 1 gana')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR 1 GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            vidas_jugador_2 -= 1
        else:
            print('Tijera gana a papel')
            print('Jugador 2 gana')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR 2 GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            vidas_jugador_1 -= 1
    elif opcion_jugador_1 == 'tijera':
        if opcion_jugador_2 == 'papel':
            print('Tijera gana a papel')
            print('Jugador 1 gana')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR 1 GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            vidas_jugador_2 -= 1
        else:
            print('Piedra gana a tijera')
            print('Jugador 2 gana')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         JUGADOR 2 GANÓ')
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ ___ ___ 
 |___|___|___|___|___|___|___|
                              """)
            vidas_jugador_1 -= 1
    return vidas_jugador_1, vidas_jugador_2
# AHORCADO 
def juego_ahorcado(): # Función principal del juego del ahorcado 
    # Lista con el hangman
    hangman = ['''
  /°°°\.
  |   |
      |
      |
      |
      |
=========''', '''
  /°°°\.
  |   |
  O   |
      |
      |
      |
=========''', '''
  /°°°\.
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  /°°°\.
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  /°°°\.
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  /°°°\.
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  /°°°\.
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  /°°°\.
  |   |
 x x  |
 /|\  |
 / \  |
      |
=========''']
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "")
    # Variable es igual a la función de seleccion de palabra, de donde traera de la lista una palabra aleatoria
    palabra_secreta = seleccionar_palabra()
    # Iniciar lista vacia para almacenar las letras adivinadas
    letras_adivinadas = []
    # Iniciar lista vacia para almacenar las letras intentadas
    letras_intentadas = []
    # Los intentos máximos es el número que retorna la función de la dificultad del ahorcado
    intentos_maximos = dificultad_ahorcado()
    # Intentos comienza en 0
    intentos = 0
    # Muestra el tablero, en este caso, solo con los guiones bajo
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))
    # Bucle infinito
    while True:
        # Cuando se selecciona la dificultad fácil
        # Se usan condiciones para utilizar todas las posiciones de la lista del hangman
        if intentos_maximos == 7:
            if intentos == 1:
                hangman_ascci = hangman[0]
                print(Fore.RED + Back.BLACK + Style.BRIGHT + hangman_ascci)
            elif intentos == 2:
                hangman_ascci = hangman[1]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 3:
                hangman_ascci = hangman[2]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 4:
                hangman_ascci = hangman[3]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 5:
                hangman_ascci = hangman[4]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 6:
                hangman_ascci = hangman[5]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 7:
                hangman_ascci = hangman[6]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
        # Cuando se selecciona la dificultad normal
        # Se usan condiciones para utilizar todas las posiciones de la lista del hangman, menos la primera
        elif intentos_maximos == 6:
            if intentos == 1:
                hangman_ascci = hangman[0]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 2:
                hangman_ascci = hangman[2]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 3:
                hangman_ascci = hangman[3]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 4:
                hangman_ascci = hangman[4]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 5:
                hangman_ascci = hangman[5]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 6:
                hangman_ascci = hangman[6]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
        # Cuando se selecciona la dificultad dificil
        # Se usan condiciones para utilizar todas las posiciones de la lista del hangman, menos las dos primeras
        elif intentos_maximos == 5:
            if intentos == 1:
                hangman_ascci = hangman[0]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 2:
                hangman_ascci = hangman[3]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 3:
                hangman_ascci = hangman[4]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 4:
                hangman_ascci = hangman[5]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
            elif intentos == 5:
                hangman_ascci = hangman[6]
                print(Fore.RED + Back.BLACK + Style.BRIGHT +hangman_ascci)
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"")
        # Colocar en minuscula la letra
        letra = input("Adivina la palabra, escribe una letra: ").lower()
        # Sí la letra, que solo puede ser una letra y si la letra es de tamaño = 1
        if letra.isalpha() and len(letra) == 1:
            # Válida de que no se descuenten intentos cuando coloca la misma letra
            # Para que cuando repita letras no descuente intentos
            if letra in letras_intentadas:
                # Mensaje de que la letra ya fue intentada
                print("Ya intentaste con esa letra, escribe otra")
            # Sí acierta la letra
            elif letra in palabra_secreta:
                # Se agrega a la lista de palabras adivinadas 
                letras_adivinadas.append(letra) 
                # Se agrega a la lista de palabras intentadas
                letras_intentadas.append(letra)
                # Imprimir de que adivinó la letra
                print("Muy bien!!!")
            # Sí no acierta
            else:
                # por cada vez que pierda, a los intentos se les suma 1
                intentos += 1
                # Agregar letras intentadas en la lista letra
                letras_intentadas.append(letra)
                # Imprimir mensaje de que no adivinó
                # Usamos format para que el número de la operación, vaya dentro de las '{}'
                print("Fallaste. Te quedan {} intentos.".format(intentos_maximos - intentos))
        # Vuelve y se repite el ciclo hasta que se ingrese una letra válido       
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa una letra válida.")
            # Tiempo de espera
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
        # Por cada iteración se va mostrando el tablero
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))
        # Sí el conjunto de letras adivinadas es igual al conjunto de palabra secreta, entonces encontró la palabra
        if set(letras_adivinadas) == set(palabra_secreta):
            # Mensaje de que ganó
            print("Felicidades, has adivinado la palabra!!!")
            # Tiempo de espera
            time.sleep(3)
            # Mensaje de "GANASTE" con generador de ascci
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
          _____          _   _           _____ _______ ______        ___  
         / ____|   /\   | \ | |   /\    / ____|__   __|  ____|    _ / _ \ 
        | |  __   /  \  |  \| |  /  \  | (___    | |  | |__     (_) | | |
        | | |_ | / /\ \ | . ` | / /\ \  \___ \   | |  |  __|      | | | |
        | |__| |/ ____ \| |\  |/ ____ \ ____) |  | |  | |____    _| |_| |
        \_____/_/    \_ \_| \_/_/    \_\_____/   |_|  |______|   (_)\___/ 
                                                                 
                                                                 """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            # Tiempo de espera
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
            # Vuelve al menu
            seleccionar_juego()
        # Sí es igual, no quedan más intentos, el jugador pierde
        if intentos == intentos_maximos:
            # Imprime el último hangman
            print(Fore.RED + Back.BLACK + Style.BRIGHT +"""
  /°°°\.
  |   |
|x x| |
 /|\  |
 / \  |
      |
=========""")
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +f"Has alcanzado el número máximo de intentos. La palabra era '{palabra_secreta}'")
            # Tiempo de espera
            time.sleep(3)
            # Mensaje de "PERDISTE" con generador de ascci
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
         _____  ______ _____  _____ _____  _____ _______ ______      __
        |  __ \|  ____|  __ \|  __ \_   _|/ ____|__   __|  ____|  _ / /
        | |__) | |__  | |__) | |  | || | | (___    | |  | |__    (_) | 
        |  ___/|  __| |  _  /| |  | || |  \___ \   | |  |  __|     | | 
        | |    | |____| | \ \| |__| || |_ ____) |  | |  | |____   _| | 
        |_|    |______|_|  \_\_____/_____|_____/   |_|  |______| (_) | 
                                                                    \_\.
                                                                             
                  """)
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/ 
 """)
            # Tiempo de espera
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
            # Vuelve al menu
            seleccionar_juego()         
# PALABRA AHORCADO        
def seleccionar_palabra():  # Función para seleccionar la palabra según el idioma
    # Mejorar presentación
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")   
    # Definir idioma como la función de seleccionar idioma
    idiomas = seleccionar_idioma_ahorcado()
    # Bucle infinito para que solo puedan ingresar valores válidos
    while True:
        # Sí seleccionó español
        if idiomas == 1:
            # Palabras en español, más de 330
            palabras = ['python', 'programación', 'inteligencia', 'fuente', 'vista', 'blanco', 'mejora'
                        , 'ir', 'alianza', 'entero', 'oír', 'creer', 'vestir', 'ética', 'enfrentar', 
                        'listar', 'esperanza', 'viaje', 'genial', 'protección', 'risa', 'brazo', 'ocupación',
                        'animal', 'sombra', 'amistad', 'valor', 'prueba', 'verde', 'placer', 'moral', 
                        'ropa', 'pintura', 'creencia', 'región', 'medio ambiente', 'éxito', 'interpretación',
                        'vivir', 'azul', 'información', 'innovación', 'comunicación', 'equipo', 'cuidado',
                        'salud', 'hoja', 'dinero', 'malo', 'distribución', 'medio', 'viejo', 'fuera', 
                        'danza', 'caliente', 'cine', 'paz', 'banco', 'sistema', 'existir', 'razón', 'hijo',
                        'número', 'roca', 'poder', 'amigo', 'guerra', 'alegría', 'enseñar', 'conexión', 
                        'transformación', 'representar', 'plazo', 'mejor', 'potencial', 'tratamiento', 
                        'verificar', 'riqueza', 'forma', 'voz', 'tipo', 'película', 'línea', 'negociación',
                        'opinión', 'ella misma', 'imagen', 'diversidad', 'capacidad', 'religión', 'justicia',
                        'aventura', 'naturaleza', 'pensamiento', 'interconexión', 'interdependencia', 
                        'conocimiento', 'ver', 'ciudadanía', 'comunidad', 'empleo', 'lejos', 'sentir', 
                        'ruido', 'padre', 'descubrimiento', 'valores', 'mente', 'lectura', 'significar',
                        'revolución', 'yo mismo', 'costo', 'alto', 'estrategia', 'proceso', 'contrato', 
                        'teatro', 'enorme', 'fuego', 'mayor', 'bebida', 'seguro', 'bienestar', 'democracia'
                        , 'ley', 'temprano', 'popular', 'guiar', 'confianza', 'decir', 'carácter', 'pobreza'
                        , 'relación', 'ancho', 'noticias', 'considerar', 'pelota', 'planeta', 'ocurrir', 'rojo'
                        , 'oeste', 'calle', 'caminar', 'pago', 'igualdad', 'cultura', 'posibilidad', 'ventana'
                        , 'consumo', 'vida', 'lanzar', 'filosofía', 'acuerdo', 'oportunidad', 'producir', 'esfuerzo'
                        , 'casa', 'luz', 'día', 'idioma', 'odio', 'decisión', 'también', 'cerrar', 'resiliencia'
                        , 'ciertamente', 'asiento', 'finanzas', 'ambiente', 'mano', 'aptitud', 'transporte', 
                        'conflicto', 'sangre', 'interés', 'noticia', 'exactamente', 'feliz', 'miedo', 'organización'
                        , 'nota', 'logro', 'investigación', 'dolor', 'fracaso', 'extrañar', 'en lugar de', 'esposa'
                        , 'arte', 'enseñanza', 'dejar caer', 'debería', 'oficio', 'nación', 'requerir', 'inicio', 
                        'todavía', 'situación', 'perro', 'estado', 'claro', 'dibujar', 'inversión', 'correr', 'creación'
                        , 'bajo', 'beneficio', 'vínculo', 'silencio', 'destrucción', 'desarrollo', 'sur', 'norma', 
                        'participación', 'general', 'agua', 'colaboración', 'compartir', 'política', 'llanto',
                        'escuchar', 'mundo', 'estación', 'crédito', 'curación', 'actuar', 'hablar', 'empleado', 
                        'evolución', 'ni', 'cargo', 'lenguaje', 'riesgo', 'segundo', 'ofrecer', 'gobernante', 
                        'precio', 'tecnología', 'aumento', 'canción', 'compra', 'venta', 'muerte', 'medicina', 
                        'color', 'progreso', 'legal', 'sueño', 'condición', 'trabajo', 'fuerte', 'unirse', 
                        'período', 'juego', 'presentar', 'hogar', 'adaptación', 'nunca', 'humanos', 'calor', 
                        'listo', 'respeto', 'avance', 'habilidad', 'sentido', 'dedicación', 'autoridad', 'probar',
                        'deuda', 'salto', 'efecto', 'prevención', 'aceptación', 'sonar', 'música', 'aprendizaje', 
                        'dirección', 'ciudad', 'gobierno', 'realidad', 'parecer', 'significado', 'palabra', 'vender',
                        'mercado', 'grupo', 'rápido', 'pintar', 'importar', 'causa', 'historia', 'aprender', 'joven', 
                        'fin', 'exploración', 'posición', 'cuerpo', 'tierra', 'país', 'registro', 'reclamar', 'tiempo',
                        'elemento', 'gato', 'cambio', 'intercambio', 'compromiso', 'positivo', 'globalización', 'destreza', 
                        'responder', 'servicio', 'acción', 'competencia', 'desafío', 'hotel', 'mensaje', 'defensa', 'fuerza',
                        'ahorro', 'estructura', 'economía', 'negocio', 'ocupar', 'tristeza', 'ejemplo', 'curso', 'edad', 'movimiento']
            # Retorna una palabra aleatoria de la lista
            return random.choice(palabras)
        # Sí seleccionó inglés
        elif idiomas == 2:
            # Palabras en inglés, más de 330
            palabras = ['range', 'search', 'success', 'scene', 'light', 'likely', 'for', 'child', 
                        'manager', 'charge', 'eye', 'government', 'evening', 'learn', 'blue', 'test', 
                        'easy', 'defense', 'national', 'window', 'end', 'disease', 'may', 'follow', 
                        'street', 'cold', 'new', 'word', 'possible', 'indeed', 'how', 'shoot', 
                        'especially', 'mind', 'reason', 'serve', 'describe', 'case', 'job', 'public', 
                        'arrive', 'next', 'mention', 'tax', 'over', 'process', 'bad', 'return', 'attack', 
                        'difference', 'clearly', 'stock', 'seem', 'join', 'eat', 'station', 'rise', 'arm', 
                        'think', 'certainly', 'girl', 'shake', 'paint', 'individual', 'effort', 'positive', 
                        'large', 'seek', 'discuss', 'son', 'deal', 'class', 'gun', 'position', 'raise', 'sell', 
                        'fund', 'ready', 'note', 'represent', 'drop', 'husband', 'safe', 'impact', 'woman', 
                        'enough', 'wish', 'man', 'experience', 'state', 'final', 'moment', 'low', 'entire', 
                        'out', 'why', 'either', 'throw', 'matter', 'private', 'hear', 'even', 'lose', 'prevent', 
                        'person', 'blood', 'tree', 'be', 'forget', 'across', 'although', 'opportunity', 'free', 
                        'pressure', 'rate', 'interest', 'suffer', 'share', 'film', 'box', 'early', 'election', 'mark', 
                        'short', 'outside', 'fight', 'message', 'score', 'teach', 'who', 'effect', 'west', 
                        'once', 'ability', 'town', 'down', 'few', 'today', 'society', 'miss', 'she', 'away', 
                        'second', 'exist', 'image', 'order', 'cover', 'character', 'able', 'address', 'sound', 
                        'course', 'believe', 'study', 'prove', 'should', 'worry', 'relate', 'movie', 'half', 
                        'season', 'training', 'role', 'mother', 'hair', 'including', 'option', 'news', 'relationship', 
                        'buy', 'player', 'report', 'boy', 'country', 'introduce', 'little', 'watch', 'focus', 
                        'fire', 'service', 'most', 'trade', 'do', 'shoulder', 'never', 'certain', 'exactly', 'number', 
                        'tell', 'education', 'at', 'party', 'hit', 'health', 'far', 'avoid', 'increase', 'general', 
                        'credit', 'family', 'major', 'myself', 'law', 'keep', 'say', 'leave', 'site', 'benefit', 'cost', 
                        'contain', 'eight', 'suggest', 'book', 'require', 'sign', 'environment', 'some', 'opinion', 
                        'economy', 'drive', 'produce', 'dream', 'south', 'size', 'live', 'single', 'investment', 
                        'choose', 'project', 'move', 'court', 'situation', 'hot', 'rule', 'shot', 'check', 'red', 
                        'item', 'herself', 'crime', 'source', 'forward', 'operation', 'start', 'particular', 'lawyer', 
                        'people', 'ground', 'offer', 'wear', 'consider', 'fly', 'improve', 'example', 'spring', 'it', 
                        'rock', 'amount', 'thus', 'own', 'fact', 'region', 'of', 'beautiful', 'choice', 'introduction', 
                        'special', 'plan', 'interview', 'claim', 'also', 'save', 'phone', 'pull', 'beat', 'information', 
                        'big', 'seat', 'culture', 'occur', 'strategy', 'degree', 'laugh', 'mean', 'main', 'legal', 'ball', 
                        'idea', 'instead', 'voice', 'close', 'list', 'act', 'answer', 'great', 'discover', 'part', 'build', 
                        'political', 'develop', 'dog', 'receive', 'talk', 'weight', 'sure', 'travel', 'quickly', 'body', 
                        'will', 'inside', 'stay', 'go', 'clear', 'could', 'condition', 'industry', 'employee', 'doubt', 
                        'concern', 'decide', 'front', 'ever', 'huge', 'record', 'brother', 'yet', 'sometimes', 'here', 
                        'wife', 'responsibility', 'road', 'bill', 'period', 'friend']
            return random.choice(palabras)
            # Retorna una palabra aleatoria de la lista   
        # Sí seleccionó francés     
        elif idiomas == 3:
            # Palabras en francés, más de 330
            palabras = ['cheveux', 'balle', 'entrevue', 'condition', 'option', 'posseder', 'film', 'parti', 'regarder', 
                        'mari', 'souffrir', 'signifier', 'mot', 'pourrait', 'situation', 'maladie', 'esprit', 'porter', 
                        'effort', 'ceil', 'avant', 'crédit', 'faire', 'santé', 'scene', 'a', 'fin', 'etre', 'position', 
                        'réponse', 'empêcher', 'election', 'stratégie', 'poids', 'raison', 'boite', 'taux', 'opportunite', 
                        'contenir', 'audessus', 'enseigner', 'politique', 'entier', 'général', 'opération', 'gros', 'chaud', 
                        'vendre', 'facile', 'succes', 'suivre', 'individu', 'principal', 'arriver', 'téléphone', 'huit', 
                        'personnage', 'retour', 'sige', 'manquer', 'homme', 'site', 'voyage', 'exiger', 'comment', 'assez', 
                        'exemple', 'personne', 'soit', 'mere', 'service', 'il', 'arbre', 'montant', 'clairement', 'decrire', 
                        'choisir', 'plan', 'projet', 'partie', 'pret', 'expérience', 'relation', 'employé', 'légal', 'recevoir', 
                        'partager', 'épaule', 'au lieu', 'pression', 'chien', 'moitié', 'tirer', 'recherche', 'surtout', 
                        'société', 'responsabilité', 'capacité', 'défense', 'perdre', 'énorme', 'augmenter', 'femme', 'possible', 
                        'image', 'formation', 'décider', 'deuxieme', 'garder', 'source', 'nombre', 'unefois', 'facture', 'corps', 
                        'agir', 'pistolet', 'éviter', 'ami', 'avis', 'froid', 'jeter', 'rester', 'différence', 'loin', 'suivant', 
                        'loi', 'rocher', 'fenetre', 'économie', 'devrait', 'fait', 'découvrir', 'positif', 'relater', 'fils', 'test', 
                        'capable', 'enregistrement', 'tribunal', 'grand', 'commerce', 'fille', 'acheter', 'vivre', 'construire', 'nouveau', 
                        'bras', 'final', 'élever', 'adresse', 'voix', 'de', 'manger', 'parler', 'améliorer', 'aller', 'ainsi', 'plus', 
                        'pour', 'considérer', 'oublier', 'apprendre', 'rue', 'responsable', 'vérifier', 'matiere', 'état', 'qui', 
                        'discuter', 'volonté', 'score', 'feu', 'y compris', 'région', 'portee', 'ellememe', 'libre', 'fonds', 
                        'pourquoi', 'elle', 'sur', 'laissertomber', 'impact', 'frere', 'conduire', 'ici', 'avantage', 'stock', 
                        'taille', 'sembler', 'noter', 'suggérer', 'joindre', 'soirée', 'sang', 'investissement', 'ville', 'déménager', 
                        'souhaiter', 'printemps', 'crime', 'prouver', 'sud', 'intéret', 'certainement', 'aussi', 'éducation', 
                        'certain', 'exister', 'sol', 'introduire', 'signer', 'fermer', 'classe', 'dehors', 'joueur', 'unique', 
                        'livre', 'introduction', 'encore', 'famille', 'meme', 'station', 'bas', 'transaction', 'jamais', 'saison', 
                        'peindre', 'cout', 'role', 'marquer', 'élévation', 'chercher', 'rever', 'information', 'environnement', 
                        'étude', 'exactement', 'choix', 'pays', 'frapper', 'période', 'développer', 'privé', 'impot', 'route', 
                        'nouvelles', 'particulier', 'servir', 'processus', 'croire', 'certains', 'représenter', 'lumiere', 'effet', 
                        'dire', 'culture', 'cours', 'rapidement', 'ouest', 'penser', 'garçon', 'combat', 'partir', 'peu', 'enfant', 
                        'produire', 'en effet', 'cas', 'descendre', 'devant', 'attaque', 'national', 'degré', 'préoccupation', 
                        'travail', 'gens', 'liste', 'se produire', 'message', 'majeur', 'secouer', 'idée', 'à travers', 'offrir', 
                        'tir', 'gouvernement', 'sauver', 'entendre', 'bleu', 'avocat', 'rouge', 'peut', 'parfois', 'article', 
                        'son', 'spécial', 'tot', 'revendication', 'beau', 'moment', 'industrie', 'couverture', 'battre', 'rire', 
                        'doute', 'rapport', 'mentionner', 'public', 'extérieur', 'moimeme', 'charger', 'mauvais', 'probable', 
                        'commencer', 'court', 'voler', 'regle', 'clair', 'commande', 'crapoter', 'ledouleurexquisite','dejaVu', 'bof', 
                        'chanterenyaourt', 'depaysement', 'flaner', 'raler', 'voila', 'chez']
            return random.choice(palabras)
            # Retorna una palabra aleatoria de la lista
        # Vuelve y se repite el ciclo hasta que se ingrese un número valido
        else: 
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.")
# IDIOMA AHORCADO
def seleccionar_idioma_ahorcado(): # Función para que el jugador seleccione el idioma de las palabras del juego del Ahorcado
    # Inicialización de la variable para almacenar la elección del idioma
    idioma = 0
    # Limpiar consola
    os.system("cls")
    # Tiempo de espera
    time.sleep(0.2)
    # Impresión de mensaje de bienvenida
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
.  _   ___ ___ ___ _  ___   _____ _  _ ___ ___   ___      _   _                              .
. (_) | _ )_ _| __| \| \ \ / / __| \| |_ _|   \ / _ \    /_\ | |                             .
. | | | _ \| || _|| .` |\ V /| _|| .` || || |) | (_) |  / _ \| |__                           .
. |_| |___/___|___|_|\_| \_/ |___|_|\_|___|___/ \___/  /_/ \_\____|                          .
.     _ _   _ ___ ___  ___    ___  ___ _        _   _  _  ___  ___  ___   _   ___   ___    _ .
.  _ | | | | | __/ __|/ _ \  |   \| __| |      /_\ | || |/ _ \| _ \/ __| /_\ |   \ / _ \  | |.
. | || | |_| | _| (_ | (_) | | |) | _|| |__   / _ \| __ | (_) |   / (__ / _ \| |) | (_) | |_|.
.  \__/ \___/|___\___|\___/  |___/|___|____| /_/ \_\_||_|\___/|_|_|\___/_/ \_\___/ \___/  (_).
.                                                                                            .""")
    # Tiempo de espera
    time.sleep(3)
    # Limpiar la consola
    os.system("cls")
    # Espaciado
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"")
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"")
    os.system("cls")
    # Bucle infinito 
    while True:
        # Se imprimen las opciones
        print("Selecciona en qué idioma quieres las palabras del Ahorcado")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"1. Español")
        print("2. Inglés")
        print("3. Francés")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")
        # Entrada del jugador para seleccionar el idioma
        seleccionar_idioma = input("Escriba el número correspondiente al idioma que desee; las palabras secretas del ahorcado serán en el idioma elegido: ")
        # Asignación del idioma según la elección del jugador
        # Sí es igual a 1
        if seleccionar_idioma == '1':
            idioma = 1
            break
        # Sí es igual a 2
        elif seleccionar_idioma == '2':
            idioma = 2
            break
        # Sí es igual a 3
        elif seleccionar_idioma == '3':
            idioma = 3
            break
        # Mensaje de error en caso de que se ingrese un número inválido
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido('1','2','3','4').")
            # Tiempo de espera
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
    # Retorno del idioma seleccionado
    return idioma
# PALABRA OCULTA
def mostrar_tablero(palabra, letras_adivinadas): # Función para mostrar el tablero 
    # Espaciado
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    # Resultado = cadena vacía
    resultado = ""
    # Iteración a través de cada letra de la palabra
    for letra in palabra:
        # Sí la letra está en las letras adivinadas
        if letra in letras_adivinadas:
            # El resultado es igual a la letra, se cambio el guión bajo por la letra
            resultado += letra + " "
        # Sí no
        else:
            # El resultado es un guión bajo
            resultado += "_ "
    # Retornar resultado con función strip  
    # Eliminación de espacios adicionales al inicio y al final del resultado con la función strip
    return resultado.strip()
# DIFICULTAD AHORCADO     
def dificultad_ahorcado(): # Función para seleccionar la dificultad del juego del Ahorcado y determinar la cantidad de intentos
    # Espaciado
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    # Vidas del jugador empiece en 0
    vidas_jugador_ahorcado = 0
    # Bucle infinito para que el jugador seleccione el nivel de dificultad
    while True:
        # Imprimir las opciones
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"")
        print("Selecciona el nivel de dificultad del Ahorcado")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")
        # Pedir al jugador para seleccionar la dificultad
        seleccionar_dificultad = input("Escriba el número correspondiente de la dificultad que desee; esto definirá los intentos que tendrá (1 = 7 intentos, 2 = 6 intentos, 3 = 5 intentos): ")
        # Asignación de la cantidad de intentos según la dificultad seleccionada
        # Sí selecciona 1 las vidas son 7
        if seleccionar_dificultad == '1':
            vidas_jugador_ahorcado = 7
            # Rompe el ciclo para retornar
            break
        # Sí selecciona 2 las vidas son 6
        elif seleccionar_dificultad == '2':
            vidas_jugador_ahorcado = 6
            # Rompe el ciclo para retornar
            break
        # Sí selecciona 3 las vidas son 5
        elif seleccionar_dificultad == '3':
            vidas_jugador_ahorcado = 5
            # Rompe el ciclo para retornar
            break
        # Vuelve y se repite el ciclo hasta que se ingrese un número valido
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.('1','2','3')")
            # Tiempo de espera
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
    # Retornar la cantidad de vidas
    return vidas_jugador_ahorcado
# SOPA DE LETRAS INICIO
def inicio_juego_sopa_de_letras(): # Función para iniciar el juego
    # Limpiar
    os.system("cls")
    # Imprimir mensaje de bienvenida
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + """
.  _   ___ ___ ___ _  ___   _____ _  _ ___ ___   ___      _   _     .
. (_) | _ )_ _| __| \| \ \ / / __| \| |_ _|   \ / _ \    /_\ | |    .
. | | | _ \| || _|| .` |\ V /| _|| .` || || |) | (_) |  / _ \| |__  .
. |_| |___/___|___|_|\_| \_/ |___|_|\_|___|___/ \___/  /_/ \_\____| .
.     _ _   _ ___ ___  ___        ___  ___       ___  ___  ___  _   .
.  _ | | | | | __/ __|/ _ \      |   \| __|     / __|/ _ \| _ \/_\  .
. | || | |_| | _| (_ | (_) |     | |) | _|      \__ \ (_) |  _/ _ \ .
.  \__/ \___/|___\___|\___/      |___/|___|     |___/\___/|_|/_/ \_\.
.          ___  ___   _    ___ _____ ___    _   ___   _             .
.         |   \| __| | |  | __|_   _| _ \  /_\ / __| | |            .
.         | |) | _|  | |__| _|  | | |   / / _ \|__ \ |_|            .
.         |___/|___| |____|___| |_| |_|_\/_/ \_\___/ (_)            .
.                                                                   .""")
    # Tiempo de espera
    time.sleep(3)
    # Limpiar la consola
    os.system("cls")
    # Definir variable con todas las letras del abecedario en una lista
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Limpiar la consola
    os.system("cls")
    # Para que el usuario ingrese las dimensiones de la matriz
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"DIMENSIONES")
    print(Fore.RED + Back.BLACK + Style.BRIGHT +"")
    N = int(input("Ingrese la dimensión de la matriz (Un numero que N tal que 10 <= N <= 30, ejemplo para matriz 10x10: '10'): "))
    print(Fore.RED + Back.BLACK + Style.BRIGHT +"")
    # Llamar función con los argumentos de N y abecedario
    juego_sopa_de_letras(N, abecedario)
# SOPA DE LETRAS 
def juego_sopa_de_letras(N, abecedario): # Función para la sopa de letras
    # Sí se cumple la condición
    if 10 <= N <= 30:
        # Iniciar lista vacía de palabras
        palabras = []
        # Pedir el número de palabras
        cuantas_palabras = int(input("¿Cuantas palabras desea ingresar? (ingrese un numero entero): "))
        # Iterar en el rango de la cantidad de palabras
        for i in range(cuantas_palabras): # Ingreso las palabras en una lista para luego acceder a estas 
            # Para pedir las palabras
            print(Fore.RED+ Back.BLACK + Style.BRIGHT + "")
            palabra = input("Ingrese la palabra: ")
            # Añadir a la lista vacía de palabras
            palabras.append(palabra)
        # Función pa generar el cursor aleatorio con posición y dirección
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "")
        def generar_cursor(dimension):# Se genera el cursor que es como un puntero que decide aleatoriamente donde va a ser la posicion inicial y luego la dirección 
            # Para la fila
            fila = random.randint(0, dimension - 1)
            # Para la columna
            columna = random.randint(0, dimension - 1)
            # Esto definirá la dirección, al formar una selección aleatoria de vectores 
            # Fila, eje x
            avanX = random.choice([-1, 0, 1]) 
            # Columna, eje y
            avanY = random.choice([-1, 0, 1])
            # Sí la opción aleatoria son dos ceros entonces 
            if avanX == 0 and avanY == 0:
                # Para que sea horizontal
                avanX = 1
            # Retorna fila, columna, y los avances en x e y
            return fila, columna, avanX, avanY
        # Función pa verificar si una palabra cabe en la matriz desde una posición y dirección dadas
        def palabra_cabe(ajiaco, palabra, cursor):
            # Indican la posicion inicial y la direccion en la que se intentará colocar 
            x, y, avanX, avanY = cursor 
            # Iterar la cantidad de letras de la palabra
            for letra in palabra:
                # Verificar si la posición está dentro de la matriz
                # Que si se pueda colocar en las dimensiones de la sopa de letras
                if not (0 <= x < len(ajiaco) and 0 <= y < len(ajiaco[0])):
                    # Sí no se cumple, retorna falso
                    return False
                # En cada uno se va a actualizar la posicion x ^ y segun la direccion dada por avanX ^ avanY
                x += avanX 
                y += avanY
            # Retornar verdadero cuando se cumpla
            return True  
        # Función pa colocar una palabra en la matriz a partir de una posición y dirección dadas
        # Cursor será algo como un puntero que selecciona aleatoriamente cual será la posicion inicial de la palabra
        def colocar_palabra(ajiaco, palabra, cursor): # Recibirá los argumentos de ajiaco, palabra y cursor
            x, y, avanX, avanY = cursor
            # Iterar la cantidad de letras de la palabra
            for letra in palabra:
                # Verificar si la posición está dentro de la matriz
                # Si x ^ y tan en el rango del tamaño de la fila y columna 
                if 0 <= x < len(ajiaco) and 0 <= y < len(ajiaco[0]): 
                    ajiaco[x][y] = letra
                    # Le suma cada x que avance
                    x += avanX 
                    # Le suma cada y que avance
                    y += avanY 
                # Sí no
                else:
                    # Romper ciclo
                    break
            # Retornar ajiaco
            return ajiaco
        # Función para generar la matriz final con palabras colocadas aleatoriamente
        def generar_matriz_palabras(palabras, dimension):
            # Se llenará de espacios vacíos la sopa para luego acceder a esos espacios llenando con palabras y después con letras
            ajiaco = [[' '] * dimension for _ in range(dimension)] 
            # Iterar la cantidad de palabras
            for palabra in palabras:
                # Intentar colocar la palabra hasta encontrar un espacio válido
                while True:  # Utilizo una bandera
                    # Variable cursor es igual a la función de generar_cursor
                    cursor = generar_cursor(dimension)
                    # Intenta hasta que se pueda poner la palabra 
                    if palabra_cabe(ajiaco, palabra, cursor): 
                        ajiaco = colocar_palabra(ajiaco, palabra, cursor)
                        # Romper ciclo
                        break
            # Retorna ajiaco que es la matriz o sopa 
            return ajiaco 
        # Función para imprimir la matriz mejor
        def imprimir_matriz(ajiaco):  # Para poner coordenadas
            # Para colocar las coordenadas de las columnas, en caso de que sea más de 9, otra vez comenzará desde 0    
            # Regla es la variable que determinará el numero de las colummnas , la cantidad de repeticiones se determina dividiendo todo sobre 10 + 1 para asegurar que hayan siempre numeros suficientes sobre las columanas                                                             
            # Tomando la parte que es el doble de la longitud de la matriz para cubrir bien las columnas
            regla = f"   {('0 1 2 3 4 5 6 7 8 9 ' * int(len(ajiaco) / 10 + 1))[:len(ajiaco) * 2]}\n" 
            # Igualar variables
            linea = regla                                                                            
            # En este caso se hizo con enumerate, apra que las coordenadas en las filas sí llegar a ser más de 9, que si se use 10, 11...
            for i, fila in enumerate(ajiaco): 
                # Se pretende imprimir el numero de fila con al menos dos digitos para mantener la alineacion y se une las letras de la fila con un espacio entre ellas  
                linea += f"{i:2d} {' '.join(fila)}\n" 
            # Imprimir la linea + regla
            print(linea + regla)
        # Función para rellenar la sopa
        def rellenar_sopa (ajiaco):  # Por cada espacio que encuentre vacio en la matriz que ya tiene ingresada las palabras, ponga una letra aleatoria
            for x in range(len(ajiaco)):
                for y in range(len(ajiaco)):
                    # Para el espaciado
                    if ajiaco[x][y] ==" ":
                        # Se usa numpy para colocar en la matriz las letras aletoriamente
                        ajiaco[x][y] = np.random.choice(abecedario)
        # Generar la matriz final y mostrarla
        matriz_resultante = generar_matriz_palabras(palabras, N)
        # Llamar función de rellenar_sopa
        rellenar_sopa(matriz_resultante)
        # Llamar función de imprimir_matriz
        imprimir_matriz(matriz_resultante)
        # Hacer que el usuario encuentre palabras hasta que todas sean encontradas
        # Se utiliza un conjunto para la eliminación de las palabras restantes
        palabras_restantes = set(palabras.copy())  
        # Función para encontrar palabras en la sopa
        def encontrar_palabra(ajiaco, inicio, fin):
            # Imprimir la coordenada de inicio y fin
            print(f"Inicio: {inicio}, Fin: {fin}")
            # Aqui, si la palabra está en la misma fila, se utiliza slicing pa extraer la palabra  
            if inicio[0] == fin[0]: 
                palabra_encontrada = ''.join(ajiaco[inicio[0]][min(inicio[1], fin[1]):max(inicio[1], fin[1]) + 1])
            # Si las coordenadas pertencen a la misma columna, utilizo una comprensión de lista para obtener las letras de la palabra correspondiente en las filas min y max
            elif inicio[1] == fin[1]:   
                palabra_encontrada = ''.join(ajiaco[i][inicio[1]] for i in range(min(inicio[0], fin[0]), max(inicio[0], fin[0]) + 1))
            # De no ser como lo anterior, es una coordenada diagonal donde utilizo la finción zip para extraer las letras de la sopa desde la posicion inicio y fin y luego las concatena para formar la palabra   
            else:
                palabra_encontrada = ''.join(ajiaco[i][j] for i, j in zip(range(inicio[0], fin[0] + 1), range(inicio[1], fin[1] + 1)))
            # Imprimir mensaje con la palabra encontrada
            print(Fore.WHITE+ Back.BLACK + Style.BRIGHT + "")
            print(f"Palabra encontrada: {palabra_encontrada}")
            print(Fore.CYAN+ Back.BLACK + Style.BRIGHT + "")
            # Retornar la palabra encontrada
            return palabra_encontrada
        # Mientras palabras restantes
        while palabras_restantes:
            # Obtener coordenadas del usuario
            # Se usa split para separar las coordenadas 
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "")
            inicio = input("Ingrese la coordenada inicial ('fila' 'columna')(separando por un espacio la fila de la columna  ¡Siga la especificación por favor!): ").split() #Por cada palabra ingresada por el usuario, la descomopne en letras usando split
            # Se usa split para separar las coordenadas 
            fin = input("Ingrese la coordenada final ('fila' 'columna')(separando por un espacio la fila de la columna  ¡Siga la especificación por favor!): ").split()
            # Convertir las coordenadas a números enteros
            # Convierte las cordenadas porporcionadas a numeros enteros y luego vuelve a almacenarlos en la variable inicio y fin 
            # Utilizo la funcion map(int) para realizar comparaciones numericas y acceder elementos en la matriz
            inicio = tuple(map(int, inicio))   
            # Utilizo la funcion map(int) para realizar comparaciones numericas y acceder elementos en la matriz
            fin = tuple(map(int, fin))  
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
                    # Imprimir que encontró la palabra
                    print(f"¡Encontraste la palabra '{palabra_encontrada}'!")
                    # Mostrar las palabras restantes
                    print(Fore.RED+ Back.BLACK + Style.BRIGHT + "")
                    print(f"Palabras restantes: {', '.join(palabras_restantes)}")
                else:
                    # Mensaje de invalidación
                    print("No es una palabra válida. Inténtelo de nuevo.")
            else:
                # Mensaje de que se debe formar una línea recta
                print("Las coordenadas deben formar una línea recta. Inténtelo de nuevo.")
                # Esperar
                time.sleep(3)
                inicio_juego_sopa_de_letras()
        # Mensaje de felicitaciones al encontrar todas las palabras
        print(Fore.YELLOW+ Back.BLACK + Style.BRIGHT + " ")
        print(Fore.YELLOW+ Back.BLACK + Style.BRIGHT + "¡Felicidades! ¡Has encontrado todas las palabras!")
        time.sleep(3.5)
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +"""
          _____          _   _           _____ _______ ______        ___  
         / ____|   /\   | \ | |   /\    / ____|__   __|  ____|    _ / _ \ 
        | |  __   /  \  |  \| |  /  \  | (___    | |  | |__     (_) | | |
        | | |_ | / /\ \ | . ` | / /\ \  \___ \   | |  |  __|      | | | |
        | |__| |/ ____ \| |\  |/ ____ \ ____) |  | |  | |____    _| |_| |
        \_____/_/    \_ \_| \_/_/    \_\_____/   |_|  |______|   (_)\___/ 
                                                                 
                                                                 """)
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
    __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
   / // // // // // // // // // // // // // // // // // // // // // // // /
  / // // // // // // // // // // // // // // // // // // // // // // // / 
 /_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_/  
                                                                           
                  """)
        # Tiempo de espera
        time.sleep(3)
        # Limpiar consola
        os.system("cls")
        # Ir al menú
        seleccionar_juego()

        
    else:
        # Mensaje de invalidación
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "Fue advertido de que el numero debía estar entre 10 y 30, vuelva a iniciar el juego si lo desea")
        # Esperar 
        time.sleep(2)
        # limpiar consola
        os.system("cls")
        # Ir a menú
        seleccionar_juego()
# SALIR
def salir(): # Función para salir del programa
    # Imprimir con colorama y un generador de ascci, un mensaje de GRACIAS POR JUGAR!!!
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    # Limpiar consola
    os.system("cls")
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT +"""
 ___________  ___  _____ _____ ___  _____  ______ ___________     ___ _   _ _____  ___ ______ _   _   _  
|  __ \ ___ \/ _ \/  __ \_   _/ _ \/  ___| | ___ \  _  | ___ \   |_  | | | |  __ \/ _ \| ___ \ | | | | | 
| |  \/ |_/ / /_\ \ /  \/ | |/ /_\ \ `--.  | |_/ / | | | |_/ /     | | | | | |  \/ /_\ \ |_/ / | | | | | 
| | __|    /|  _  | |     | ||  _  |`--. \ |  __/| | | |    /      | | | | | | __|  _  |    /| | | | | | 
| |_\ \ |\ \| | | | \__/\_| || | | /\__/ / | |   \ \_/ / |\ \  /\__/ / |_| | |_\ \ | | | |\ \|_| |_| |_| 
 \____|_| \_\_| |_/\____/\___|_| |_|____/  \_|    \___/\_| \_| \____/ \___/ \____|_| |_|_| \_(_) (_) (_) 
                                                                                                         
                                                                                                         """)
    print("""                    For: NICOLAS ESTUPIÑAN and SANTIAGO AVENDAÑO                                         
                                                                                                         """)
    # Función para salir
    exit() 
# MENÚ
def seleccionar_juego(): # Bucle para que el jugador solo pueda introducir los valores 1, 2 y 3 para seleccionar el juego o 4 para salir 
    while True:
        # Imprimir un menu grande, con colorama y generador de ascci
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT + """
                             __  __  ___  _  _  _   _  
                            |  \/  || __|| \| || | | | 
                            | |\/| || _| | .` || |_| | 
                            |_|  |_||___||_|\_| \___/  
                                                       """)
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "")

        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "SELECCIONA EL JUEGO  QUE QUIERAS JUGAR ")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "")
        # Se muestran las opciones de juego, o la opción salir
        print("1. Piedra, Papel o Tijera        ")
        print("2. Ahorcado                      ")
        print("3. Sopa de Letras                ")
        print("4. Salir                         ")
        print(Fore.RED + Back.BLACK + Style.BRIGHT +"")
        # Se pide al jugador que acción quiere hacer mediante el ingreso del número
        eleccion = input("Ingresa el número correspondiente al juego que deseas jugar o si quieres salir (1, 2, 3, 4): ")
        # Dependiendo la opción que elija, lo enviará a la función respectiva, ya sea de cada juego, o salirse.
        if eleccion == '1':
            juego_piedra_papel_o_tijera()
            break
        elif eleccion == '2':
            juego_ahorcado()
            break
        elif eleccion == '3':
            inicio_juego_sopa_de_letras()
            break
        elif eleccion == '4':
            salir()
            break
        # Vuelve y se repite el ciclo hasta que se ingrese un número valido
        else:
            # Imprime mensaje 
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido ('1','2','3','4').")
            # Tiempo de espera
            time.sleep(2)
            # Limpiar consola
            os.system("cls")
# COMENZAR JUEGO
def comenzar_juego(): # Función para dar comienzo al juego
    # Limpiar consola
    os.system("cls")
    # Imprimir INDUSPLAYTHON con los respectivos colores usando colorama
    print (Fore.GREEN + Back.BLACK + Style.BRIGHT + """
    . _____ _   _______ _   _ ___________ _      _____   _______ _   _ _____ _   _ .    
    .|_   _| \ | |  _  \ | | /  ___| ___ \ |    / _ \ \ / /_   _| | | |  _  | \ | |.    
    .  | | |  \| | | | | | | \ `--.| |_/ / |   / /_\ \ V /  | | | |_| | | | |  \| |.    
    .  | | | . ` | | | | | | |`--. \  __/| |   |  _  |\ /   | | |  _  | | | | . ` |.    
    . _| |_| |\  | |/ /| |_| /\__/ / |   | |___| | | || |   | | | | | \ \_/ / |\  |.    
    . \___/\_| \_/___/  \___/\____/\_|   \_____|_| |_/\_/   \_/ \_| |_/\___/\_| \_/.    
                                                                                        
                                                                                        """)
    # Elaborado por
    print("                For: NICOLAS ESTUPIÑAN and SANTIAGO AVENDAÑO                            ")
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
    # Tiempo de espera
    time.sleep(5)   
    # Limpiar consola
    os.system("cls")
    # Llamar la función seleccionar juego para seleccionar el juego desde el menu.
    seleccionar_juego() 
# INICIO
if __name__ == "__main__":
    # Comienza el programa llamando a la función de comenzar el juego
    comenzar_juego()
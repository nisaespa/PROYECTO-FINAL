import random # Importar random, para valores aleatorios
from colorama import init, Back, Fore, Style # Importar de colorama init, back, fore y style para los colores de letra, de fondo y el estilo.
import time # Para controlar los tiempos entre las acciones
import os # Para limpiar la consola
import numpy as np # Probando con numpy, para la sopa de letras

# El programa trata de un salón o menú de tres juegos básicos de python: AHORCADO, SOPA DE LETRAS Y PIEDRA PAPEL O TIJERA. Con interacción con la consola.

# CANTIDAD DE JUGADORES PIEDRA PAPEL O TIJERA
def juego_piedra_papel_o_tijera():  # Función para seleccionar cantidad de jugadores.
    # Impresión de un mensaje de bienvenida con formato y colores
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "     ")
    print("¡¡BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA!!")
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "     ")
    # Bucle infinito para permitir al jugador elegir la cantidad de jugadores
    while True:
        # Mensaje para que el jugador elija la cantidad de jugadores
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "ELIJE LA CANTIDAD DE JUGADORES")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "1. Un jugador")
        print("2. Dos jugadores")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")

        # Solicitar al jugador para la cantidad de jugadores
        jugadores = input("Ingresa la cantidad de jugadores: ")

        # Verificar la elección del jugador y llamar a la función correspondiente
        if jugadores == '1':
            juego_piedra_papel_o_tijera_un_jugador()  # Llamar a la función para un jugador
            break
        elif jugadores == '2':
            juego_piedra_papel_o_tijera_dos_jugadores()  # Llamar a la función para dos jugadores
            break
        else:
            print("Por favor, ingresa un número válido.")  # Mensaje de error si la entrada no es válida

# DIFICULTAD MODO UN JUGADOR
def dificultad_un_jugador():
    # Impresión de espacios en blanco para mejorar la presentación
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    
    vidas_jugador = 0  # Inicialización de la variable que almacenará las vidas del jugador

    # Bucle infinito para que el jugador seleccione la dificultad
    while True:
        # Mensaje para que el jugador elija el nivel de dificultad
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "SELECCIONA EL NIVEL DE DIFICULTAD")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print(Fore.RED + Back.BLACK + Style.BRIGHT +"")

        # Solicitar al jugador para la selección de dificultad
        seleccionar_dificultad_un_jugador = input("Escriba el número correspondiente a la dificultad que\ndesee contra la computadora, esto definirá las vidas \nque tendrá (1 = 3 vidas, 2 = 2 vidas, 3 = 1 vida): ")

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
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.")

    return vidas_jugador  # Devolver el número de vidas seleccionado por el jugador

# UN JUGADOR PIEDRA PAPEL O TIJERA
def juego_piedra_papel_o_tijera_un_jugador():
    # Impresión de espacios en blanco para mejorar la presentación
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    
    vidas_computadora = 3  # Inicialización de las vidas de la computadora
    rondas = 1  # Inicialización del contador de rondas
    vidas_jugador = dificultad_un_jugador()  # Obtener la cantidad de vidas del jugador mediante la función dificultad_un_jugador()

    # Bucle principal del juego
    while True:
        # Impresión de la presentación del juego en cada ronda
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + f'       RONDAS!!!: {rondas}')
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'')

        # Impresión de las vidas de la computadora
        if vidas_computadora == 3:   
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas de la computadora: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤')
        elif vidas_computadora == 2:
            print('Vidas de la computadora: ' + Fore.RED + Back.BLACK + Style.BRIGHT + ' ❤ ❤')
        elif vidas_computadora == 1:
            print('Vidas de la computadora: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤') 
        
        # Impresión de las vidas del jugador
        if vidas_jugador == 3:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤')
        elif vidas_jugador == 2:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤')
        elif vidas_jugador == 1:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador: ' + Fore.RED + Back.BLACK + Style.BRIGHT +' ❤') 
        
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

# SELECCIÓN DE OPCIONES 
def seleccionar_opciones_uno(): 
    # Impresión de espacios en blanco para mejorar la presentación
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
            return opcion_del_jugador, opcion_del_computador

# REGLAS UN JUGADOR
def reglas_piedra_papel_o_tijera_un_jugador(opcion_del_jugador, opcion_del_computador, vidas_jugador, vidas_computadora):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ") 
    # Sí son la misma opción, entonces es empate
    if opcion_del_jugador == opcion_del_computador:
        # Se generaran mensajes con ayuda de un generador de ascci para cuando el jugador o el computador ganen, o sea empate
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         EMPATE')
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
    # Opciones para que el jugador gane
    elif opcion_del_jugador == 'piedra':
        if opcion_del_computador == 'tijera':
            print('piedra gana a tijera')
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
            print('papel gana a piedra')
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
    elif opcion_del_jugador == 'papel':
        if opcion_del_computador == 'piedra':
            print('papel gana a piedra')
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
            print('tijera gana a papel')
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
            print('tijera gana a papel')
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
            print('piedra gana a tijera')
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
    return vidas_jugador, vidas_computadora

# DOS JUGADORES 

def juego_piedra_papel_o_tijera_dos_jugadores():
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    vidas_jugador_1 = 3
    vidas_jugador_2 = 3
    rondas = 1
    while True:
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT + f'       RONDAS!!!: {rondas}')
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"")
        if vidas_jugador_1 == 3:
            print('Vidas del jugador 1: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤')
        elif vidas_jugador_1 == 2:
            print('Vidas del jugador 1: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤')
        elif vidas_jugador_1 == 1:
            print('Vidas del jugador 1: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ')
        if vidas_jugador_2 == 3:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador 2: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤ ❤')
        elif vidas_jugador_2 == 2:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador 2: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ❤')
        elif vidas_jugador_2 == 1:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT +'Vidas del jugador 2: '+Fore.RED + Back.BLACK + Style.BRIGHT +' ❤ ')

        opcion_jugador_1 = seleccionar_opciones_dos(1)
        opcion_jugador_2 = seleccionar_opciones_dos(2)
        vidas_jugador_1, vidas_jugador_2 = reglas2(opcion_jugador_1, opcion_jugador_2, vidas_jugador_1, vidas_jugador_2)
        rondas += 1
        
        if vidas_jugador_1 == 0: # gana jugador 2
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
            time.sleep(3)
            # Limpiar consola
            os.system("cls")
            seleccionar_juego()
        if vidas_jugador_2 == 0: # gana jugador 1
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
            seleccionar_juego()    
def seleccionar_opciones_dos(jugador):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    opciones = ('piedra', 'papel', 'tijera')
    while True:
        print(Fore.RED + Back.BLACK + Style.BRIGHT +"")
        opcion_jugador = input(f'Elige entre piedra, papel o tijera jugador {jugador}: ')
        opcion_jugador = opcion_jugador.lower()
        if opcion_jugador in opciones:
            return opcion_jugador
        # Vuelve y se repite el ciclo hasta que se ingrese validamente
        else:
            print('Opción no válida. Por favor, elige piedra, papel o tijera.')
def reglas2(opcion_jugador_1, opcion_jugador_2, vidas_jugador_1, vidas_jugador_2):
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    # Sí son la misma opción, entonces es empate
    if opcion_jugador_1 == opcion_jugador_2:
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""
  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +'         EMPATE')
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT +"""  ___ ___ ___ ___ ___ 
 |___|___|___|___|___|
                              """)
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
    # Con arte ascci el hangman
    hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  xx   |
 /|\  |
 / \  |
      |
=========''']
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "      ")
    # Variable es igual a la función de seleccion de palabra, de donde traera de la lista una palabra aleatoria
    palabra_secreta = seleccionar_palabra()
    # Iniciar lista vacia para almacenar las letras adivinadas
    letras_adivinadas = []
    # Iniciar lista vacia para almacenar las letras intentadas
    letras_intentadas = []
    intentos_maximos = dificultad_ahorcado()
    intentos = 0
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))
    # Bucle infinito que valida todo
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
                hangman_ascci = hangman[1]
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
                hangman_ascci = hangman[2]
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
        # Sí la letra, que solo puede ser una letra y si la letra es de un caracter
        if letra.isalpha() and len(letra) == 1:
            # Válida de que no se descuenten intentos cuando coloca la misma letra
            if letra in letras_intentadas:
                print("Ya intentaste con esa letra, escribe otra")
            # Sí acierta la letra
            elif letra in palabra_secreta:
                # Se agrega a la lista de palabras adivinadas e intentadas
                letras_adivinadas.append(letra) 
                letras_intentadas.append(letra)
                print("¡Correcto!")
            else:
                # por cada vez que pierda, a los intentos se les suma 1
                intentos += 1
                # Agregar letras intentadas en la lista letra
                letras_intentadas.append(letra)
                print("Incorrecto. Te quedan {} intentos.".format(intentos_maximos - intentos))
        # Vuelve y se repite el ciclo hasta que se ingrese una letra valido       
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa una letra válida.")

        print(mostrar_tablero(palabra_secreta, letras_adivinadas))
        # Sí el conjunto de letras adivinadas es igual al conjunto de palabra secreta, entonces encontró la palabra
        if set(letras_adivinadas) == set(palabra_secreta):
            print("Felicidades, has adivinado la palabra!")
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
  +---+
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
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")   
    # Definir variable como la función de seleccionar idioma
    idiomas = seleccionar_idioma_ahorcado()
    # Bucle infinito para que solo puedan ingresar valores válidos
    while True:
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
    # Impresión de mensajes de bienvenida
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"¡¡BIENVENIDO AL JUEGO DEL AHORCADO!!")
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"     ")
    print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"     ")
    # Bucle infinito para que el jugador seleccione el idioma
    while True:
        print("Selecciona en qué idioma quieres las palabras del Ahorcado")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"1. Español")
        print("2. Inglés")
        print("3. Francés")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")
        # Entrada del jugador para seleccionar el idioma
        seleccionar_idioma = input("Escriba el número correspondiente al idioma que desee; las palabras secretas del ahorcado serán en el idioma elegido: ")
        # Asignación del idioma según la elección del jugador
        if seleccionar_idioma == '1':
            idioma = 1
            break
        elif seleccionar_idioma == '2':
            idioma = 2
            break
        elif seleccionar_idioma == '3':
            idioma = 3
            break
        # Mensaje de error en caso de que se ingrese un número inválido
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.")
    # Retorno del idioma seleccionado
    return idioma

# PALABRA OCULTA
def mostrar_tablero(palabra, letras_adivinadas): # Función para mostrar el tablero actualizado con las letras adivinadas
    # Impresión de espacios en blanco para mejorar la presentación
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    # Inicialización de la variable para almacenar el resultado del tablero
    resultado = ""
    # Iteración a través de cada letra de la palabra
    for letra in palabra:
        # Verificación de si la letra está en las letras adivinadas
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    # Eliminación de espacios adicionales al inicio y al final del resultado
    return resultado.strip()

# DIFICULTAD AHORCADO     
def dificultad_ahorcado(): # Función para seleccionar la dificultad del juego del Ahorcado y determinar la cantidad de intentos
    # Impresión de espacios en blanco para mejorar la presentación
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"                                                                                                                                                ")
    # Inicialización de la variable de vidas del jugador en el juego del Ahorcado
    vidas_jugador_ahorcado = 0
    # Bucle infinitopara que el jugador seleccione el nivel de dificultad
    while True:
        print(Fore.MAGENTA + Back.BLACK + Style.BRIGHT +"")
        print("Selecciona el nivel de dificultad del Ahorcado")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT +"1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        print(Fore.RED + Back.BLACK + Style.BRIGHT + "")
        # Pedir al jugador para seleccionar la dificultad
        seleccionar_dificultad = input("Escriba el número correspondiente de la dificultad que desee; esto definirá los intentos que tendrá (1 = 8 intentos, 2 = 6 intentos, 3 = 4 intentos): ")
        # Asignación de la cantidad de intentos según la dificultad seleccionada
        if seleccionar_dificultad == '1':
            vidas_jugador_ahorcado = 7
            break
        elif seleccionar_dificultad == '2':
            vidas_jugador_ahorcado = 6
            break
        elif seleccionar_dificultad == '3':
            vidas_jugador_ahorcado = 5
            break
        # Vuelve y se repite el ciclo hasta que se ingrese un número valido
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.")
    # Retorno de la cantidad de intentos
    return vidas_jugador_ahorcado

# SOPA DE LETRAS - SALIR
def juego_sopa_de_letras(): # En este caso, tuvimos problemas con la sopa de letras por lo cual lo dejamos en otro archivo
    # Esta función cumple lo mismo que la función de salir
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
    # Función salir
    exit()

# SALIR
def salir():
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
def seleccionar_juego(): # Bucle para que el jugador solo pueda introducir los valores 1, 2 y 3 para seleccionar el juego o 4 para salir                                                                                                                                             ")

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
            juego_sopa_de_letras()
            break
        elif eleccion == '4':
            salir()
            break
        # Vuelve y se repite el ciclo hasta que se ingrese un número valido
        else:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "Por favor, ingresa un número válido.")
            # Limpiar consola
            os.system("cls")
            
# INICIAR
if __name__ == "__main__":
    init()
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
    time.sleep(4)
    # Limpiar consola
    os.system("cls")
    # Inicia la función para seleccionar el juego desde el menu.
    seleccionar_juego()
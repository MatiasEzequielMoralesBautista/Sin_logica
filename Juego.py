import pygame
import random
import os
import json

# pygame.init()
# pantalla = pygame.display.set_mode((800,400))
    # for evento in pygame.event.get():
    #     if evento.type == pygame.QUIT:
    #         pygame.quit()
    #         quit()
    #     pantalla.fill((0,255,0))
    #     pygame.display.update()

############################################
def leer_archivo_csv(archivo:str,lista_preguntas:list):
    if os.path.exists(archivo):
        with open(archivo,"r") as preguntas:
            preguntas.readline()
            for i in preguntas:
                leer_preguntas = i.split(",")
                diccionario = crear_diccionarios(leer_preguntas)
                lista_preguntas.append(diccionario)
            # mostrar_diccionario(lista_preguntas)          #mostrar todo
            return lista_preguntas
    else:
        print("El archivo no exite o no se encuentra.")
############################################

############################################
def crear_diccionarios(leer_preguntas:list):
    diccionario = {
    "preguntas" : leer_preguntas[0],
    "respuesta_1" : leer_preguntas[1],
    "respuesta_2" : leer_preguntas[2],
    "respuesta_3" : leer_preguntas[3],
    "respuesta_4" : leer_preguntas[4],
    "respuesta_correcta" : leer_preguntas[5]
    }
    return diccionario
############################################

############################################
def mostrar_diccionario(lista: list):
    for i in range(0, len(lista)):
        for j in range(1,4):
            print(f"{lista[i][j].strip()}")
        
        respuesta = int(input("Ingrese su respuesta correcta (1-4): "))
        if respuesta in [1, 2, 3, 4]:
            opcion_seleccionada = lista[i][f"respuesta_{respuesta}"].strip()
            respuesta_correcta = lista[i]["respuesta_correcta"].strip()
            
            if opcion_seleccionada == respuesta_correcta:
                print("CORRECTO")
            else:
                print("INCORRECTO")
        else:
            print("Opción no válida. Intenta de nuevo.")
############################################

############################################
def mostrar_menu(lista):
    while True:
        opciones = int(input("Ingrese (1) para jugar.\n--->> "))
        if opciones == 1:
            mostrar_diccionario(lista)
############################################

#------------------------------------------------------------------------------
#agus--------------------------------------------------------------------------
# def generar_json(nombre_archivo:str,lista:list)->bool:
#     if type(lista)==list and len(lista) > 0:
#         with open(nombre_archivo,'a') as archivo:
#             json.dump(lista,archivo,indent=4)
#         retorno = True
#     else:
#         retorno = False
#     return retorno

# lista = ['Dario','puntaje','fecha','hola','chau']
# generar_json("pruebas.json",lista)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# lista_preguntas = []
# leer_archivo_csv("preguntas.csv",lista_preguntas)

# print(lista_preguntas)
# print(diccionario["respuesta_correcta"])
lista_preguntas = []
lista = leer_archivo_csv("preguntas.csv",lista_preguntas)

mostrar_menu(lista)


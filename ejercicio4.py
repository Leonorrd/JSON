#!/usr/bin/python
# _*_ coding: utf-8 
#Importa fichero Json
import json
#lee fichero Json
with open('monumentos.json') as data_file:    
    doc = json.load(data_file)

#Pide el id del monumento y te da la descripción del monumento la latitud y longitud.

ejer = raw_input("número de ejercicio: ")
numid= raw_input("id monumento")
#ejercicio 4
if ejer == "4":

    for nombre in doc:
	print nombre["nombre"]
        print nombre["direccion"]
	print nombre["tipo"]

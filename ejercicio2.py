#!/usr/bin/python
# _*_ coding: utf-8 
#Importa fichero Json
import json
#lee fichero Json
with open('monumentos.json') as data_file:    
    doc = json.load(data_file)

#Muestra el nombre monumentos y direcciónn.

ejer = raw_input("número de ejercicio: ")
#ejercicio 2
if ejer == "2":
    for nombre in doc:
	print nombre["nombre"]
        print nombre["direccion"]

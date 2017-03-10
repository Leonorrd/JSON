#!/usr/bin/python
# _*_ coding: utf-8 
#Importa fichero Json
import json
#lee fichero Json
with open('monumentos.json') as data_file:    
    doc = json.load(data_file)

#Muestra los nombres  de monumentos que hay.
ejer = raw_input("número de ejercicio: ")
#ejercicio 1
if ejer == "1":
    for nombre in doc:
        print nombre["nombre"]

'''JESUS DAVID MEJIA VERGARA'''
import numpy as np
from matplotlib import pyplot as plt
from random import randint, uniform,random

'''Para el Ejercicio necesitamos 50 estudiantes'''

array_edades1 = []
array_edades2 = []
array_edades3 = []
rango1 = 20
rango2 = 30
'''Para ahorrar procesos, voy a generar numeros aleatorios, los cuales seran entre rango1 - rango2
    estos van a representar las edades, y los añadire a un vector'''

for i in range(1,51):#DE ESTA FORMA GENERAMOS 50 ESTUDIANTES
    array_edades1.append(randint(rango1,rango2))

for i in range(rango1,rango2+1):
    array_edades2.append(i)

for i in array_edades2:
    cantidad = 0
    for j in array_edades1:
        if i == j:
            cantidad = cantidad + 1
    array_edades3.append(cantidad)

print('Datos de Trabajo\n')
print('Edades')
print(array_edades1)
print('Edades sin valores repetidos')
print(array_edades2)
print('Cantidad de personas con la edad')
print(array_edades3)

print('\nGestion de Datos\n')

print ("Edades:")
print (array_edades1)

print("Rango:")
print(np.ptp(array_edades1))

print("Tercer Percentil:")
print(np.percentile(array_edades1,3))

print("Mediana:")
print(np.median(array_edades1))

print("Media:")
print(np.mean(array_edades1))

print("Desviacion Estandar:")
print(np.std(array_edades1))

x = array_edades2
y = array_edades3

plt.bar(x, y, align = 'center')
plt.title("Diagrama de Barras")
plt.ylabel("Cantidad")
plt.xlabel("Edades")
plt.show()





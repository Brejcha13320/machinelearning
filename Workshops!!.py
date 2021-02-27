import numpy as np
from matplotlib import pyplot as plt

a = np.array([20,22,23,28,21,25,25,24])

print ("Edades:")
print (a)

print("Rango:")
print(np.ptp(a))

print("Tercer Percentil:")
print(np.percentile(a,3))

print("Mediana:")
print(np.median(a))

print("Media:")
print(np.mean(a))

print("Desviacion Estandar:")
print(np.std(a))

'''[20,22,23,28,21,25,25,24]'''
x = [20,22,23,28,21,25,24]
y = [1,1,1,1,1,2,1]

plt.bar(x, y, align = 'center')
plt.title("Diagrama de Barras")
plt.ylabel("Cantidad")
plt.xlabel("Edades")
plt.show()
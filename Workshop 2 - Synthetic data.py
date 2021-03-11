'''importar libreria scipy y matplotlib para poder usar sus funciones'''
from scipy import ndimage
import matplotlib.pyplot as plt

'''La variable np no estaba definiada, por esto el codigo no funcionaba'''
import numpy as np

'''Le damos el tamaño que van a tener las imagenes np.zeros((alto,ancho))'''
im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')

sob = np.hypot(sx, sy)

'''Tamaño de la ventana'''
plt.figure(figsize=(16, 5))

'''subplot de trabajo de la figura 1 square'''

plt.subplot(141)
'''mostramos la imagen 1'''
plt.imshow(im, cmap=plt.cm.gray)
'''con el axis('off') desactivamos los marcos que determinan el ancho y alto de la imagen'''
plt.axis('off')
'''damos el titulo y el tamaño de letra'''
plt.title('square', fontsize=20)

'''subplot de trabajo de la figura 2 solbe x direction)'''

plt.subplot(142)
'''mostramos la imagen 2'''
plt.imshow(sx)
'''con el axis("off") desactivamos los marcos que determinan el ancho y alto de la imagen'''
plt.axis('off')
'''damos el titulo y el tamaño de letra'''
plt.title('Sobel (x direction)', fontsize=20)

'''subplot de trabajo de la figura 3 solbe filter'''

plt.subplot(143)
'''mostramos la imagen 3'''
plt.imshow(sob)
'''con el axis("off") desactivamos los marcos que determinan el ancho y alto de la imagen'''
plt.axis('off')
'''damos el titulo y el tamaño de letra'''
plt.title('Sobel filter', fontsize=20)

'''area de trabajo de la figura 4'''

'''esto causa el efecto de la figura 4'''
im += 0.07*np.random.random(im.shape)

'''como actualizamos el valor de im entonces tambien actualizamos las variables sx y sy,
    de esta forma mostramos la nueva imagen, si esto no se actualiza muestra la imagen 3'''
sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

'''subplot de trabajo de la figura 4'''

plt.subplot(144)
'''mostramos la imagen 4'''
plt.imshow(sob)
'''con el axis("off") desactivamos los marcos que determinan el ancho y alto de la imagen'''
plt.axis('off')
'''damos el titulo y el tamaño de letra'''
plt.title('Sobel for noisy image', fontsize=20)

'''wspace la es la distancia entre cada imagen'''
plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)

'''mostramos la ventana'''
plt.show()
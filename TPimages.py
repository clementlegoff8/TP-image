# TP images ################################################

# Import des librairies ####################################

import numpy as np
import matplotlib.pyplot as plt

# Création d'une image de couleur ###########################

image = np.empty((91, 91, 3), dtype=np.uint8)

image[:] = np.array([0,255,0])

#print(image[0,0])
#print(image[-1,-1])

image[::10]= np.array([0,255,255])
image[:,::10]= np.array([0,255,255])

#plt.imshow(image)
#plt.show()

# Lecture d'une image en couleur ############################

im = plt.imread("data/les-mines.jpg")
#print(bool(im.flags.writeable))

im2 = im.copy()
#print(bool(im2.flags.writeable))

#print(type(im2))
#print(np.ndim(im2))
#print(im2.shape[:2])
#print(im.itemsize)
#print(im.dtype)
#print(im2.max(),im2.min())

#plt.imshow(im2[:10,:10])

#for i in (2,5,10,20):
    #plt.imshow(im2[::i,::i])
    #plt.show()

# Accès à une partie d'image ###################################

def sous_image_centree(l,c):
    i = im2.shape[0] //2
    j = im2.shape[1] //2
    sous_im = im2[i-l//2:i+l//2,j-c//2:j+c//2]
    return sous_im

#plt.imshow(sous_image_centree(100,200))
#plt.show()

# Canaux RGB de l'image ###################################################

r = im2[::,::,0]
g = im2[::,::,1]
b = im2[::,::,2]
#plt.imshow(r,cmap="Reds")
#plt.show()
#plt.imshow(g,cmap="Greens")
#plt.show()
#plt.imshow(b,cmap="Blues")
#plt.show()

im3 = im.copy()

im3[-200:,-200:] = np.array([255, 255, 255])
im3[-200::2,-200:] = np.array([255,0,0])

#plt.imshow(im3[-20:,-20:])
#plt.show()

# Transparence des images ###################################################

newim = np.empty((533,800,4),dtype=np.uint8)
newim[::,::,:3] = im2
newim[::,::,3] = 128

#plt.imshow(newim)
#plt.show()

# Image en niveaux de gris en float ####################################################

gris1 = im/255.0
gris1[::,::,0] = (gris1[::,::,0] + gris1[::,::,1] + gris1[::,::,2])/3
gris1[::,::,1] = gris1[::,::,0]
gris1[::,::,2] = gris1[::,::,0]

#plt.imshow(gris1)
#plt.show()

gris2 = im/255.0
gris2[::,::,0] = 0.299 * gris2[::,::,0] + 0.587 * gris2[::,::,1] + 0.114 * gris2[::,::,2]
gris2[::,::,1] = gris2[::,::,0]
gris2[::,::,2] = gris2[::,::,0]

#plt.imshow(gris2)
#plt.show()
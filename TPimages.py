# TP images #######################################################################################

# Import des librairies ###########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Création d'une image de couleur #################################################################

image = np.empty((91, 91, 3), dtype=np.uint8) #création d'un tableau non initialisé

image[:] = np.array([0,255,0]) #on met tous les pixels en vert

#print(image[0,0]) #valeur RGB du premier pixel
#print(image[-1,-1]) #valeur RBG du dernier pixel

image[::10]= np.array([0,255,255]) #lignes bleues
image[:,::10]= np.array([0,255,255]) #colonnes bleues

#plt.imshow(image)
#plt.show()

# Lecture d'une image en couleur ###################################################################

im = plt.imread("data/les-mines.jpg")
#print(bool(im.flags.writeable)) #vérification qu'on peut lire l'image

im2 = im.copy()
#print(bool(im2.flags.writeable))

#print(type(im2))
#print(np.ndim(im2))
#print(im2.shape[:2])
#print(im.itemsize)
#print(im.dtype)
#print(im2.max(),im2.min())

#plt.imshow(im2[:10,:10]) #affichage du rectangle de 10x10 pixels en haut à gauche

# Accès à des partie d'image ########################################################################

#for i in (2,5,10,20):
    #plt.imshow(im2[::i,::i]) #on ne garde qu'une colonne/ligne sur i
    #plt.show()

def sous_image_centree(l,c): #renvoie le rectangle de l lignes et c colonnes au milieu de l'image
    i = im2.shape[0] //2
    j = im2.shape[1] //2
    sous_im = im2[i-l//2:i+l//2,j-c//2:j+c//2]
    return sous_im

#plt.imshow(sous_image_centree(100,200))
#plt.show()

# Canaux RGB de l'image ###############################################################################

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

#im3[-200:,-200:] = np.array([219, 112, 147])
im3[-200:,-200:] = np.array([255, 255, 255]) #on place un carré blanc en bas à droite
im3[-200::2,-200:] = np.array([255,0,0]) #avec des lignes rouges

#plt.imshow(im3[-20:,-20:])
#plt.show()

# Transparence des images ##############################################################################

newim = np.empty((533,800,4),dtype=np.uint8) #nouvelle image non initialisée de la bonne taille
newim[::,::,:3] = im2
newim[::,::,3] = 128 #valeur dans le nouveau canal de transparence

#plt.imshow(newim)
#plt.show()

# Image en niveaux de gris en float #####################################################################

gris1 = im/255.0 #passage en flottants
gris1[::,::,0] = (gris1[::,::,0] + gris1[::,::,1] + gris1[::,::,2])/3
gris1[::,::,1] = gris1[::,::,0]
gris1[::,::,2] = gris1[::,::,0] #on passe tous les pixels à la valeur moyenne RGB

#plt.imshow(gris1)
#plt.show()

gris2 = im/255.0
gris2[::,::,0] = 0.299 * gris2[::,::,0] + 0.587 * gris2[::,::,1] + 0.114 * gris2[::,::,2]
gris2[::,::,1] = gris2[::,::,0]
gris2[::,::,2] = gris2[::,::,0]

#plt.imshow(gris2)
#plt.show()

gris3 = gris1**2 #on passe toutes les valeurs au carré

#plt.imshow(gris3)
#plt.show()

gris4 = gris1**(1/2) #on prend la racine carrée de toutes les valeurs

#plt.imshow(gris4)
#plt.show()

gris5 = (gris1*255).astype(np.uint8) #on repasse en entiers

#plt.imshow(gris5)
#plt.show()

# Affichage grille de figures ##############################################################################

#fig, axes = plt.subplots(1,3) #pour afficher 3 images côte à côte

#axes[0].imshow(gris1)
#axes[0].set_title('Moyenne')
#axes[0].axis('off')
#axes[1].imshow(gris2)
#axes[1].set_title('Correction Y')
#axes[1].axis('off')
#axes[2].imshow(gris4)
#axes[2].set_title('Racine carrée')
#axes[2].axis('off')

#plt.show()

fig, axes = plt.subplots(3,3) #pour faire un damier

axes[0,0].imshow(gris1)
axes[0,0].axis('off')
axes[0,1].imshow(gris2)
axes[0,1].axis('off')
axes[0,2].imshow(gris4)
axes[0,2].axis('off')
axes[1,0].imshow(gris4)
axes[1,0].axis('off')
axes[1,1].imshow(gris1)
axes[1,1].axis('off')
axes[1,2].imshow(gris2)
axes[1,2].axis('off')
axes[2,0].imshow(gris2)
axes[2,0].axis('off')
axes[2,1].imshow(gris4)
axes[2,1].axis('off')
axes[2,2].imshow(gris1)
axes[2,2].axis('off')

plt.show()
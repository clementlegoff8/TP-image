# TP images (partie 2) #############################################################################################

import numpy as np
from matplotlib import pyplot as plt

# Création d'un patchwork ##########################################################################################

def rectangle_size(n): #renvoie la taille de rectangle nécessaire en fonction du nombre de couleurs
    c = int(np.ceil(np.sqrt(n)))
    l = int(np.ceil(n/c))
    return (l,c)

def patchwork(colors, side=10, background=[169, 169, 169]): #crée le patchwork voulu
    l,c = rectangle_size(len(colors))
    image = np.empty((side*l,side*c,3),dtype=np.uint8)
    for k in range(len(colors)):
        i,j = k//c, k%c
        image[side*i:side*(i+1),side*j:side*(j+1)] = colors[k]
    j = j+1
    while j < c:
        image[side*i:side*(i+1),side*j:side*(j+1)] = background
        j = j+1
    return image

colors = [[255, 0, 0],[0, 255, 0],[0, 0, 255],[255, 255, 0],[255, 0, 255]]

#plt.imshow(patchwork(colors,10))
#plt.show()

#plt.imshow(patchwork(colors+colors, side=10, background=[0, 0, 0]))
#plt.show()

color_names = ['DarkBlue', 'AntiqueWhite', 'LimeGreen', 'NavajoWhite', 'Tomato', 'DarkGoldenrod', 'LightGoldenrodYellow', 'OliveDrab', 'Red', 'Lime']

data = open("data/rgb-codes.txt",'r')
dictionnaire_couleurs = {}
for ligne in data:
    a = ligne.strip().split(" ")
    dictionnaire_couleurs[a[0]]=[int(a[1]),int(a[2]),int(a[3])]

#print(dictionnaire_couleurs["Red"])
#print(dictionnaire_couleurs["Lime"])
#print(dictionnaire_couleurs["Blue"])

def patchwork2(colors, side=10, background="DarkGray"):
    l,c = rectangle_size(len(colors))
    image = np.empty((side*l,side*c,3),dtype=np.uint8)
    for k in range(len(colors)):
        i,j = k//c, k%c
        image[side*i:side*(i+1),side*j:side*(j+1)] = dictionnaire_couleurs[colors[k]]
    j = j+1
    while j < c:
        image[side*i:side*(i+1),side*j:side*(j+1)] = dictionnaire_couleurs[background]
        j = j+1
    return image

#plt.imshow(patchwork2(color_names))
#plt.show()

couleurs_aleatoires = [np.random.choice(list(dictionnaire_couleurs.keys())) for i in range(np.random.randint(1,21))]

#plt.imshow(patchwork2(couleurs_aleatoires))
#plt.show()

couleurs_blanches = []
for couleur in list(dictionnaire_couleurs.keys()):
    if "White" in couleur:
        couleurs_blanches.append(couleur)

#plt.imshow(patchwork2(couleurs_blanches))
#plt.show()

couleurs_jaunes = []
for couleur in list(dictionnaire_couleurs.keys()):
    if "Yellow" in couleur:
        couleurs_jaunes.append(couleur)

#plt.imshow(patchwork2(couleurs_jaunes))
#plt.show()

#plt.imshow(patchwork2(list(dictionnaire_couleurs.keys())))
#plt.show()

#plt.imsave("patchwork.png",patchwork2(list(dictionnaire_couleurs.keys())))
#patch = plt.imread("patchwork.png")
#plt.imshow(patch)
#plt.show()

# Image en sépia ########################################################################################################

matrice_sepia = [[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]

def sepia(image):
    sepia = image.copy()
    l,c,p = image.shape
    for i in range(l):
        for j in range(c):
            pixel = np.dot(matrice_sepia,np.array(sepia[i,j]/255.0,dtype=float))
            for k in range(3):
                if pixel[k] > 1:
                    pixel[k] = 1
            sepia[i,j] = 255.0*pixel
    return sepia

mines = plt.imread("data/les-mines.jpg")

#plt.imshow(mines)
#plt.show()
#plt.imshow(sepia(mines))
#plt.show()

# Somme dans une image et overflow ########################################################################################

image_somme = mines[:,:,0] + mines[:,:,1] + mines[:,:,2]
#print(image_somme.dtype)
#print(image_somme.max()) #c'est 255 vu qu'on est en uint8 c'est logique...

#plt.imshow(image_somme, cmap="gray")
#plt.show()

l,c,p = mines.shape
image_somme2 = np.empty((l,c,1))
for i in range(l):
    for j in range(c):
        image_somme2[i,j] = np.sum(mines[i,j])
#print(image_somme2.dtype)
#print(image_somme2.max())

#plt.imshow(image_somme2, cmap="gray")
#plt.show()

new_im = image_somme2.astype(np.uint8)
new_im = np.where(new_im >= 127, 255, 0)
#plt.imshow(new_im, cmap="gray")
#plt.show()
#print(np.unique(new_im))

# Exemple de qualité de compression ########################################################################################

from PIL import Image

mines2 = Image.open("data/les-mines.jpg")
#print(mines2.fp.seek(0, 2))
#print(np.allclose(np.array(mines2), mines))

plt.imsave("Mines.jpg",mines)
mines2.save("Mines2.jpg", quality=100)

new_mines = Image.open("Mines.jpg")
new_mines2 = Image.open("Mines2.jpg")
#print(new_mines.fp.seek(0, 2))
#print(new_mines2.fp.seek(0, 2)) #c'est beaucoup plus

#fig, axes = plt.subplots(1, 2)
#axes[0].imshow(new_mines)
#axes[1].imshow(new_mines2)
#plt.show() #aucune différence apparente...
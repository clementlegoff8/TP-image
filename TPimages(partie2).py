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
# TP images ##########################

import numpy as np
import matplotlib.pyplot as plt

image = np.empty((91, 91, 3), dtype=np.uint8)

image[:] = np.array([0,255,0])

#print(image[0,0])
#print(image[-1,-1])

image[::10]= np.array([0,255,255])
image[:,::10]= np.array([0,255,255])

#plt.imshow(image)
#plt.show()

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

def sous_image_centree(l,c):
    i = im2.shape[0] //2
    j = im2.shape[1] //2
    sous_im = im2[i-l//2:i+l//2,j-c//2:j+c//2]
    return sous_im

plt.imshow(sous_image_centree(100,100))


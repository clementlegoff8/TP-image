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

print(type(im2))
print(np.ndim(im2))
print(np.shape(im2))
print(type(im2[0,0,0]))
print(im2[0,0])

#plt.imshow(im2[:10,:10])

plt.show()
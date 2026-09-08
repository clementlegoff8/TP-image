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
im.flags.writeable
import matplotlib.pyplot as plt
# %matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

img = plt.imread("ei1.jpeg")
img2 = plt.imread("ei3.jpeg")

eiCropped = img.copy()
eiCropped = img[0:256, 64:320]

eiCropped1 = img2.copy()
eiCropped1 = img2[64:256, 128:320]

print('ei Ori Shape : ', img.shape)
print('ei Crop Shape : ', img.shape)

print('ei1 Ori Shape : ', img2.shape)
print('ei1 Crop Shape : ', img2.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Citra Input 1")

ax[1].imshow(img2, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(eiCropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(eiCropped, cmap='gray')
ax[3].set_title('Citra Output 2')

inv = invert(eiCropped)
print('Shape Input : ', eiCropped.shape)
print('Shape Output : ', inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(eiCropped)
ax[0].set_title("Citra Input")

ax[1].hist(eiCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')

gray = rgb2gray(eiCropped1)
print("img2gray shape = ", gray.shape)

copycopy = gray.copy().astype(float)

m1, n1 = copycopy.shape
output1 = np.empty([m1, n1])

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copycopy[baris, kolom] + 100

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(eiCropped1, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].hist(eiCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')
plt.show()

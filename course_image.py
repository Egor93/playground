from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=Image.open("pluto-1300x815.jpg")
# convert to numpy array
pic = np.array(img)[:,:,2]
# average values - coarsen
coarseness = 5
shape = np.array(pic.shape, dtype=float)
new_shape = np.ceil(shape/coarseness).astype(int)*coarseness
# Create the zero-padded array and assign it with the old density
zp_pic = np.zeros(new_shape)
zp_pic[0:pic.shape[0],0:pic.shape[1]]=pic
pic_reshaped=zp_pic.reshape(new_shape[0]//coarseness, coarseness, new_shape[1]//coarseness,coarseness)
pic_coarse=pic_reshaped.sum(axis=(1,3))
plt.imshow(pic_coarse);plt.show()

#%%
from PIL import Image
import numpy as np
import math

# %%
myimage=Image.open('uws.jpeg')
# %%
myimage.show()
# %%
myimage.size
# %%
myimage.format
# %%
myarray=np.array(myimage)
# %%
myarray.shape
# %%
myimage2=Image.fromarray(myarray)
# %%
myimage2.show()
# %%
a=np.ones(10000).reshape(10,1000)
a=a/2
b=Image.fromarray(a)
b.show()
# %%
myimage
# %%
#myarray[100:400,100:400]
b=myimage.convert('L')
# %%
a=np.array(b)
# %%
a.shape
# %%
a
# %%
x=np.zeros((2,3))
# %%
x[:,0] =[1,2]
x[:,0].shape
# %%
x
# %%

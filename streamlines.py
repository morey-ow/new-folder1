# streamlines.py
# -------------------------------------------------------------------------
# Create streamlines from a vector field.
# "A Student's Guide to Python for Physical Modeling" 
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt

# generate grid of points
lower, upper, step = -2, 2, 0.1
coords = np.arange(lower, upper+step, step)
X, Y = np.meshgrid(coords, coords)

# define vector field
Vx, Vy = Y, -X

# display streamlines defined by vector field
plt.figure()
plt.streamplot(coords, coords, Vx, Vy)
plt.axis('square')
plt.show()

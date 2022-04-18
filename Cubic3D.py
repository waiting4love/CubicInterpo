import numpy as np
import matplotlib.pyplot as plt

def cubic(x):
    if x < 0:
        x = -x
    bi_coef = 0
    if x<=1:
        bi_coef = 1.5*x**3 - 2.5*x**2 + 1
    elif x<=2:
        bi_coef = -0.5*x**3 + 2.5*x**2 - 4*x + 2
    return bi_coef

def interp2(src, x, y):
    ox = int(x)
    oy = int(y)
    dx = x - ox
    dy = y - oy
    if dx == 0 and dy == 0:
        return src[oy, ox]
    gray_val = 0
    for n in range(-1, 3):
        k1 = cubic(dy - n)
        oy2 = np.clip(oy + n, 0, len(src[0]) - 1)
        for m in range(-1, 3):
            k2 = cubic(m - dx)
            ox2 = np.clip(ox + m, 0, len(src[0]) - 1)
            gray_val += k1 * k2 * src[oy2, ox2]
    return gray_val

def peaks(x, y):
    return 3*(1-x)**2*np.exp(-(x**2) - (y+1)**2) - 10*(x/5 - x**3 - y**5)*np.exp(-x**2-y**2) - 1/3*np.exp(-(x+1)**2 - y**2)

x = np.arange(-3,3,1)
y = np.arange(-3,3,1)
x_2d, y_2d = np.meshgrid(x, y)
z = peaks(x_2d, y_2d)

x2 = np.arange(-3,3,0.1)
y2 = np.arange(-3,3,0.1)

z2 = np.empty((len(y2), len(x2)))
for yi,yy in enumerate(y2):
    for xi,xx in enumerate(x2):
        z2[yi, xi] = interp2(z, xx+3, yy+3)

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x_2d, y_2d, z)


x_2d2, y_2d2= np.meshgrid(x2, y2)
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x_2d2, y_2d2, z2)

plt.show()
import cv2
import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import matplotlib.pyplot as plt

# input the image path
image_path = "../Res/imageO/pku.jpg"
img = cv2.imread(image_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(img_gray.shape)
p, q = img_gray.shape
# show the raw image
plt.figure(0)
plt.imshow(img_gray, cmap="gray")
plt.title("Raw Image")

# Set Basic parameters
N1 = min(p, q)
N = 1024    # 采样率
scale = 1/4

size_scale = N / N1 * scale
size_scale_x = int(size_scale * p)
size_scale_y = int(size_scale * q)
print(size_scale_x)

X1 = cv2.resize(img_gray, [size_scale_x, size_scale_y])

M1, N1 = X1.shape
X = np.zeros((N, N))
X[int(N/2 - M1/2 + 1):int(N/2 + M1/2), int(N/2 - N1/2 + 1):int(N/2 + N1/2)] = X1[1:M1, 1:N1]

h = 0.632e-3        # 波长，单位mm
k = 2 * np.pi / h
pix = 0.00465        # CCD像素宽度
L = N * pix         # CCD宽度
z0 = 1000           # 衍射距离
L0 = h * z0 / pix   # 重建像平面宽度

Y = X
b = np.random.rand(N, N) * 2 * np.pi
f = Y * np.exp(1j * b)     # 叠加随机相位噪声，形成振幅正比于图像的初始场复振幅
X0 = np.abs(f)

plt.figure(1)
plt.imshow(X, cmap="gray")
plt.title("Scale Image")

# Fresnell
n = np.array(range(N))
x = -L0 / 2 + L0 / N * n
y = x
yy, xx = np.meshgrid(y, x)
Fresnel = np.exp(1j * k / 2 / z0 * (xx * xx + yy * yy))
f2 = f * Fresnel
Uf = fft2(f2, (N, N))
Uf = fftshift(Uf)
x = -L / 2 + L / N * n
y = x
yy, xx = np.meshgrid(y, x)
phase = np.exp(1j * k * z0) / (1j * h * z0) * np.exp(1j * k / 2 / z0 * (np.power(xx, 2) + np.power(yy, 2)))
Uf = Uf * phase

plt.figure(2)
plt.imshow(np.abs(Uf), cmap="gray")
plt.title("Amplitude distribution of object light")

# Reference Light
Qx = (4 - 2.5) * L0 / 8 / z0
Qy = Qx
x = np.linspace(-L/2, L/2 - L/N, N)
y = x
X, Y = np.meshgrid(x, y)
Ar = np.max(np.abs(Uf))
Ur = Ar * np.exp(1j * k * (X * Qx + Y * Qy))

# Interference
Uh = Ur + Uf
Wh = Uh * np.conj(Uf)
Wh = np.abs(Wh)
Imax = np.max(Wh)
Ih = Wh / Imax * 255

plt.figure(3)
plt.imshow(Ih, cmap="gray")
plt.title("Interference Hologram")
cv2.imwrite("./result/oaih_pku_CGH.bmp", Ih)

# Reconstruction
N1, N2 = Ih.shape
N = min(N1, N2)
h = 0.000632        # 波长(mm)
z0 = 1000
L = N * pix         # CCD宽度(mm)
In = Ih

n = np.array(range(N))
x = -L / 2 + L / N * n
y = x
yy, xx = np.meshgrid(y, x)
k = 2 * np.pi / h

Fresnel = np.exp(-1j * k / 2 / z0 * (np.power(xx, 2) + np.power(yy, 2)))
f2 = In * Fresnel
Uf = ifft2(f2, (N, N))
Uf = fftshift(Uf)
L0 = h * z0 / pix

x = -L0 / 2 + L0 / N * n
y = x
yy, xx = np.meshgrid(y, x)
phase = np.exp(-1j * k * z0) / (-1j * h * z0) * np.exp(-1j * k / 2 / z0 * (np.power(xx, 2) + np.power(yy, 2)))
U0 = Uf * phase
U0 = abs(U0)
Gmax = np.max(U0)
Gmin = np.min(U0)
# U0 = U0 / Gmax * 255

# try to change the parameter to get the best image
p = 10
Gm = Gmax / p
np.clip(U0, Gmin, Gm, out=U0)

U = U0 / Gm * 255

plt.figure(4)
plt.imshow(U0, cmap="gray")
plt.title("Amplitude distribution of object plane reconstructed by inverse operation")
cv2.imwrite("./result/oaih_pku_recover.bmp", U)

plt.show()










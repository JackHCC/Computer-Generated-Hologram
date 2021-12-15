import cv2
import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import matplotlib.pyplot as plt

# input the image path
image_path = "../Res/image256/lena.png"
img = cv2.imread(image_path)
print(img.shape)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(img_gray.shape)
p, q = img_gray.shape
# show the raw image
plt.figure(0)
plt.imshow(img_gray, cmap="gray")
plt.title("Raw Image")

N1 = min(p, q)
N = 1080    # 采样率
scale = 0.5

size_scale = int(N / N1 * scale)
size_scale_x = int(size_scale * p)
size_scale_y = int(size_scale * q)

X1 = cv2.resize(img_gray, [size_scale_x, size_scale_y])

M1, N1 = X1.shape
X = np.zeros((N, N))
X[int(N/2 - M1/2 + 1):int(N/2 + M1/2), int(N/2 - N1/2 + 1):int(N/2 + N1/2)] = X1[1:M1, 1:N1]

h = 0.532e-3        # 波长，单位mm
k = 2 * np.pi / h
pix = 0.0064        # SLM像素宽度
L = N * pix         # SLM宽度
z0 = 1200           # 衍射距离
L0 = h * z0 / pix   # 重建像平面宽度

Y = X
# a = np.ones((N, N))
b = np.random.rand(N, N) * 2 * np.pi
print(b, b.shape)
U0 = Y * np.exp(1j * b)     # 叠加随机相位噪声，形成振幅正比于图像的初始场复振幅
X0 = np.abs(U0)

plt.figure(1)
plt.imshow(X, cmap="gray")
plt.title("Scale Image")



'''
    Record:记录
'''
n = np.array(range(N))
print(n.shape)
x = -L0 / 2 + L0 / N * n
y = x
yy, xx = np.meshgrid(y, x)
print(yy.shape, xx.shape)
Fresnel = np.exp(1j * k / 2 / z0 * (xx * xx + yy * yy))
print(Fresnel)
f2 = U0 * Fresnel
Uf = fft2(f2, (N, N))
# Uf = fft2(f2)
Uf = fftshift(Uf)
print("Uf", Uf.shape)
x = -L / 2 + L / N * n
y = x
yy, xx = np.meshgrid(y, x)
phase = np.exp(1j * k * z0) / (1j * h * z0) * np.exp(1j * k / 2 / z0 * (np.power(xx, 2) + np.power(yy, 2)))
Uf = Uf * phase

print("Uf * phase", Uf)

plt.figure(2)
plt.imshow(np.abs(Uf), cmap="gray")
plt.title("Amplitude distribution of object light")

Phase = np.angle(Uf) + np.pi
# 形成0-255灰度级的相息图
ki = Phase / 2 / np.pi * 255

print(ki.shape)

plt.figure(3)
plt.imshow(Phase, cmap="gray")
plt.title("Kinoforms")
cv2.imwrite("./result/ki_lena_CGH.bmp", ki)

'''
    Recon:再现
'''
U0 = np.cos(Phase - np.pi) + 1j * np.sin(Phase - np.pi)
n = np.array(range(N))
x = -L / 2 + L / N * n
y = x
yc, xc = np.meshgrid(y, x)
Fresnel = np.exp(-1j * k / 2 / z0 * (np.power(xc, 2) + np.power(yc, 2)))
f2 = U0 * Fresnel
Uf = ifft2(f2, (N, N))
x = -L0 / 2 + L0 / N * n
y = x
yy, xx = np.meshgrid(y, x)
phase = np.exp(-1j * k * z0) / (-1j * h * z0) * np.exp(-1j * k / 2 / z0 * (np.power(xx, 2) + np.power(yy, 2)))
Uf = Uf * phase

Uf = np.abs(Uf)

Uf = Uf * 255 / np.max(Uf)
print(Uf)

plt.figure(4)
plt.imshow(Uf, cmap="gray")
plt.title("Amplitude distribution of object plane reconstructed by inverse operation")
cv2.imwrite("./result/ki_lena_recover.bmp", Uf)

plt.show()

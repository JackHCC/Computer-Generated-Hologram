from PIL import Image
import cv2
import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import matplotlib.pyplot as plt

x32 = 4
y32 = 4

s = 64*8

# input the image path
image_path = "../Res/image64/test.bmp"
g = Image.open(image_path, mode="r")

# convert RGB image to Gray image
g = g.convert("L")
G = np.array(g)
# print(G.shape, G)

p, q = G.shape

# show the raw image
Z = G
plt.figure(0)
plt.imshow(Z, cmap="gray")

# generate a random numbers array of p size
R1 = np.random.rand(p)
# print(R1.shape)

# give random phase
A = Z * np.exp(1j * 2 * np.pi * R1)

# fft2
A = fftshift(fft2(fftshift(A)))
# print(A)

A_fre = np.abs(A)
plt.figure(1)
plt.imshow(A_fre, cmap="gray")

A1 = np.abs(A)
B1 = np.mod(np.angle(A), 2 * np.pi)/(2 * np.pi)
C = np.max(A1)
# print(C)

A2 = int(s/p)
B2 = A2
Z = np.zeros((s, s))

for I in range(0, p):
    y0 = y32 + (I - 1) * B2
    for J in range(0, q):
        x0 = x32 + (J - 1) * A2
        H = np.round(A1[I, J] * B2 / C)
        F1 = round(B1[I, J] * A2)
        W = A2 / 2
        x1 = int(np.round(x0 + F1 - W/2))
        x2 = int(x1 + W - 1)
        y1 = int(np.round(y0 - H/2 + 0.5))
        y2 = int(y1 + H - 1)
        if x2 < J * A2:
            Z[y1:y2, x1:x2] = 1
        else:
            Z[y1:y2, x1:J * A2] = 1
            Z[y1:y2, (J-1) * A2 + 1:x2 - A2] = 1

# 傅里叶全息图
Z_mid = Z * 255
Z_mid_show = Image.fromarray(Z_mid).convert("L")
plt.figure(2)
plt.imshow(Z_mid_show, cmap="gray")
Z_mid_show.save("./result/fh_test_CGH.bmp", "bmp")

P = fftshift(ifft2(Z))

P_show = np.abs(P) * 256
P_reg = P_show * 255 / np.max(P_show)
plt.figure(3)
plt.imshow(P_reg, cmap="gray")

P1 = P_reg[int(s/2 - 128 + 1):int(s/2 + 128), int(s/2 - 128 + 1):int(s/2 + 128)]
plt.figure(4)
plt.imshow(P1, cmap="gray")

Z_large = Z_mid[int(s/2 - 64 + 1):int(s/2 + 64), int(s/2 - 64 + 1):int(s/2 + 64)]
plt.figure(5)
plt.imshow(Z_large, cmap="gray")
Z_large_show = Image.fromarray(Z_large).convert("L")
Z_large_show.save("./result/fh_test_large_CGH.bmp", "bmp")

Z_recover = np.abs(P1) * 255
Z_recover = Z_recover * 255 / np.max(Z_recover)
# print(np.max(Z_recover))

plt.figure(6)
plt.imshow(Z_recover, cmap="gray")
Z_recover_im = Image.fromarray(Z_recover).convert("L")
Z_recover_im.save("./result/fh_test_recover.bmp", "bmp")

plt.show()






















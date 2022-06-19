#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Computer-Generated-Hologram 
@File    :fresnel_hologram.py
@Author  :JackHCC
@Date    :2022/6/15 22:17 
@Desc    :

'''
from PIL import Image
import numpy as np
from scipy.fftpack import fft2, fftshift
import matplotlib.pyplot as plt

cm = 1e-2
mm = 1e-3
um = 1e-6
nm = 1e-9


class Fresnel:
    def __init__(self, lambda_=633 * nm, pix=3.45 * um, z0=1500 * mm, zr=1500 * mm, flag=0, shift=0):
        self.lambda_ = lambda_
        self.pix = pix
        self.z0 = z0
        self.zr = zr
        self.flag = flag
        self.shift = shift

    def zero_padding(self, raw_img):
        width, height = raw_img.shape
        m = 2 * width
        n = 2 * height
        pad_img = np.zeros((m, n))
        posx = (m - width) // 2
        posy = (n - height) // 2
        pad_img[posx:posx + width, posy:posy + height] = raw_img[:, :] / 255
        return pad_img

    def fresnel(self, pad_img, flag=True):
        M, N = pad_img.shape
        Lx0 = np.sqrt(self.lambda_ * self.z0 * M)  # FFT计算时同时满足振幅及相位取样条件的物光场宽度
        Ly0 = np.sqrt(self.lambda_ * self.z0 * N)
        if flag:
            dx0 = Lx0 / M
            dy0 = Ly0 / N
        else:
            dx0 = self.pix
            dy0 = self.pix

        # 菲涅尔全息计算
        x = dx0 * np.array(range(-M // 2, M // 2))
        y = dy0 * np.array(range(-N // 2, N // 2))
        Y, X = np.meshgrid(y, x)
        Fresnel = np.exp(1j * np.pi * (np.power(X, 2) + np.power(Y, 2)) / (self.lambda_ * self.z0))
        f2 = pad_img * Fresnel
        f2 = fftshift(f2)
        Uf = fft2(f2)
        Uf = fftshift(Uf)
        dx1 = (self.lambda_ * self.z0) / (M * dx0)
        dy1 = (self.lambda_ * self.z0) / (N * dy0)
        x1 = dx1 * np.array(range(-M // 2, M // 2))
        y1 = dy1 * np.array(range(-N // 2, N // 2))
        Y1, X1 = np.meshgrid(y1, x1)
        phase = np.exp(1j * 2 * np.pi * self.z0 / self.lambda_) / (1j * self.lambda_ * self.z0) * np.exp(
            1j * np.pi / self.lambda_ / self.z0 * (np.power(X1, 2) + np.power(Y1, 2)))
        Uf = Uf * phase
        T = dx0  # 空域取样间隔
        Uf = Uf * T * T  # 二维离散变换量值补偿
        return Uf

    def wave(self, pad_img):
        M, N = pad_img.shape
        Lx0 = np.sqrt(self.lambda_ * self.z0 * M)  # FFT计算时同时满足振幅及相位取样条件的物光场宽度
        Ly0 = np.sqrt(self.lambda_ * self.z0 * N)
        dx0 = Lx0 / M
        dy0 = Ly0 / N

        x0 = dx0 * np.array(range(-M // 2, M // 2))
        y0 = dy0 * np.array(range(-N // 2, N // 2))
        Y0, X0 = np.meshgrid(y0, x0)

        dx1 = (self.lambda_ * self.zr) / (M * dx0)
        dy1 = (self.lambda_ * self.zr) / (N * dy0)
        x1 = dx1 * np.array(range(-M // 2, M // 2))
        y1 = dy1 * np.array(range(-N // 2, N // 2))
        X1, Y1 = np.meshgrid(x1, y1)

        # 相位物体
        p = np.sin(Y0 * np.pi / 50)
        phaseObject = np.exp(1j * p)
        # planeWave reference
        # pr = 2 * np.pi * X1 * np.sin(5 * np.pi / 180) / self.lambda_ + self.shift
        phi = 2 * np.pi * X1 * np.sin(np.pi / 2) / self.lambda_ + self.shift
        planeWave = np.exp(1j * phi)

        # sphericalWave
        L = -N * dx1
        xr = -L / 4
        phi = np.pi * (np.power(X1 + xr, 2) + np.power(Y1 + xr, 2)) / (self.lambda_ * self.z0) + self.shift
        sphericalWave = np.exp(1j * phi)
        # 相位物体

        if self.flag == 1:
            wave = planeWave
        elif self.flag == 0:
            wave = sphericalWave
        else:
            wave = phaseObject
        return wave

    def record(self, raw_img):
        pad_img = self.zero_padding(raw_img)
        object_ = self.fresnel(pad_img)
        refer_ = self.wave(pad_img)
        w1 = object_ + 0.5 * refer_
        w1 = np.power(np.abs(w1), 2)  # 求出全息平面上的强度分布
        return w1

    def reconstruct(self, holo_img, RoomNo=10):
        # image processing
        holo_img = holo_img - np.mean(holo_img)
        U0 = self.fresnel(holo_img, False)

        Gmax = np.max(np.abs(U0))
        Gmin = np.min(np.abs(U0))
        U1 = np.abs(U0)
        U1 = (U1 - Gmin) / (Gmax / RoomNo - Gmin)
        return U1

    def format_img(self, img):
        img = img ** 0.5
        format_img = img * 255
        format_img = format_img.astype(np.uint8)
        return format_img


if __name__ == "__main__":
    # input the image path
    image_path = "../Res/Set5/GTmod12/butterfly.png"
    g = Image.open(image_path, mode="r")
    # convert RGB image to Gray image
    g = g.convert("L")
    plt.figure(1)
    plt.imshow(g, cmap="gray")
    G = np.array(g)

    # flag=0: 球面波
    # flag=1: 平面波
    # 其他: 物体相位
    fresnel = Fresnel(flag=0)
    # 全息记录
    holo = fresnel.record(G)
    print(holo.shape, holo)
    plt.figure(2)
    plt.imshow(holo, cmap="gray")
    holo_show = Image.fromarray(fresnel.format_img(holo)).convert("L")
    holo_show.save("./result/fre_butterfly_CGH.bmp", "bmp")
    # 全息再现
    recon_img = fresnel.reconstruct(holo)
    recon_img = fresnel.format_img(recon_img)
    print(recon_img.shape, recon_img)
    plt.figure(3)
    plt.imshow(recon_img, cmap="gray")
    recon_img_show = Image.fromarray(recon_img).convert("L")
    recon_img_show.save("./result/fre_butterfly_recover.bmp", "bmp")

    plt.show()

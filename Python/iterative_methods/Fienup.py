from PIL import Image
import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
import matplotlib.pyplot as plt
from tqdm import tqdm


class Fienup:
    def __init__(self, image, step_size):
        self.raw_image = np.array(image)
        self.width, self.height = self.raw_image.shape[0], self.raw_image.shape[1]
        self.amplitude = self.norm_amplitude()
        self.phase = 2 * np.pi * np.random.rand(self.width, self.height)
        self.step_size = step_size  # 设置反馈参量，范围为[0,1]，step_size=0时为GS算法
        # 初始复振幅
        self.complex_amplitude = self.amplitude * np.exp(1j * self.phase)
        self.RMSE = None
        # 相位全息
        self.phase_result = None
        self.result = None

    def norm_amplitude(self):
        return self.raw_image / np.max(self.raw_image)

    def train(self, epoch=500):
        self.RMSE = np.zeros(epoch)
        for i in tqdm(range(epoch)):
            # 逆傅立叶变换到频域
            freq_img = ifft2(fftshift(self.complex_amplitude))
            # 取相位值, 频域作全1幅值约束，相位全息图
            # f_img_norm = 1 * freq_img / np.abs(freq_img)
            f_img_phase = np.angle(freq_img)
            f_img_norm = self.amplitude * np.exp(1j * f_img_phase)
            # 作傅里叶变换返回空域
            space_img = fft2(fftshift(f_img_norm))
            error = np.abs(self.amplitude) - fftshift(np.abs(space_img) / np.max(space_img))
            self.RMSE[i] = np.sqrt(np.mean(np.power(error, 2)))
            # 引入反馈调节
            self.complex_amplitude = np.abs(self.amplitude + error * self.step_size) * (space_img / np.abs(space_img))

        self.phase_result = np.abs(f_img_phase)
        self.result = np.abs(fftshift(space_img))

        plt.figure(0)
        plt.imshow(self.raw_image, cmap="gray")
        # 相位原件分布
        plt.figure(1)
        plt.imshow(self.phase_result, cmap="gray")
        # 模拟衍射输出
        plt.figure(2)
        plt.imshow(self.format_image(self.result), cmap="gray")
        plt.figure(3)
        plt.plot(list(range(epoch)), self.RMSE)
        plt.show()

    def format_image(self, img):
        img = img * 255 / np.max(img)
        img = img.astype(np.uint8)
        return img


if __name__ == "__main__":
    image_path = "../../Res/image256/lena.png"
    g = Image.open(image_path, mode="r")
    # convert RGB image to Gray image
    g = g.convert("L")
    # Resize
    g = g.resize((512, 512), Image.BILINEAR)
    # G = np.array(g)
    fien = Fienup(g, 0.2)
    fien.train()


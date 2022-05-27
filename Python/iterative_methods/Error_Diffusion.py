import cv2 as cv
import copy
import math
from matplotlib import pyplot as plt

img = cv.imread("../../Res/image256/lena.png")  # image to perform processing on
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # converting to grayscale
cv.imshow("Original Image", grayimg)
cv.waitKey(0)

compression_rate = 64  # 4 Quantization levels

# Reducing color range without error diffusion
without_err_diffuse = copy.deepcopy(grayimg)
for row in range(len(without_err_diffuse)):
    for col in range(len(without_err_diffuse[0])):
        oldpixel = without_err_diffuse[row][col]
        newpixel = math.floor(oldpixel / compression_rate)
        without_err_diffuse[row][col] = newpixel * compression_rate

cv.imshow("Without Dithering", without_err_diffuse)
cv.waitKey(0)

sum1 = 0
sum2 = 0

# Reducing color range with error diffusion
with_err_diffuse = copy.deepcopy(grayimg)
for i in range(len(with_err_diffuse)):
    for j in range(len(with_err_diffuse[0])):
        oldpixel = with_err_diffuse[i][j]
        newpixel = math.floor(oldpixel / compression_rate)
        with_err_diffuse[i][j] = newpixel * compression_rate
        error = oldpixel - with_err_diffuse[i][j]
        if (j + 1) < len(with_err_diffuse[0]):
            with_err_diffuse[i][j + 1] = with_err_diffuse[i][j + 1] + (
                        error * (7 / 16))  ##error diffused to right pixel
        if (i + 1) < len(with_err_diffuse) and (j - 1) >= 0:
            with_err_diffuse[i + 1][j - 1] = with_err_diffuse[i + 1][j - 1] + (
                        error * (3 / 16))  ##error diffused to bottom left pixel
        if (i + 1) < len(with_err_diffuse):
            with_err_diffuse[i + 1][j] = with_err_diffuse[i + 1][j] + (
                        error * (5 / 16))  ##error diffused to bottom pixel
        if (i + 1) < len(with_err_diffuse) and (j + 1) < len(with_err_diffuse[0]):
            with_err_diffuse[i + 1][j + 1] = with_err_diffuse[i + 1][j + 1] + (
                        error * (1 / 16))  ##error diffsued to bottom right pixel

cv.imshow("After Floyd Steinberg Dithering ", with_err_diffuse)
cv.waitKey(0)
cv.destroyAllWindows()

# Histograms of all three images
plt.hist(grayimg.ravel(), 256, [0, 256])
plt.title("Original image")
plt.show()

plt.hist(without_err_diffuse.ravel(), 256, [0, 256])
plt.title("Image: without error diffusion")
plt.show()

plt.hist(with_err_diffuse.ravel(), 256, [0, 256])
plt.title("Image: with error diffusion")
plt.show()

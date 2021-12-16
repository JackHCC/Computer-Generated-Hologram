# Computer-Generated-Hologram
✨This library introduces the current production process of computer holography, and uses MATLAB and Python to record and reproduce holograms. In the future, I will build a computer hologram simulation framework or a simulation application program.



## Introduction

CGH stands for computer-generated holograms (CGH). Holograms are unique in their ability to record both the intensity and phase of information.

|                          CGH Class                           |                  Document                   | Link |
| :----------------------------------------------------------: | :-----------------------------------------: | :--: |
| Circuitous Phase Type Hologram/Fourier Hologram【迂回位相型全息图】 |   👉[Doc](Doc/Fourier_Hologram/README.md)    | Code |
|                      Kinoform【相息图】                      |       👉[Doc](Doc/Kinoform/README.md)        | Code |
|               Fresnel Hologram【菲涅尔全息图】               |                    👉Doc                     | Code |
|       Off Axis Interference Hologram【离轴干涉全息图】       | 👉[Doc](Doc/Interference_Hologram/README.md) | Code |



## Usage

Working on a hologram simulation API.

Please wait!



## Experiment

### Before Experiment

Before experimenting, it's best to understand common image formats and their fundamentals. Understanding the pixel level of an image will help you experiment better and give you a better understanding of the fundamentals of image processing.

Here are some examples of images you should pay more attention to the suffix of the image, and the size of the image, so that you can work with the image later.

![64×64-test.bmp](./Res/image64/test.bmp)

<img src="./Res/image256/lena.png" alt="256×256-lena.png" style="zoom:50%;" />

### Fourier Hologram

Circuitous Phase Type Hologram/Fourier Hologram is Binary hologram.

#### DataSet

For this experiment we used this image for testing

![64×64-test.bmp](./Res/image64/test.bmp)

#### Experimental Principle

Please read this [Doc](Doc/Fourier_Hologram/README.md)ument.

#### Experimental Procedure

Two ways to do experiments are provided here, Matlab or Python, and you can choose the familiar way to run the code.

- Run the `fourier_hologram.m` or `fourier_hologram.py`, They are in the Python and Matlab folders respectively.
- Then you will get Circuitous Phase Type Hologram/Fourier Hologram below.

![](./Matlab/result/fh_test_CGH.bmp)

+ Finally, after running the program, you can get the reproduced graph and compare it with the original image.

![](./Matlab/result/fh_test_recover.bmp)

### Kinoform

#### DataSet

For this experiment we used this image for testing

![256×256-lena.png](./Res/image256/lena.png)

#### Experimental Principle

Please read this [Doc](Doc/Kinoform/README.md)ument.

#### Experimental Procedure

Two ways to do experiments are provided here, Matlab or Python, and you can choose the familiar way to run the code.

- Run the `kinoforms.m` or `kinoforms.py`, They are in the Python and Matlab folders respectively.
- Then you will get Kinoform below.

![](./Python/result/ki_lena_CGH.bmp)

- Finally, after running the program, you can get the reproduced graph and compare it with the original image.

![](./Python/result/ki_lena_recover.bmp)

### Off Axis Interference Hologram

#### DataSet

For this experiment we used this image for testing

<img src="./Res/imageO/pku.jpg" style="zoom:50%;" />

#### Experimental Principle

Please read this [Doc](Doc/Interference_Hologram/README.md)ument.

#### Experimental Procedure

Two ways to do experiments are provided here, Matlab or Python, and you can choose the familiar way to run the code.

- Run the `offaxis_interference_hologram.m` or `offaxis_interference_hologram.py`, They are in the Python and Matlab folders respectively.
- Then you will get Off Axis Interference Hologram below.

![](./Python/result/oaih_pku_CGH.bmp)

- Finally, after running the program, you can get the reproduced graph and compare it with the original image.

![](./Python/result/oaih_pku_recover.bmp)



## Contact

If you have any questions or good ideas, please contact: jackcc0701@163.com




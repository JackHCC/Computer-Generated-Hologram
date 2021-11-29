clear;
close all;

x32=4;
y32=4;
s=64*8;
g=imread ('../Res/image64/test.bmp');

%G=Rgb2gray (g);
G=g;
G=im2double (G);
[p q]=size(G); %p, q图像的像素
Z=G;
R1=rand(p);
A=Z.*exp(i*2*pi*R1);%乘以单位振幅的随机指数函数，平滑傅里叶变换

A=fftshift(fft2(fftshift(A)));%fftshift的作用正是让正半轴部分和负半轴部分的图像分别关于各自的中心对称
figure, imshow (A);

A1=abs(A);%求绝对值
B1=mod(angle(A),2*pi)/(2*pi);%取模运算
C=max(max(A1));%求出矩阵的最大元素

A2=s/p;
B2=A2;
Z=zeros(s,s);

for I=1:p
    y0=y32+(I-1)*B2;
    for J=1:q
        x0= x32+(J-1)*A2; 
        H=round(A1(I,J)*B2/C); %矩空高度
        F1=round(B1(I,J)*A2); %中心偏离值
        W=A2/2; %矩形宽度
        x1=round (x0+F1-W/2);
        x2=x1+W-1;
        y1=round (y0-H/2+0.5);
        y2=y1+H-1;
 
        if x2<J*A2
            Z(y1:y2,x1:x2)=1;
        else
            Z(y1:y2,x1:J*A2)=1;
            Z(y1:y2,(J-1)*A2+1:x2-A2)=1;
        end
    end
end

figure, imshow(Z);

P=fftshift(ifft2(Z));
figure, imshow(abs(P)*256);

P1=P(s/2-128+1:s/2+128,s/2-128+1:s/2+128);
figure, imshow(abs(P1)*256);

imwrite(Z,'./result/fh_test_CGH.bmp');
imwrite(Z(s/2-64+1:s/2+64,s/2-64+1:s/2+64),'./result/fh_test_larger_CGH.bmp');
imwrite(abs(P1)*255,'./result/fh_test_recover.bmp');


clear;
close all;
%% 选择图片路径并读取现实
chemin='.\images\';     %图片选择默认路径
[nom,chemin]=uigetfile([chemin,'*.*'],['调入模拟物体图像'],256,256);    %在文件夹中选择路径
[XRGB,MAP]=imread([chemin,nom]);    %获取图像
figure,imshow(XRGB);    %显示图像
isRGB = 0;     %如果是RGB，该变量置为1，否则，置为0
if isRGB==0
    X0=XRGB;    %灰度图直接处理
else
    X0=rgb2gray(XRGB);  %彩色图像转换为灰度图像
end
figure,imshow(X0,[]);       %显示选择的图像

%% 基础参数设置
[M0,N0]=size(X0);	%获取灰度图像的像素数大小
N1=min(M0,N0);
N=1080;     %相息图取样数, 可按需要修改
m0=0.5;      %图像在重建周期中的显示比例, 
%m0=input('图像在重建周期中的显示比例(0->1)');    %动态输入的话打开注释
X1=imresize(X0,N/N1*m0);
[M1,N1]=size(X1);
X=zeros(N,N);
X(N/2-M1/2+1:N/2+M1/2,N/2-N1/2+1:N/2+N1/2)=X1(1:M1,1:N1);

h=0.532e-3;      %波长(mm), 可按需要修改
k=2*pi/h;
pix=0.0064;      %SLM像素宽度(mm), 可按需要修改
L=N*pix;         %SLM宽度(mm)
z0=1200;          %----衍射距离(mm),
%z0=input('衍射距离(mm)');   %衍射距离如果需要动态设置，打开注释
L0=h*z0/pix;      %重建像平面宽度(mm)
Y=double(X);
a=ones(N,N);
b=rand(N,N)*2*pi;
U0=Y.*exp(1i.*b);  %叠加随机相位噪声,形成振幅正比于图像的初始场复振幅
X0=abs(U0);       %初始场振幅,后面叠代运算用
figstr=strcat('SLM平面宽度=',num2str(L),'mm');
figstr0=strcat('初始物平面宽度=',num2str(L0),'mm');
figure(1),imshow(X,[]),colormap(gray); xlabel(figstr);title('物平面图像');
np=0;
%np=input('叠代次数');   %迭代次数需要次数动态设置，打开注释

%% 梅涅尔衍射的计算
for p=1:np+1    %叠代次数
    %菲涅耳衍射的S-FFT计算开始,相息图记录
    n=1:N;
    x=-L0/2+L0/N*(n-1);	 					
    y=x;
    [yy,xx] = meshgrid(y,x); 
    Fresnel=exp(1i*k/2/z0*(xx.^2+yy.^2));
    f2=U0.*Fresnel;
    Uf=fft2(f2,N,N);
    Uf=fftshift(Uf);
    x=-L/2+L/N*(n-1);%SLM宽度取样(mm) 					
    y=x;
    [yy,xx] = meshgrid(y,x); 
    phase=exp(1i*k*z0)/(1i*h*z0)*exp(1i*k/2/z0*(xx.^2+yy.^2));
    Uf=Uf.*phase;
    %菲涅耳衍射的S-FFT计算结束
    figstr=strcat('SLM宽度=',num2str(L),'mm');
    figure(2),imshow(abs(Uf),[]),colormap(gray); xlabel(figstr);title('到达SLM平面的物光振幅分布');
    Phase=angle(Uf)+pi;
    Ih=uint8(Phase/2/pi*255);%形成0-255灰度级的相息图
    figure(3),imshow(Phase,[]),colormap(gray); xlabel(figstr);title('相息图');
    %菲涅耳衍射的S-IFFT计算开始，相息图重建
    U0=cos(Phase-pi)+1i*sin(Phase-pi);
    n=1:N;
    x=-L/2+L/N*(n-1);	 					
    y=x;
    [yy,xx] = meshgrid(y,x); 
    Fresnel=exp(-1i*k/2/z0*(xx.^2+yy.^2));
    f2=U0.*Fresnel;
    Uf=ifft2(f2,N,N);
    x=-L0/2+L0/N*(n-1); %SLM宽度取样(mm) 					
    y=x;
    [yy,xx] = meshgrid(y,x); 
    phase=exp(-1i*k*z0)/(-1i*h*z0)*exp(-1i*k/2/z0*(xx.^2+yy.^2));
    Uf=Uf.*phase;
    figure(4),imshow(abs(Uf),[]),colormap(gray); xlabel(figstr0);title('逆运算重建的物平面振幅分布');
    %保持相位不变，引用原图振幅，重新开始新一轮计算
    Phase=angle(Uf);
    U0=X0.*(cos(Phase)+1i*sin(Phase));
end

%figure(5),imshow(Ih,[]),colormap(gray); xlabel(figstr);title('相息图');

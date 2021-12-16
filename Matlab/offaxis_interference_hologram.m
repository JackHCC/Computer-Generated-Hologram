%           h ——波长（mm）；          I ——数字全息图；
%           L ——全息图宽度（mm）；    z0——记录全息图的距离(mm)；
%% Image Read and preprocess
XRGB=imread('./images/pku.jpg');
X0=rgb2gray(XRGB);
% figure,imshow(X0,[]);
[M0,N0]=size(X0);

%% Set Basic parameters
N1=min(M0,N0);
N=1024;          %模拟形成的全息图取样数
X1=imresize(X0,N/4/N1);
[M1,N1]=size(X1);
X=zeros(N,N);
X(N/2-M1/2+1:N/2+M1/2,N/2-N1/2+1:N/2+N1/2)=X1(1:M1,1:N1);
h=0.632e-3;      %波长(mm), 可按需要修改
k=2*pi/h;
% CCD：Charge Coupled Device（电荷耦合元件），是一种将图像转换为电信号的半导体元件。由类似棋盘的格状排列的小像素 (pixel) 组成。
pix=0.00465     ;%CCD像素宽度(mm), 可按需要修改
L=N*pix;         %CCD宽度(mm)
z0=1000;         %衍射距离(mm), 可按需要修改
L0=h*N*z0/L;     %物平面宽度(mm)
Y=double(X);
%a=ones(N,N);
b=rand(N,N)*2*pi;
f=Y.*exp(1i.*b);  %叠加随机相位噪声,形成振幅正比于图像的初始场复振幅

figstr=strcat('初始物平面宽度=',num2str(L0),'mm');
figure(1),imshow(X,[]),colormap(gray); xlabel(figstr);title('物平面图像');

%% Fresnell 
%---------------菲涅耳衍射的S-FFT计算开始
n=1:N;
x=-L0/2+L0/N*(n-1);	 					
y=x;
[yy,xx] = meshgrid(y,x); %网格化数据平面
Fresnel=exp(1i*k/2/z0*(xx.^2+yy.^2));
f2=f.*Fresnel;
Uf=fft2(f2,N,N);
Uf=fftshift(Uf);
x=-L/2+L/N*(n-1);   %CCD宽度取样(mm) 					
y=x;
[yy,xx] = meshgrid(y,x); 
phase=exp(1i*k*z0)/(1i*h*z0)*exp(1i*k/2/z0*(xx.^2+yy.^2));%菲涅耳衍射积分前方的相位因子
Uf=Uf.*phase;
%---------------S-FFT计算结束
figstr=strcat('模拟CCD宽度=',num2str(L),'mm');
figure(2),imshow(abs(Uf),[]),colormap(gray); xlabel(figstr);title('到达CCD平面的物光振幅分布');

%% Reference Light
%---------------形成0-255灰度级的数字全息图
fex=N/L;
Qx=(4-2.5)*L0/8/z0;          %按照优化设计定义参考光方向余弦
Qy=Qx;
x=[-L/2:L/N:L/2-L/N];
y=x;
[X,Y]=meshgrid(x,y);
Ar=max(max(abs(Uf)));        %按物光场振幅最大值定义参考光振幅
Ur=Ar*exp(1i*k*(X.*Qx+Y.*Qy));%参考光复振幅

%% Interference
Uh=Ur+Uf;                    %物光与参考光干涉
Wh=Uh.*conj(Uh);             %干涉场强度
Imax=max(max(Wh));
I=uint8(Wh./Imax*255);      %形成0-255灰度级的数字全息图
Ih=I;
imwrite(I,'./Ih.bmp');     %形成数字全息图文件
figstr=strcat('全息图宽度=',num2str(L),'mm');
figure(3),imshow(Ih,[]),colormap(gray);xlabel(figstr);title('模拟形成的数字全息图');

%% Reconstruction
%基于S-FFT的全息重建
f0 = double(Ih);
[N1,N2]=size(f0);
N=min(N1,N2);                      
h=0.000632;             %波长(mm)              
z0=1000;
L=N*pix;                %CCD宽度(mm)                        
In(1:N,1:N)=f0(1:N,1:N);
%-----------------------------1-FFT重建开始
n=1:N;
x=-L/2+L/N*(n-1);	 					
y=x;
[yy,xx] = meshgrid(y,x); 
k=2*pi/h;	
Fresnel=exp(1i*k/2/z0*(xx.^2+yy.^2));
f2=In.*Fresnel;
Uf=fft2(f2,N,N);
Uf=fftshift(Uf);
L0=h*z0*N/L;
x=-L0/2+L0/N*(n-1);	 					
y=x;
[yy,xx] = meshgrid(y,x); 
phase=exp(1i*k*z0)/(1i*h*z0)*exp(1i*k/2/z0*(xx.^2+yy.^2));
U0=Uf.*phase;   %积分运算结果乘积分号前方相位因子
%-----------------------------1-FFT重建结束
If=U0*conj(U0);
Gmax=max(max(abs(U0)));
Gmin=min(min(abs(U0)));
figstr=strcat('重建物平面宽度=',num2str(L0),'mm');
figure(4),
imshow(abs(U0),[Gmin Gmax/1]),colormap(gray); xlabel(figstr);title('1-FFT物平面重建图像');

%% Light intensity change
p=10;
while p
    figure(5);
    imshow(abs(U0),[Gmin Gmax/p]),colormap(gray);xlabel(figstr);title('1-FFT物平面重建图像');
    p=input('Gmax/p,p=10?');
end
Up=fft2(U0);
figure(6),imshow(abs(Up),[])
figure(7),plot(abs(Up(round(512)+1,:)));
hold on;

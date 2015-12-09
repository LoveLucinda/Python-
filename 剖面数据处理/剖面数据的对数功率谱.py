# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl  
# 基本的剖面数据对数功率谱求取
# 0. Input parameter
filename=u"I:\\Research\\1-EMD in Marine ravity\\DATA\\ExtractData\\点距规则化+功率谱\\2014_029.S-162-提取测线2_距离_规则化5.dat"
startrow=1      #数据开始的行号
colnum_x=0      #x的列号
colnum_y=6      #y的列号
#_________________________________________________________________________________________________________________________________

# 1. read data
AllData=np.loadtxt(filename,dtype=np.str,delimiter="\t")

# 2. extract data
x=AllData[startrow:,colnum_x].astype(np.float)
y=AllData[startrow:,colnum_y].astype(np.float)
longitude=AllData[startrow:,1].astype(np.float)

# 3. plot raw data
pl.figure(figsize=(16,8)) 
pl.subplot(211)
pl.plot(longitude,y)
pl.xlabel("Longitude(degree)")
pl.ylabel("Etovos Correction (mGal)")
pl.title("One gravity profile from SWIR")

# 4. get power spectrum of the data
fftsize=len(x)
xs=y[:fftsize]
xf=np.fft.rfft(xs)/fftsize
sampling_rate=1.0/x[len(x)-1]
freqs = np.linspace(0, sampling_rate/2, fftsize/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

# 5. plot spectrum
pl.subplot(212)
pl.plot(freqs, xfp)
pl.xlabel(u"Frequency(Hz)")
pl.ylabel("Log Power spectrum")
pl.subplots_adjust(hspace=0.4)
pl.show()

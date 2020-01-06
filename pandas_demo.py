# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:40:03 2019

@author: libozhang
"""

import numpy as np
import pandas as pd
import matplotlib as plt
s=pd.Series([1,2,3,6,np.nan,9,12])
print(s)
dates=pd.date_range('20190809',periods=10)
print(dates)

df1=pd.DataFrame({"A":pd.date_range("20190821",periods=4),
              "B":pd.Series(1, index=list(range(4)), dtype='float32'),
              "C":1.,
              "D":np.array([3] * 4, dtype='int32'),
              "E":pd.Categorical(["test", "train", "test", "train"]),
              "F":'foo'})
df=pd.DataFrame(np.random.randn(10,10),index=dates,columns=list("ABCDEFGHIJ"))
print(df1)
print(df1.dtypes)
print(df1.head(2))
print(df1.tail(3))
print(df1.index)
print(df1.columns)
print(df1.to_numpy())
print(df.describe())
print(df.loc[dates[0:3],['A','B','C']])
print(df.iloc[3])
print(df[df.A>0])

ts=pd.Series(np.random.randn(1000),index=pd.date_range('20190809',periods=1000))
ts=ts.cumsum()
ts.plot()
df4=pd.DataFrame(np.random.randn(1000,5),index=ts.index,columns=list('ABCDE'))
df=df.cumsum()
df4.plot()


df4.to_csv("SAVE2019_8_21_14-13-57.csv")
df4.to_excel("testdata.xlsx")
csv11=pd.read_csv("SAVE2019_8_21_14-13-57.csv")

xls=pd.read_excel("testdata.xlsx",index_col=None,na_value=['NA'])
print(csv11)
print(xls)


#%%matplotlib

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 250

ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-10, 15, 0.1)
Y = np.arange(-10, 15, 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(2*X**2 + 5*Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()



#%%open file

with open('d:\\pycodes\\demofile.txt','w') as f:
    f.write('hello world')

print(f)
#%%pandas
 import numpy as np
 import pylab as pl
 import scipy as sp
 x=np.linspace(-np.pi,np.pi,512)
 s=np.sin(x)
 s1=np.cos(x)
 pl.title("tr function")
 pl.xlabel("X")
 pl.ylabel("Y")
 pl.plot(x,s)
 pl.plot(x,s1)
 lista=sp.ones(500)
 lista[200:300]=-1
 f=sp.fft(lista)
 pl.plot(f)
 
#%%Pillow 图像操作的框架
 
from PIL import Image
im1=Image.open('snake.png')
print(im1.size,im1.format,im1.mode)
Image.open('snake.png').save('test.png')
im2=Image.open("test.png")
size=(288,180)
im2.thumbnail(size)
out=im2.rtate(45)
im1.paste(out,(50,50))

#%%读取csv文件并画图
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter

df=pd.read_excel('D:\\python\\ad.xlsx')
df1=df[1:][:]
df3=df2[0:100]
print(df1)
print(df2)
df2.plot(figsize=(10,5))
df['A'].plot(figsize=(10,5))
df1.B.plot(kind='barh')

workbook=xlsxwriter.Workbook("d:testdemo.xlsx")
worksheet=workbook.add_worksheet()
worksheet.set_column('A:A',20)
bold=workbook.add_format({'bold':1})
worksheet.write('A1','hello')
worksheet.write('A2',"python")
worksheet.write(4,1,2019)
worksheet.write(3,6,823)

#%%图形化工具

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df=pd.Series(np.random.randn(200),index=pd.date_range('2019/08/23',periods=200))
ts.plot()












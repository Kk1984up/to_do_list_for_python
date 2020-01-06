# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:37:55 2019

@author: libozhang
"""

import wordcloud
import jieba
txt="微创医疗是一家医疗器械产业集群"
w=wordcloud.WordCloud(width=1000,font_path="msyh.ttc",height=500)
w.generate("".join(jieba.lcut(txt)))
w.to_file("word.png")


#%%集合的使用

N=int(input("请输入一个整数:"))
n=str(N)
n1=set(n)
s=0
for i in n1:
    s=s+eval(i)

print(s)

#%%
import jieba
s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''

words=jieba.lcut(s)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(1):
    word,count=items[i]
    print("{}".format(word))
    
#%%
f = open("latex.log")
s, c = 0, 0
for line in f:
    line = line.strip("\n")
    if line == "":
        continue
    s += len(line)
    c += 1
print(round(s/c))

f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()    

#%%

s=input("请随机输入任何字符:")
t=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for line in s:
    if line in t:
        print(line,end="")
        
        
alpha = []
for i in range(26):
    alpha.append(chr(ord('a') + i))
    alpha.append(chr(ord('A') + i))
s = input()
for c in s:
    if c in alpha:
        print(c, end="")


s = input()
try:
    if complex(s) == complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")
    
#%%
    
import sys
print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(sys.getrecursionlimit(), sys.executable, sys.maxunicode))



from tabulate import tabulate
data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data, tablefmt="grid"))










    
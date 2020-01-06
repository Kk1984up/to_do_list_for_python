# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:40:00 2019

@author: libozhang
"""
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""
        
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('table').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string])


def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t"
    print(tplt.format("排名","名称"))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1])

def main():
    uinfo=[]
    url='http://www.smianet.com/hy.aspx'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,100)#打印100所学校的信息
main()
    
#%%最好大学排名定向爬虫实战
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[4].string])


def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        
    
def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/ARWU2019.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,100)#打印100所学校的信息
main()
    
#%%taobao‘price rank

import requests
import re

def getHTMLText(url):
    
    try:
        coo='miid=1349413379755444737; t=16724935fce051a87ebb95bf57059a2b; hng=CN%7Czh-CN%7CCNY%7C156; cna=mCgjFXCckDYCATogBIYCoXLC; thw=cn; lgc=%5Cu51AC%5Cu5929%5Cu7684%5Cu5C0F%5Cu732B1991; tracknick=%5Cu51AC%5Cu5929%5Cu7684%5Cu5C0F%5Cu732B1991; tg=0; enc=bAKPzM0%2Fk9DnBG%2BmYHQpMDHYaMRm7kOtMwudC6AwSovA3VhRERVS427KWYgkm5a0ICT7vJ%2FAFHaEb%2BxwSxW3Ig%3D%3D; mt=ci=85_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _m_h5_tk=95330f2862b3254866c70f080ba7866c_1565979262854; _m_h5_tk_enc=22111eae6326a0ab936058ad344ca803; v=0; cookie2=1f37a20f44a314d9ca0082e5d57fe638; _tb_token_=f5e3b6776bbe3; unb=801755480; uc3=nk2=1VH21glvtq0C6xfCd5M%3D&lg2=URm48syIIVrSKA%3D%3D&id2=W8nVFJPVabe7&vt3=F8dBy3K7kTKh4GVoSyY%3D; csg=d5e51763; cookie17=W8nVFJPVabe7; dnk=%5Cu51AC%5Cu5929%5Cu7684%5Cu5C0F%5Cu732B1991; skt=ca44d2bc98f5297c; existShop=MTU2NjMxNTMzNA%3D%3D; uc4=id4=0%40Wep393DLY3bN5S%2F3%2Ba%2BAeZY4guw%3D&nk4=0%40140wsOH7GxjhCbl09N361zt20uWaJ1KUrQ%3D%3D; publishItemObj=Ng%3D%3D; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=101; _nk_=%5Cu51AC%5Cu5929%5Cu7684%5Cu5C0F%5Cu732B1991; cookie1=U%2BJ8WFfIhez%2F2NEGIa2i%2FMWmMlgoDaQhp%2F9ltLgzhD8%3D; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTaHogqw%2F3lWg%3D%3D&tag=8&lng=zh_CN; isg=BDQ0Y11W1TtZ10H96YxbkkObBfJmpViSAX-FUs6VwL9COdSD9h0oh-r7uTFE2pBP; l=cBMDACsPqhKNnw7BBOCanurza77OSIRYYuPzaNbMi_5pA6TsNpbOkJF3SF96VjWd_U8B43SO_1J9-etkZPxMysK-g3fP.'
        cookies={}
        for line in coo.split(';'):
            name,value=line.strip().split('=',1)
            cookies[name]=value
        header={'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        r=requests.get(url,timeout=30,header=header,cookies=cookies)
        r.rasie_for_status()
        print(r.status_code)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""

def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print("")
        
def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
        
def main():
    goods="书包"
    depth=2
    start_url="https://s.taobao.com/search?q="+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
        printGoodsList(infoList)
        
main()
    
    

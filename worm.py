#coding:utf-8
from bs4 import BeautifulSoup
import re
import urllib.request as uP
htmlPath =r"http://www.bookben.com"
htmlText =uP.urlopen(htmlPath).read().decode("gbk")
Soup = BeautifulSoup(htmlText,"lxml")
categorys = Soup.select("#menu > ul.cr-menu > li > a")

#获取每个类别的链接
list1 = []
list2 = []
for category in categorys:
    path = htmlPath + category.get("href")
    name = category.get_text()
    list1.append(path)
    list2.append(name)
    uP.urlopen(htmlPath)
def huoqu(Soup,i):
    titles = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ")> dt > a")
    imgs = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ")> dd.imgdd > a > img")
    categorys = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ") > dd:nth-of-type(2)")
    authors = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ") > dd:nth-of-type(3)")
    sizes = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ") > dd:nth-of-type(4)")
    dates = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ") > dd:nth-of-type(5)")
    #每一个下载页面都在另外的页面，所以需要再打开一个页面，此时需要对新页面进行处理
    downs = Soup.select(
        "#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl:nth-of-type(" + str(i) + ") > dd.icon > a")

    new_down = str(str(downs[0]).split(" ")[1]).split("=")[1][1:-1]

    new_url = "http://www.bookben.com"+new_down

    Text = uP.urlopen(new_url).read().decode("gbk")
    new_Soup = BeautifulSoup(Text, "lxml")
    downs=new_Soup.select("#wrap > div.xiaotian > div.left > div:nth-of-type(2) > dl.yxjs > dd > ul > li:nth-of-type(2) > a")

    for title, img, category, author, size, date, down in zip(titles, imgs, categorys, authors, sizes, dates, downs):
        data = {

            "title": title.get("title"),
            "img": img.get("src"),
            "category": category.get_text(),
            "author": author.get_text(),
            "size": size.get_text(),
            "date": date.get_text(),
            "down": down.get("href"),
        }
        print(data)

#获取每个类别链接下的第一页的小说标题，图片，描述，下载地址，
for flag in range(1,len(list2)-1):
    count =2
    htmlText = uP.urlopen(list1[flag]).read().decode("gbk")
    Soup = BeautifulSoup(htmlText, "lxml")
    sum = len(Soup.select("#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl"))
    next1 =Soup.select("#wrap > div.xiaotian > div.left > div.nylr > div.ym > ul")
    print(list2[flag])
    for i in range(1, sum + 1):
        huoqu(Soup,i)
    last_page = int(str(next1[0].get_text()).split("\xa0")[2][2:])
    while count<=last_page:
        print("第",count,"页")
        url = list1[flag]+"index_"+str(count)+".html"
        htmlText = uP.urlopen(url).read().decode("gbk")
        Soup = BeautifulSoup(htmlText, "lxml")
        sum = len(Soup.select("#wrap > div.xiaotian > div.left > div.nylr > div.lblr > dl"))
        last_page = int(str(next1[0].get_text()).split("\xa0")[2][2:])
        for i in range(1, sum + 1):
            huoqu(Soup,i)
        count+=1
    print(count)





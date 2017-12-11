from bs4 import BeautifulSoup
import urllib.request as uP
import re
from imagemaster.models import  *
from down_test import down_img
dbList = [Image_RenXiang,Image_FengJing,Image_ShengTai,Image_JiShi,Image_ShengHuo,Image_LoMo,
          Image_GuanNian,Image_ShouJiSnap,Image_DaWu,Image_ChongWu,Image_MeiShi]

htmlURL =r"http://photo.poco.cn/like/index-upi-tpl_type-hot.html#list"
htmlText =uP.urlopen(htmlURL).read().decode("gbk")

Soup = BeautifulSoup(htmlText,"lxml")
cate = Soup.select("#list > div.item-title.border-color2.color2.clearfix > ul > li")
cateList =[]
for mystr in cate[::2]:
    pat = re.compile('<a class="click" href="(.*?)">(.*?)</a></li>')
    cateList.append(re.findall(pat,str(mystr))[0])
print(len(cateList))
for i in range(len(cateList)-1):

    htmlURL = 'http://photo.poco.cn/like/'+cateList[i][0]
    htmlText = uP.urlopen(htmlURL).read().decode("gbk")
    Soup = BeautifulSoup(htmlText, "lxml")
    pageNum = Soup.select("#list > div.page.f-tdn.color2.tc > a:nth-of-type(10)")
    print(cateList[i][1])
    for NUM in pageNum:
        length =int(NUM.get_text())
        for k in range(1,20):
            newURL ='http://photo.poco.cn/like/index-upi-p-'+str(k)+'-tpl_type-hot-channel_id-0.html#list'
            htmlText = uP.urlopen(newURL).read().decode("gbk")
            Soup = BeautifulSoup(htmlText, "lxml")
            imagesNum = Soup.select("#list > div.mod-txtimg145-list.f-tdn.white > ul > li > div.img-box > a")
            print("第"+str(k)+"页爬取完成")
            for everyOne in imagesNum:
                patten = re.compile("'(.*?)',145")
                pagetext = re.findall(patten,str(everyOne))
                print(pagetext[0])
                img_url = down_img(pagetext[0])
                db.session.add(dbList[i](img_url))
                db.session.commit()

                pass








"""
http://photo.poco.cn/like/
#list > div.page.f-tdn.color2.tc > a:nth-child(10)
http://photo.poco.cn/like/index-upi-p-1-tpl_type-hot-channel_id-0.html#list
#list > div.mod-txtimg145-list.f-tdn.white > ul > li:nth-child(1) > div.img-box > a
body > div.conntent > div > div.bannerWrap.pt15.pb15 > div > ul > li > div > div > div.pic
"""
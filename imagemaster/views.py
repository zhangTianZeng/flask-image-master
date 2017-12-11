#coding:utf-8
from imagemaster import app
from flask import render_template
from imagemaster.models import *
dbList = [Image_RenXiang,Image_FengJing,Image_ShengTai,Image_JiShi,Image_ShengHuo,Image_LoMo,
          Image_GuanNian,Image_ShouJiSnap,Image_DaWu,Image_ChongWu,Image_MeiShi]
@app.route("/")
def index():

    images_RenXiang = dbList[0].query.all()
    images_FengJing = dbList[1].query.all()
    images_ShengTai =dbList[2].query.all()
    images_JiShi = dbList[3].query.all()
    images_ChongWu = dbList[9].query.all()
    return render_template("index.html",images_RenXiang = images_RenXiang,images_FengJing = images_FengJing,images_ShengTai = images_ShengTai,images_JiShi = images_JiShi,
                           images_ChongWu = images_ChongWu)

@app.route("/single/")
def single():
    return render_template("single.html")

@app.route("/about/")
def about():
    return render_template("about.html")
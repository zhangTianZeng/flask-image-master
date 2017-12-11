#coding:utf-8
from imagemaster import db

class Image_RenXiang(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)
class Image_FengJing(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_ShengTai(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_JiShi(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_ShengHuo(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_LoMo(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_GuanNian(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_ShouJiSnap(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_DaWu(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_ChongWu(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)

class Image_MeiShi(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1024))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<IndexImage %d>" % (self.id)


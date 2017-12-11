#coding:utf-8
from imagemaster import db
from imagemaster.models import *
def init_database():

    db.drop_all()
    db.create_all()

if __name__=="__main__":
    init_database()
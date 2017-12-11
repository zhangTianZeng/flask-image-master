import re,uuid
import urllib.request
from imagemaster import app
from imagemaster.qiniusdk import qiniu_upload_file

def down_img(url):
    f = open("hello"+".jpg", 'wb')
    f.write((urllib.request.urlopen(url)).read())
    f.close()

    file_name = str(uuid.uuid1()).replace('-', '') + '.' +'jpg'
    url = qiniu_upload_file( file_name)
    return url
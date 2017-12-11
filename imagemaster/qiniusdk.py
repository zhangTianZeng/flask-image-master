#coding:utf-8

from qiniu import Auth,put_file
import os

#需要填写你的 Access Key 和 Secret Key
access_key = 'xxx'
secret_key = 'xxx'
#构建鉴权对象
q = Auth(access_key,secret_key)
#要上传的空间
bucket_name = 'xxx'
domain_prefix = 'xxx'
save_dir = 'D:/upload/'

def qiniu_upload_file(save_file_name):
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, save_file_name)

    ret, info = put_file(token ,save_file_name,"hello.jpg")
    #ret,info = put_stream(token,save_file_name,source_file.save,"qiniu",source_file.stream.tell())

    if info.status_code == 200:


        return domain_prefix +"/"+ save_file_name
    return None

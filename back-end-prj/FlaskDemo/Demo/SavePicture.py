'''
Created on 2018-8-30

@author: wuqi2
'''
import urllib
# 网络上图片的地址
#get head pic from  my.lenovo.com

from requests_ntlm import HttpNtlmAuth
import csv

# 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
import requests
from PIL import Image
from io import BytesIO
import time
import random


csv_reader = csv.reader(open("D:/workspace/Flask/username.csv"))
for row in csv_reader:
    #print(row[0]);
    img_src = 'http://my.lenovo.com/my/user%20photos/profile%20pictures/'+row[0]+'_lthumb.jpg';
    #img_src ='''https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535717589907&di=a33a6c5693dec4e143a8b595a19005eb&imgtype=0&src=http%3A%2F%2Fhc24.aipai.com%2Fuser%2F886%2F8353886%2F5628503%2Fcard%2F25501370%2F25501370_400.jpg'''
    #img_src2 ='http://my.lenovo.com/my/User Photos/Profile Pictures/lidm1_MThumb.jpg'
    #print(img_src)
#response = requests.get(img_src,cookies=cookies)
    try:
        response =requests.get(img_src,auth=HttpNtlmAuth('lenovo.com\\wuqi2','123!@#qwe'))
        #print('tyr')
        image = Image.open(BytesIO(response.content))

        #D:\Users\wuqi2\pyDemo\FlaskDemo\pic

        file_path='D:\\Users\\wuqi2\\pyDemo\\FlaskDemo\\pic\\'+row[0]+'.jpg'
        #print(file_path)
        image.save(file_path)
        time.sleep(random.randint(0,2))
    except:
        print(img_src)
        f = open('D:\\workspace\\Flask\\pic\\log.txt','a')
        f.write('\n'+img_src)
        f.close()
       
print('get image done')
#print(response)
#image = Image.open(BytesIO(response.content))
#image.save('D:\workspace\Flask\lidm1wwww.jpg')



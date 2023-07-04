import re
import urllib.request
import os
import time
import ssl
import random
path='C:/Users/GeekerWu/Desktop/manager/back-end-prj/tsvideo2/'
'''
#http://www.zzvips.com/article/211763.html参考
#m3u8url='https://a.ak-kk.com/20220807/lNWBpanM/hls/index.m3u8'
#replacestr='https://a.ak-kk.com/20220807/lNWBpanM/hls/'

#m3u8url='https://a.ak-kk.com/20220807/75UjY8HR/hls/index.m3u8'
#replacestr='https://vo1.123188kk.com/20220807/75UjY8HR/hls/'

#resourcelist 网络地址
m3u8url='https://a.ak-kk.com/20211013/lKXOtjpS/hls/index.m3u8'
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20211013/lKXOtjpS/hls/'

#秘汤巡游隐汤 秘湯めぐり 隠れ湯
m3u8url='https://a.ak-kk.com/20211211/X1n3IFrt/hls/index.m3u8'
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20211211/X1n3IFrt/hls/'
#目标文件名
filmname='秘汤巡游隐汤1'
m3u8url='https://a.ak-kk.com/20211211/e2J5yDxe/hls/index.m3u8'
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20211211/e2J5yDxe/hls/'
#目标文件名
filmname='秘汤巡游隐汤2'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://awslsn1.sisuoyun.com/81820210105/DM0908436/1000kb/hls/index.m3u8'
resoucesite='https://awslsn1.sisuoyun.com/81820210105/DM0908436/1000kb/hls/'
#key 中 resource对应地址串 替换成本地
replacestr='https://awslsn1.sisuoyun.com/81820210105/DM0908436/1000kb/hls/'
#目标文件名
filmname='Implicity'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://a.ak-kk.com/20220630/gCJSwRym/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite=''
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20220630/gCJSwRym/hls/'
#目标文件名
filmname='异世界性爱社团1'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://a.ak-kk.com/20220630/WgBNVJ6m/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite=''
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20220630/WgBNVJ6m/hls/'
#目标文件名
filmname='异世界性爱社团2'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://xiusebf1.com/20210804/CUuf7Xrq/1000kb/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://xiusebf1.com'
#key 中 resource对应地址串 替换成本地
replacestr='/20210804/CUuf7Xrq/1000kb/hls/'
#目标文件名
filmname='ImplicityII'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://a.ak-kk.com/20211013/qA7l0wDL/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite=''
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20211013/qA7l0wDL/hls/'
#目标文件名
filmname='翔平的实况转播成人频道'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://vod2.hjbfq1.com/20220501/CB0MZS16/1000kb/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://vod2.hjbfq1.com/'
#key 中 resource对应地址串 替换成本地
replacestr='/20220501/CB0MZS16/1000kb/hls/'
#目标文件名
filmname='超★痴女メイド!'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://vod2.hjbfq1.com/20220630/nUXbyFeP/1000kb/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://vod2.hjbfq1.com'
#key 中 resource对应地址串 替换成本地
replacestr='/20220630/nUXbyFeP/1000kb/hls'
#目标文件名
filmname='超★痴女メイド!2'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://bf1.maozyapi.com/20220119/49A5DEB58700C235/hls/1000k/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://bf1.maozyapi.com/20220119/49A5DEB58700C235/hls/1000k/'
#key 中 resource对应地址串 替换成本地
replacestr='/20220119/49A5DEB58700C235/hls/1000k/'
#目标文件名
filmname='给每天经过家门口的JK送奇怪玩具然后嘿嘿'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://xiusebf1.com/20220223/X6OHQ0WJ/2000kb/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://xiusebf1.com'
#key 中 resource对应地址串 替换成本地
replacestr='/20220223/X6OHQ0WJ/2000kb/hls/'
#目标文件名
filmname='催眠侄女'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://bf1.maozyapi.com/20210828/1AFA99E48507FAAE/hls/2000k/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://bf1.maozyapi.com/20210828/1AFA99E48507FAAE/hls/2000k/'
#key 中 resource对应地址串 替换成本地
replacestr='/20220223/X6OHQ0WJ/2000kb/hls/'
#目标文件名
filmname='パンチラティーチャー1'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://bf1.maozyapi.com/20210828/2A33688627A1E18B/hls/2000k/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://bf1.maozyapi.com/20210828/2A33688627A1E18B/hls/2000k/'
#key 中 resource对应地址串 替换成本地
replacestr='/20210828/2A33688627A1E18B/hls/2000k/'
#目标文件名
filmname='パンチラティーチャー2'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://a.ak-kk.com/20220902/j6HCXRZk/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite=''
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20220902/j6HCXRZk/hls/'
#目标文件名
filmname='榨精病栋3'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://play2.aibobofang.com/20220808/l1zm0V8P/1500kb/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite='https://play2.aibobofang.com'
#key 中 resource对应地址串 替换成本地
replacestr='/20220808/l1zm0V8P/1500kb/hls/'
#目标文件名
filmname='返场昨晚极品清纯学妹'

#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://play2.aibobofang.com/20220808/l1zm0V8P/1500kb/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite=''
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20220715/Okrzae1O/hls/'
#目标文件名
filmname='异世界迷宫里的后宫生活01'

'''




#https://huangzhongtv.com/vodplay/49886-1-1.html
m3u8url='https://a.ak-kk.com/20220721/MABjSPeQ/hls/index.m3u8'
#无网址list 需要添加 有网址置空
resoucesite=''
#key 中 resource对应地址串 替换成本地
replacestr='https://vo1.123188kk.com/20220721/MABjSPeQ/hls/'
#目标文件名
filmname='异世界迷宫里的后宫生活02'








# 下载m3u8文件
def getM3u8():
    #url = 'https://ycalvod.yicai.com/record/live/cbn/f292cab1-9106-43cb-ac55-ee425a7f3e7e.m3u8?auth_key=1642017157-0-0-5e333fdb1501fae08aa348a6ea164950&ycfrom=yicaiwww'
    headers = {
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Type':'application / vnd.apple.mpegurl',
        'Host':'a.ak-kk.com',
        'Origin':'https://kanju77.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    }
    req = urllib.request.Request(url=m3u8url, headers=headers)
    res = urllib.request.urlopen(req)
    con = res.read().decode('utf-8')
    #文件存成index.m3u8
    with open(f'tsvideo2\\my.m3u8', 'w', encoding='utf-8') as fp:
        fp.write(con)

# 通过m3u8找到ts文件的路径
def getUrlOfTs():
    #with open(f'tsvideo2\\my.m3u8', 'r', encoding='utf-8') as fp:
    #support continue
    with open(f'tsvideo2\\Urllist.txt', 'r', encoding='utf-8') as fp:
        con = fp.read()
        # print(con)
        '''
        #support http://xxxx.ts
        tmps = re.finditer(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', con)
        urls = []
        filedata=""
        for i in tmps:
            # print('i',i.group())
            if i.group().find('key.key') > 0:
                print('key', i.group())
                tsUrl = i.group()
                urls.append(tsUrl)
                filedata+=f"{tsUrl}\n"
            else:
                tsUrl = i.group()
                urls.append(tsUrl)
                filedata += f"{tsUrl}\n"
        print(urls)
        with open(f'tsvideo2\\Urllist.txt',"w",encoding="utf-8") as f:
            f.write(filedata)
        '''
        #support none https  only xxx.ts
        tmps = re.finditer(r'.*.ts', con)
        #print(tmps)
        urls = []
        filedata = ""
        #urls.append(resoucesite +'/20220221/Kj3ItpHW/2000kb/hls/'+ 'key.key')
        for i in tmps:
            tsUrl = i.group()
            urls.append(resoucesite + tsUrl)
            filedata += f"{tsUrl}\n"
        print(urls)
        
        with open(f'tsvideo2\\Urllist.txt', "w", encoding="utf-8") as f:
            f.write(filedata)
        return urls



def alter(file,old_str,path):
    """https://blog.csdn.net/u012206617/article/details/121673782
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(f'tsvideo2\\{file}', "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,path)
            if 'key.key' in line:
                line = line.replace('key.key','key.m3u8')
            file_data += line
    with open(f'tsvideo2\\index.m3u8',"w",encoding="utf-8") as f:
        f.write(file_data)

    #os.rename("%s.bak" % file, 'index.m3u8')
'''
def alter2():
    """https://blog.csdn.net/u012206617/article/details/121673782
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(f'tsvideo2\\my.m3u8', "r", encoding="utf-8") as f:
        for line in f:
            if 'key.key' in line:
                line = line.replace('key.key', 'key.m3u8')
            expression = re.compile(r'.*.ts')
            line = expression.sub(path+line, line)
            file_data += line
    with open(f'tsvideo2\\index.m3u8', "w", encoding="utf-8") as f:
        f.write(file_data)

    #os.rename("%s.bak" % file, 'index.m3u8')

'''



# 下载ts文件
def loadTs(urls):
    num = 0
    endNum = 0
    for url in urls:
        print('ts url:',url)
        num = num + 1
        '''
        headers = {
            'Accept': '* / *',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'vo1.123188kk.com',
            'Origin': 'https://kanju77.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        
         headers = {
            'Accept': '* / *',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Host':'xiusebf1.com',
            'Origin':'https://cg-h.com',
            'Referer':'https://cg-h.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        
         headers = {
            'Accept': '* / *',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Host':'vo1.123188kk.com',
            'Origin':'https://cg-h.com',
            'Referer':'https://cg-h.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        headers = {
            'Accept': '* / *',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="105", "Google Chrome";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Host':'play2.aibobofang.com',
            'Origin':'https: // player.aibozyplayer.com',
            'Referer':'https: // player.aibozyplayer.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        '''
        headers = {
            'Accept': '* / *',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="105", "Google Chrome";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Host':'vo1.123188kk.com',
            'Origin':'https://kanju77.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }



        context=ssl._create_unverified_context()
        req = urllib.request.Request(url=url, headers=headers)
        try:
            res = urllib.request.urlopen(req,context=context)
        except:
            try:
                slpt = random.randrange(1, 5)
                print(f'except sleep {slpt}')
                time.sleep(slpt)
                res = urllib.request.urlopen(req)
            except:
                print(f'except sleep 2times {slpt}')
                time.sleep(slpt)
                res = urllib.request.urlopen(req, context=context)

        con = res.read()
        if url.find('key.key') > 0:
            title = 'key.m3u8'
        else:
            ##正则替换 删除网址留下文件名
            expression = re.compile(r'.*hls/')
            #expression = re.compile(r'.*2000k/')
            title = expression.sub('',url)
            #title = str(num) + '.ts'
        with open(f'tsvideo2\\{title}', 'wb') as fp:
            fp.write(con)
        print(str(num) + title + '下载完成~~~')
        file_data = ""
        with open(f'tsvideo2\\Urllist.txt', "r", encoding="utf-8") as f:
            for line in f:
                if f'{title}' in line:
                    print(f'{title} removed from urllist.txt')
                else:
                    file_data += line
            f.close()
        with open(f'tsvideo2\\Urllist.txt', "w", encoding="utf-8") as f:
            f.write(file_data)
            f.close()



    print('\n\n全部下载完成\n\n')
    return num


# 下载ts文件
def continueloadTs(urls):
    num = 0
    endNum = 0
    for url in urls:
        print('ts url:',url)
        num = num + 1
        headers = {
            #'referer': 'https://www.yicai.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        }
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        con = res.read()
        if url.find('key.key') > 0:
            title = 'key.m3u8'
        else:
            ##正则替换 删除网址留下文件名
            expression = re.compile(r'.*hls/')
            title = expression.sub('',url)
            #title = str(num) + '.ts'
        with open(f'tsvideo2\\{title}', 'wb') as fp:
            fp.write(con)
        print(str(num) + title + '下载完成~~~')
    print('\n\n全部下载完成\n\n')
    return num


# 合并ts文件
'''
def hebingTs(endNum):
    for i in range(1, endNum + 1):
        with open(filmname+'.mp4', 'ab+') as fp:
            fp.write(open(f'.\\tsvideo2\\{i}.ts', 'rb').read())
    print('合并完成！')
'''
def join_video():
    """
    利用ffmpeg合并加密的ts文件
    :param listname: 本地m3u8文件路径
    :param newfilename: 待合成的文件名称
    :return:
    """
    #command = f'ffmpeg -allowed_extensions ALL -i {listname} -c copy {newfilename}'
    #command1 = 'cd C:/Users/GeekerWu/Desktop/manager/back-end-prj/tsvideo2'

    command2 = f'ffmpeg -allowed_extensions ALL -i {path}index.m3u8 -c copy {path+filmname}.mp4'

    #command2 = f'ffmpeg - f concat - i file_list.txt - c copy {path+filmname}.mp4'

    #ffmpeg - f   concat - i   G:\\xing\\list.txt - c   copy   G:\\xing\\output.mp4

    #print(command1)
    print(command2)
    #os.system(command1)
    re = os.system(command2)
    time.sleep(2)
    if re == 0:
        print('合并成功')
    else:
        print('合并失败！！！！！！！！！！！！！！！！！！')

def join_video2():
    #support unscert stream
    filepath = "C:/Users/GeekerWu/Desktop/manager/back-end-prj/tsvideo2/"
    file_list = sorted(os.listdir(filepath))


    '''
    for file in file_list:
        file_data+=f"file '{path+file}'\n"
    with open(f'.\\tsvideo2\\file_list.txt',"w", encoding="utf-8") as f:
        f.write(file_data)
    '''


    file_data = ""
    with open(f'tsvideo2\\index.m3u8', "r", encoding="utf-8") as f:
        for line in f:
            if line.find('.ts') > 0:
                sourcestr=line.replace('\n', '')
                file_data +=f"file '{sourcestr}'\n"
    with open(f'tsvideo2\\file_list.txt', "w", encoding="utf-8") as f:
        f.write(file_data)

    command2 = f'ffmpeg -f concat -safe 0 -i {path}file_list.txt -c copy {path+filmname}.mp4'

    # ffmpeg - f   concat - i   G:\\xing\\list.txt - c   copy   G:\\xing\\output.mp4

    # print(command1)
    print(command2)
    # os.system(command1)
    re = os.system(command2)
    time.sleep(2)
    if re == 0:
        print('合并成功')
    else:
        print('合并失败！！！！！！！！！！！！！！！！！！')


#ffmpeg -allowed_extensions ALL -i index.m3u8 -c copy video.mp4


# 主函数
def main():

    # 获取 m3u8
    #getM3u8()
    # 编辑相对路径并另存为 index.m3u8
    #alter("my.m3u8",replacestr, path)
    #alter2()
    # 获取url list 和 key （key 改后缀名 .m3u8）

    urls = getUrlOfTs()
    #print(urls)
    endNum = loadTs(urls)
    print('endNum',endNum)
    '''
    join_video2()
    '''
    join_video()

    #hebingTs(endNum)


if __name__ == '__main__':
    main()
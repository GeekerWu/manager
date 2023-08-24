import requests
headers={
        'Accept':'*/*',
        'Accept-Encoding':'identity;q=1, *;q=0',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Cookie':'BAIDUID=509554C414A02F4538B7161F8EAD181C:FG=1; BAIDUID_BFESS=509554C414A02F4538B7161F8EAD181C:FG=1; BAIDU_WISE_UID=wapp_1690223441079_253; ZFY=x9iKarLAD8jyWAgmmuvvNGqIfO1bbGRBYLlTyzKvTok:C; BIDUPSID=509554C414A02F4538B7161F8EAD181C; PSTM=1690223442; jsdk-uuid=4007f89b-6f43-47f2-96b4-aad7cbc4806a; BA_HECTOR=a02g8k810ga1ag0ga58k00851ieatr71p; PSINO=2; H_PS_PSSID=36557_39226_39222_39097_39193_39199_26350_39138_39224_39137_39100; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1692759922; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1692760252; ab_sr=1.0.1_N2MzZDZkYjE2NDE3MjgyNGIwZDE2ODExYjJiYThlOTRkMmIxNTg1OGFjNWU5YjgxNjg1ZmM0NTIzYWQwOTgxNDNhYjVkZTkzOWU0MjFiOTI4MGI3YWQ4YzM3ZGY0N2YwYWNhNDk1ZTEzNjhlZTc3M2YxMzJiYjQ4N2NjZGZhZDUzM2RkM2I2ZGZlZjJjYmNkNTYzMmIyMzZjNGZiMDA3OQ==; SOUND_SPD_SWITCH=0; SOUND_PREFER_SWITCH=0',
        'Host':'fanyi.baidu.com',
        'Range':'bytes=0-',
        'Referer':'https://fanyi.baidu.com/translate?aldtype=16047&query=%E4%BD%A0%E5%A5%BD&keyfrom=baidu&smartresult=dict&lang=auto2jp',
        'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'audio',
        'Sec-Fetch-Mode':'no-cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
# url='https://fanyi.baidu.com/gettts?lan=jp&text=%E3%81%82%E3%82%8A%E3%81%8C%E3%81%A8%E3%81%86%E3%81%94%E3%81%96%E3%81%84%E3%81%BE%E3%81%99&spd=1&source=web'

url='https://dict.youdao.com/dictvoice?audio=%E3%81%8A%E3%81%AF%E3%82%88%E3%81%86%E3%81%94%E3%81%96%E3%81%84%E3%81%BE%E3%81%99&le=ja'
# res=requests.get(url,headers=headers)
res=requests.get(url)
print(res)
print(res.content)
'''
    with open("./voiceasset/ttstest.mp3", "wb") as file:
        file.write(res.content)
        file.flush()
'''


# import urllib
# print('1')
# h = urllib.request.urlopen("https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat143400050013&st=categoryid%24pcmcat143400050013&qp=&intl=nosplash")
# h2=urllib.request.urlopen("https://www.baidu.com")
# print('2')
# webcontent = h.read()
# print(webcontent)
# # h = urllib.request.urlopen(url)
# # webcontent = h.read()
# h.close()
# #if __name__ == '__main__':
import requests
url = "https://www.bestbuy.com"
s = requests.Session()
#52245=; tfs_upg=true

r = s.get('https://www.bestbuy.com', headers={'user-agent': 'Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Version\/11.0 Mobile\/15A372 Safari\/604.1'}) 

r2 = s.get('https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat143400050013&st=categoryid%24pcmcat143400050013&qp=&intl=nosplash', headers={'user-agent': 'Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Version\/11.0 Mobile\/15A372 Safari\/604.1'}) 

# ':path': '\/',
# ':scheme': 'https',
# 'accept': 'text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,image\/apng,*\/*;q=0.8',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
# 'cache-control': 'max-age=0',
# 'cookie': '52245=; tfs_upg=true',
# 'upgrade-insecure-requests': '1'
#,
#'user-agent': 'Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Version\/11.0 Mobile\/15A372 Safari\/604.1'

print(r2.content)
        



#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
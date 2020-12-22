'''
Created on 2020-4-28

@author: wuqi2
'''
import requests
url = "https://cn-api-test.lenovo.com/uat/token"

data = {"grant_type":"client_credentials"}
headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':'Basic UWJ2QnYzWHhsbGMzMFNfY1Byem9oeEpSRGZnYTpzTFJvdG1iX2ZFZjJUT1hiS2xMelY0ZFFLRFVh'
}
res = requests.post(url=url,data=data,headers=headers,verify=False)
print(res.text)
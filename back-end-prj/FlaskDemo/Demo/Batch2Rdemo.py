'''
Created on 2018-11-29

@author: wuqi2
'''


import subprocess
#cmd = 'cmd.exe c:\\sam.bat'
p = subprocess.Popen("cmd.exe /c" + "D:\\Users\\wuqi2\\Desktop\\ttt.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()
while(curline != b''):
    print(curline)
    curline = p.stdout.readline()
     
p.wait()
print(p.returncode)
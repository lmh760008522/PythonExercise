import requests
import webbrowser

#搜索的信息
param ={"wd":"刘美含"} 
r = requests.get("http://www.baidu.com/s",params=param) 
print(r.url)
webbrowser.open(r.url)

data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
print(r.text)

r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)
#coding = "utf-8"
import requests
import re
import time
import csv

#将citydata.text的数据读出来，传递给citydata

citydata = ''
file = open('citydata.txt')
for line in file:
    citydata = citydata + line
file.close()
#print(citydata)

#利用正则获取citydata中的所有五个数字字符

result_0 = re.findall('[0-9][0-9][0-9][0-9][0-9]',citydata)

#利用set去重

result_1 = set(result_0)

#遍历整个列表
#list_data = []
for url_0 in result_1:
    
    url= "http://tianqi.2345.com/t/his/"+url_0+"his.js?"
    #time.sleep(0.01)
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",    
}

    req = requests.get(url,headers=headers)
    req_return = req.content.decode("gbk","ignore")
    # list_data.append(req_return)  
    f = open("6.txt","a+")#与c语言文件读写相同
    f.write(req_return)
    #print(req_return)

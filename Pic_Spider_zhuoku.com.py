import requests
import re
import os
import time

folder_path = 'F:\PyDowns\zhuoku'
os.chdir(folder_path)

def GetHtml(url):
    Response = requests.get(url)
    Response.encoding = 'GBK'
    Html = Response.text
    return Html

def GetCarsList(url):
    result = GetHtml(url)
    Cars = re.findall(r'<a target="_blank" href="(.*?)\.htm', result)
    CarsList = []
    for i in Cars:
        CarsList.append('http://www.zhuoku.com' + i + '(1).htm#turn')
    return CarsList

def DownPics(url):
    CarsList = GetCarsList(url)
    for i in CarsList:
        PicsUrl = []
        Count = 1
        result = GetHtml(i)
        Title =  re.findall(r'<title>(.*?)\(', result)[0]
        if not os.path.isdir(Title):
            os.mkdir(Title)
        PicNum = re.findall('下一张</a><a href=\d+\((.*?)\)', result)[0]
        href = re.findall('下一张</a><a href=(.*?)\(', result)[0]
        for i in range(1, int(PicNum)+1):
            PicsUrl.append('http://www.zhuoku.com/zhuomianbizhi/jing-car/' + href + '(%d).htm#turn' % i)
        for i in PicsUrl:
            result = GetHtml(i)
            PicName = re.findall(r'thumbs/tn_(.*?)"', result)[0]
            Path = folder_path + "\\" + Title + "\\" + PicName
            PicUrl = re.findall(r'<img id="imageview" src="(.*?)"', result)[0]
            print (PicUrl)
            
            headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer':'%s' % i} #破防盗链        
            with open(Path, 'wb') as f:
                f.write(requests.get(PicUrl, headers = headers).content)
                print ("正在下载《%s》的第%d/%d张" % (Title, Count, int(PicNum)))
                Count += 1
                time.sleep(1)

url = 'http://www.zhuoku.com/zhuomianbizhi/jing-car/index-1.htm'
DownPics(url)
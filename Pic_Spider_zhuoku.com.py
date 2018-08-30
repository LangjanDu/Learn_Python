import requests
import re
import os
import time

folder_path = 'F:\PyDowns\zhuoku'
os.chdir(folder_path)

def CarsUrl():
    url = 'http://www.zhuoku.com/zhuomianbizhi/jing-car/index-1.htm'
    Cars = requests.get(url)
    Cars.encoding = 'GBK'
    Cars = Cars.text
    Cars = re.findall(r'<a target="_blank" href="(.*?)\.htm', Cars)
    CarsUrl = []
    str1 = 'http://www.zhuoku.com'
    for i in Cars:
        CarsUrl.append(str1 + i + '(1).htm#turn')
    return CarsUrl

def PicsUrl():
    str2 = 'http://www.zhuoku.com/zhuomianbizhi/jing-car/'
    PicsUrl = []
    for i in CarsUrl():
        Car = requests.get(i)
        Car.encoding = 'GBK'
        Car = Car.text
        PicNum = re.findall('下一张</a><a href=\d+\((.*?)\)', Car)[0]
        href = re.findall('下一张</a><a href=(.*?)\(', Car)[0]
        for i in range(1, int(PicNum)+1):
            PicsUrl.append(str2 + href + '(%d).htm#turn' % i)
    return PicsUrl

def SavePic():
     for i in PicsUrl():
        Pic = requests.get(i)
        Pic.encoding = 'GBK'
        Pic = Pic.text
        PicName = re.findall(r'thumbs/tn_(.*?)"', Pic)[0]
        Title =  re.findall(r'<title>(.*?)\(', Pic)[0]
        PicNum = re.findall('下一张</a><a href=\d+\((.*?)\)', Pic)[0]
        Path = folder_path + "\\" + Title + "\\" + PicName
        PicUrl = re.findall(r'<img id="imageview" src="(.*?)"', Pic)[0]
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer':'%s' % i}
        
        if not os.path.isdir(Title):
            os.mkdir(Title)
        with open(Path, 'wb') as f:
            f.write(requests.get(PicUrl, headers = headers).content)
            print ("正在下载%s" % PicName)
            time.sleep(1)
SavePic()
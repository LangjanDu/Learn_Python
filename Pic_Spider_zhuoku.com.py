import json
import random
import requests
import re
import threading
import time
import os

folder_path = 'F:\PyDowns\zhuoku'
os.chdir(folder_path)

def MyHeaders(): #随机提取一个User-Agent
    UA = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"]
    myheaders = {'User-Agent':random.choice(UA)}
    UserAgentList = random.choice(UA)
    return myheaders, UserAgentList

def GetProxyList(): #爬取可用的代理IP，验证有效的写入本地文件，每次启动先清除旧数据
    with open('F:\PyDowns\zhuoku\ValidProxyList.json', 'w') as f: #清除旧代理IP
        f.truncate()
    ipurl = 'http://www.xicidaili.com/nn/1' #代理IP网站
    html = requests.get(ipurl, headers = MyHeaders()[0]).text
    ips = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})', html, re.S)
    protocol = re.findall('<td>(\D{4,5})</td>', html)
    for i in range(len(ips)):
        ip = protocol[i].lower() + '://' + ips[i][0] + ':' + ips[i][1]
        proxy = {protocol[i].lower() : ip}
        try:
             ver = requests.get('http://www.zhuoku.com/', headers = MyHeaders()[0], proxies = proxy, timeout = 3)
            if ver.status_code == 200:
                with open('F:\PyDowns\zhuoku\ValidProxyList.json', 'a') as f:
                    json.dump(proxy, f, ensure_ascii = False)
                    f.write('\n')
        except Exception as e:
            pass

def GetProxy(): #从本地文件提取一个随机的可用的代理IP
    ProxyFile = open('F:\PyDowns\zhuoku\ValidProxyList.json', 'r')
    ValidProxyList = []
    for line in ProxyFile.readlines():
        ValidProxyList.append(json.loads(line))
    return random.choice(ValidProxyList)

def GetHtml(url):
    Response = requests.get(url, headers = MyHeaders()[0])
    Response.encoding = 'GBK'
    Html = Response.text
    return Html

def GetCarsList(url): #获取该页面所有图辑URL
    result = GetHtml(url)
    Cars = re.findall(r'<a target="_blank" href="(.*?)\.htm', result)
    CarsList = []
    for i in Cars:
        CarsList.append('http://www.zhuoku.com' + i + '(1).htm#turn')
    return CarsList

def DownPics(url): #提取图片URL并按照图辑名分别保存到本地
    try:
        PicsUrl = []
        Count = 1
        result = GetHtml(url)
        T =  re.findall(r'<title>(.*?)\(', result)[0]
        Title = re.sub('[\/:*?"<>|]','-',T) #去掉非法字符
        if not os.path.isdir(Title):
            os.mkdir(Title)
        PicNum = re.findall('下一张</a><a href=\d+\((.*?)\)', result)[0]
        href = re.findall('下一张</a><a href=(.*?)\(', result)[0]
        for i in range(1, int(PicNum)+1):
            PicsUrl.append('http://www.zhuoku.com/zhuomianbizhi/jing-car/' + href + '(%d).htm#turn' % i)
        for i in PicsUrl:
            result = GetHtml(i)
            PN = re.findall(r'thumbs/tn_(.*?)"', result)[0]
            PicName = re.sub('[\/:*?"<>|]','-',PN) #去掉非法字符
            Path = folder_path + "\\" + Title + "\\" + PicName
            PicUrl = re.findall(r'<img id="imageview" src="(.*?)"', result)[0]
            headers = {'User-Agent' : MyHeaders()[1], 'Referer' : i} #反防盗链        
            with open(Path, 'wb') as f: #下载图片
                print ("正在下载《%s》的第%d/%d张" % (Title, Count, int(PicNum)))
                f.write(requests.get(PicUrl, headers = headers, proxies = GetProxy()).content)
                Count += 1
                time.sleep(random.uniform(1.5,2.0))
            with open('F:\PyDowns\zhuoku\downloads_history.txt', 'a') as downloads_history: #记录已下载的URL
                downloads_history.write(i + '\n')
    except:
        with open('F:\PyDowns\zhuoku\error_history.txt', 'a') as e:
            e.write(url + '\n')

def main(): #主程序
    pageurl = 'http://www.zhuoku.com/zhuomianbizhi/jing-car/index-1.htm' #www.zhuoku.com网汽车类壁纸第*页
    GetProxyList()
    CarsList = GetCarsList(pageurl)
    threads = []
    num = range(len(CarsList))
    for url in CarsList: #创建线程，一个图辑一个线程
        t = threading.Thread(target = DownPics, args=(url,))
        threads.append(t)
    for i in num: #启动线程
        threads[i].start()
    for i in num:
        threads[i].join()

if __name__ == '__main__':
    main()
import urllib.request
import requests
import re
import os
import time

folder_path = 'F:\PyDowns\Lesmao.cc'
os.chdir(folder_path) #定义程序运行目录，下载文件保存路径

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

for page_num in range(17750,0,-1): #最新页码需根据实际情况修改，新->旧

	try:

		album_img_count = 0 #由于图片命名

		for pagination_num in range(1,6): #每页有5个分页，1->5
			pagination_url = "http://www.lesmao.cc/thread-%d-%d-1.html"%(page_num, pagination_num)
			pagination_html = requests.get(pagination_url, headers=headers).text

			album_name = re.findall(r'"adw"><li><img alt="(.*?) -',pagination_html)[0]

			if not os.path.isdir(album_name):
				os.mkdir(album_name) #创建图片专辑文件夹名

			img_urls = re.findall(r'" src="(.*?)"', pagination_html)

			for each_img_url in img_urls:
				album_img_count += 1
				img_name = str(folder_path+'\%s\%s-%s.jpg'%(album_name, album_name, album_img_count))
				print('正在下载：' + '%s-%s.jpg'%(album_name, album_img_count))
				urllib.request.urlretrieve(each_img_url, img_name) #保存图片

	except:
		print("出现错误")

	else: #以下代码用来记录已下载的page_url
		page_url = "http://www.lesmao.cc/thread-%d-1-1.html"%page_num
		downloads_history = r'F:\PyDowns\Lesmao.cc\downloads_history.txt'
		t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		history = t + ' ：' + page_url
		print(history)
		with open(downloads_history, 'a') as f:
			f.write(history + '\n')
			f.close()
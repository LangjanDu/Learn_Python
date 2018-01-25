import urllib.request
import requests
import re
import os 

folder_path = 'F:\PyDowns\Lesmao.cc'	#定义下载文件保存路径
	#print(folder_path)
os.chdir(folder_path)
	#print(os.getcwd())

for page in range(17670,0,-1): #最新页码需根据实际情况修改，新->旧，倒序
	
	try:
		
		page_url = "http://www.lesmao.cc/thread-%d-1-1.html"%(page)
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
		
		Response = urllib.request.urlopen(page_url).read() #获取网页的源代码；urllib.request 模块提供了最基本的构造 HTTP 请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理 authenticaton （授权验证）， redirections （重定向)， cookies (浏览器Cookies）以及其它内容
		page_html = Response.decode('utf-8') #Response为bytes类型,需要进行类型转换才能正常显示在python中
		album_name = re.findall(r'"adw"><li><img alt="(.*?) -',page_html)[0]
		print(album_name)
		os.mkdir(album_name)
		album_img_count = 0
		
		for x in range(1,6): #每页有5个分页，1->5
			
			Pagination_url = "http://www.lesmao.cc/thread-%d-%d-1.html"%(page,x)
			print(Pagination_url)
			headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

			r = requests.get(Pagination_url, headers=headers)

			Response = urllib.request.urlopen(Pagination_url) 
			Pagination_html = Response.read().decode('utf-8')			
			img_name = re.findall(r'"adw"><li><img alt="(.*?) -',Pagination_html)[0]
				#print(img_name)
			img_ul = re.findall(r'ul class="adw".*?</ul>',Pagination_html,re.S)[0] #re.S必须要有，#使 . 匹配包括换行在内的所有字符
			img_urls = re.findall(r'" src="(.*?)"',img_ul) 
				#print(img_urls)
				#album_img_count = 0
				
			for each_img_url in img_urls:
				
				print("正在下载:"+each_img_url)
				album_img_count += 1
				page_path = str(folder_path+'\%s\%s-%s.jpg'%(album_name,img_name,album_img_count))
				#print(page_path)
				urllib.request.urlretrieve(each_img_url,page_path)
				
	except:
		print("出现错误")
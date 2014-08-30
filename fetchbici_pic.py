#coding:utf-8
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import urllib2
import urllib
import re
import os





def getimg(html,dirpath):

	drive = "E:\\img\\"+dirpath
	if not os.path.exists(drive):
 	    os.mkdir(drive)

	#过滤出图片的url的list
	urllist = re.findall(r'<img.*?zoomfile="(.*?.jpg)"',html)

	for url in urllist:
		
		imgname = url[url.rindex('/')+1:]
		#url_asem 是过滤出的图片url加上比斯的域名
		url_asem = "http://hkbici.com/"+url
		print url_asem,imgname
        #从网址获取资源到本地
		urllib.urlretrieve(url_asem, os.path.join(drive,imgname))



# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('http://hkbici.com/forum.php')

# Inspect name of the form
for f in br.forms():
    print f

# Select the second (index one) form - the first form is a search query box
br.select_form(nr=0)

# User credentials
br.form['username'] = 'xchong'
br.form['password'] = 'xchong24'

# Login
br.submit()


#fetch the html after log in
htmlpagexml = br.open('http://hkbici.com/forum-18-2.html').read()
print(htmlpagexml)

#magin
print 'fetch url from website \n'

#filter the page url
urlpagelist =  re.findall(r'<a href="(thread-.*?)"',htmlpagexml)

#urlpagelist去重复
newlist = list()
for item in urlpagelist:

	if  item not in newlist:
		newlist.append(item) 

#打印出最终的各个图片页面的url
print newlist

for urlp in newlist:
    
  #进入详细图片页面的url
  urlpasem = "http://hkbici.com/"+urlp
  print urlpasem	    
  #进入详细图片页面url的xml
  htmlimgxml = br.open(urlpasem).read()
  getimg(htmlimgxml,urlp)
     




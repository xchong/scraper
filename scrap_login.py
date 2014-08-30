#coding="utf-8"
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

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
br.form['username'] = 'your username'
br.form['password'] = 'your password'

# Login
br.submit()

print(br.open('http://hkbici.com/forum.php?gid=1').read())
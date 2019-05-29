from grab import Grab
g = Grab()
g.setup(url='https://football.kulichki.net/russia2001/1/index.htm',
        log_file='out.html')
g.request()

print(g.response.code)
print(g.response.headers)


filter='''<font size="2">
<img src="../Soccbar.gif" width="346" height="14"></font></p>
</font>
<p align="center"><font size="2">'''

#body_str = g.response.body.decode('cp1251')
#g.response.body = body_str.encode('utf-8')
#print(body_str)

print(g.search(filter))
#g.xpath_text('//h2/a[@class="topic"]')
#<b><a href="1.htm"> </a><br>
print ('!')
print (g.xpath_text('.//table/tr/td'))
print ('!')

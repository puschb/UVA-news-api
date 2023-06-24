from bs4 import BeautifulSoup
from urllib2 import urlopen





'''
#getting an article from the list
get = urlopen("https://news.virginia.edu/content/all-news?page=534")
html = get.read()

soup = BeautifulSoup(html, 'html.parser')
list_of_articles = soup.find_all("div", class_ = "uva-today-news-item-title")
print list_of_articles

#print list_of_articles[0].a['href']
#print list_of_articles[0].a.contents[0]

#print soup'''

'''
#text
get = urlopen("https://news.virginia.edu/content/el-nino-and-its-high-temps-are-back-already-hot-world-what-does-it-mean")
html = get.read()

soup = BeautifulSoup(html, 'html.parser')

intro = soup.find("div", class_ = "paragraphs-item-intro-text")
body = soup.find_all("div", class_ = "paragraphs-item-body-text")

text = ""
for p in intro.find_all("p"):
    if p.string != None:
        text += p.string.encode('utf-8') + '\n\n'
    else:
        for s in p.stripped_strings:
            text += s.encode('utf-8')
        text += '\n\n'



for b in body:
    for p in b.find_all("p"):
        if p.string != None:
            text += p.string.encode('utf-8') + '\n\n'
        else:
            for s in p.stripped_strings:
                text += s.encode('utf-8')
            text += '\n\n'


print text'''



#id
#using the index from the list+ page number


'''#category
get = urlopen("https://news.virginia.edu/content/uva-marshall-scholar-kristen-barrett-explore-literature-film")
html = get.read()

soup = BeautifulSoup(html, 'html.parser')
category= soup.find("meta", property = "og:type")['content']
print category'''

#author
#changes based on the version, need to make two different ones

#email - same as author

#date
'''get = urlopen("https://news.virginia.edu/content/uva-marshall-scholar-kristen-barrett-explore-literature-film")
html = get.read()

soup = BeautifulSoup(html, 'html.parser')
date= soup.find("meta", property = "og:updated_time")['content']
print date'''


#link - from list

#title
get = urlopen("https://news.virginia.edu/content/uva-marshall-scholar-kristen-barrett-explore-literature-film")
html = get.read()

soup = BeautifulSoup(html, 'html.parser')
title= soup.find("meta", property = "og:title")['content']
print title



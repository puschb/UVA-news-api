from bs4 import BeautifulSoup
from urllib.request import urlopen
import asyncio
import time
import httpx

class UVANewsArticle():
    def __init__(self,title, author,email, date, link, text, category):
        self.postTitle = title
        self.postAuthor = author
        self.postEmail = email
        self.postDate = date
        self.postLink = link
        self.postText = text
        self.postCategory = category

    def __repr__(self):
        return u'''{{
          "postTitle": "{}",
          "postAuthor": "{}",
          "postEmail": "{}",
          "postDate": "{}",
          "postLink": "{}",
          "postText": "{}",
          "postCategory": "{}"
        }}'''.format( self.postTitle, self.postAuthor,self.postEmail,
                    self.postDate,self.postLink, self.postText, self.postCategory)
    

class UVANewsArticleBuilder():

    @staticmethod
    async def buildArticle(link, built_articles_list, client):
        '''async with httpx.AsyncClient() as client:
            response = await client.get(link)'''
        response = await client.get(link)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        num_exceptions = 0

        author, exception = UVANewsArticleBuilder.__getAuthor(soup,link)
        num_exceptions += exception
        email, exception = UVANewsArticleBuilder.__getEmail(soup)
        num_exceptions += exception
        date, exception = UVANewsArticleBuilder.__getDate(soup)
        num_exceptions += exception
        title, exception = UVANewsArticleBuilder.__getTitle(soup)
        num_exceptions += exception
        text, exception = UVANewsArticleBuilder.__getText(soup)
        num_exceptions += exception
        category, exception = UVANewsArticleBuilder.__getCategory(soup)
        num_exceptions += exception

        built_articles_list.append(UVANewsArticle(author=author,email=email,date=date, link=link, 
                                    title=title, text=text,category= category))

        #return UVANewsArticle(author=author,email=email,date=date, link=link, 
        #                      title=title, text=text,category= category)#, num_exceptions

    @staticmethod
    def __getAuthor(soup,link):
        did_exception_happen = 0
        author = None
        try:
            author_email_tag = soup.find("li", class_ = "author list") or soup.find("li", class_ = "author")
            author = author_email_tag.find_all("a")[0].string
        except:
            did_exception_happen = 1
        return author, did_exception_happen
    
    @staticmethod
    def __getEmail(soup):
        did_exception_happen = 0
        email = None
        try:
            author_email_tag = soup.find("li", class_ = "author list") or soup.find("li", class_ = "author")
            email = author_email_tag.find_all("a")[1].string
        except:
            did_exception_happen = 1
        return email, did_exception_happen

    @staticmethod    
    def __getDate(soup):
        did_exception_happen = 0
        try:
            date = soup.find("meta", property = "og:updated_time")['content']
        except:
            date = None
            did_exception_happen = 1
        return date, did_exception_happen
    
    @staticmethod
    def __getTitle(soup):
        did_exception_happen = 0
        try:
            title = soup.find("meta", property = "og:title")['content']
        except:
            title = None
            did_exception_happen = 1
        return title, did_exception_happen

    @staticmethod
    def __getText(soup):
        did_exception_happen = 0
        try:
            intro = soup.find("div", class_ = "paragraphs-item-intro-text")
            body = soup.find_all("div", class_ = "paragraphs-item-body-text")

            text = ""
            for p in intro.find_all("p"):
                if p.string != None:
                    text += p.string + '\n\n'
                else:
                    for s in p.stripped_strings:
                        text += s
                    text += '\n\n'

            for b in body:
                for p in b.find_all("p"):
                    if p.string != None:
                        text += p.string + '\n\n'
                    else:
                        for s in p.stripped_strings:
                            text += s
                        text += '\n\n'
        except:
            text = None
            did_exception_happen = 1
        
        return text, did_exception_happen

    @staticmethod    
    def __getCategory(soup):
        did_exception_happen = 0
        try:
            category= soup.find("meta", property = "og:type")['content']
        except:
            category = None
            did_exception_happen = 1
        return category, did_exception_happen
    

    

class ScrapeUVANews:
    css_classifier_body_p = "paragraphs-item-body-text"
    css_classifier_intro_p = "paragraphs-item-intro-text"
    uva_news_default_link = "https://news.virginia.edu/content/all-news?page={}"
    counter = 1

    #hardcoded for now, will change
    final_page = 534

    async def getAll(self):
        t1 = time.perf_counter()
        page_num = self.final_page
        uva_all_news_links = [self.uva_news_default_link.format(i) for i in range(534)]
        
        all_article_links = []
        built_articles = []
        async with httpx.AsyncClient(timeout=None) as client:
            await asyncio.gather(*[self.__getArticles(page,all_article_links,client) for page in uva_all_news_links])

            await asyncio.gather(*[UVANewsArticleBuilder.buildArticle(link, built_articles, client) for link in all_article_links])





        '''finishedScraping = False
        list_of_articles = self.__getArticles(self.uva_news_default_link.format(page_num))

        
        total_exceptions = 0

        while((not list_of_articles == None) and len(list_of_articles > 0)):
            

            for article_link in list_of_articles:
                built_article, num_exceptions = UVANewsArticleBuilder.buildArticle(article_link)
                total_exceptions += num_exceptions
                uva_all_news_links.append(built_article)
            print(i)
            
            page_num += 1
            list_of_articles = self.__getArticles(self.uva_news_default_link.format(page_num))'''

        #print(self.commandLineReturnArticles(built_articles))
        #print(f"number of exceptions while scraping: {num_exceptions}")
        print(f'done\n#articles = {len(all_article_links)}\ntime: {time.perf_counter()-t1}')

     
        
    
    
    async def __getArticles(self,link, all_articles,client):
        self.counter += 1
        root_link = "https://news.virginia.edu"
        '''async with httpx.AsyncClient() as client:
            response = await client.get(link)'''
        response = await client.get(link)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        list_of_articles = soup.find_all("div", class_ = "uva-today-news-item-title")

        for article_link in list_of_articles:
            all_articles.append(root_link + article_link.a['href'])
        
    
    def commandLineReturnArticles(self, list_of_articles):
        list_to_str = u'{\n"posts": ['
        for count,article in enumerate(list_of_articles):
            if not count == len(list_of_articles)-1:
                list_to_str += str(article) + ',\n'
            else:
                list_to_str += str(article) + '\n]\n}'

        return list_to_str
    



scraper = ScrapeUVANews()
asyncio.run(scraper.getAll())
#scraper.simpleTest2()

    
        


#output_json = 
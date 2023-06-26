from bs4 import BeautifulSoup
from urllib.request import urlopen

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
    def buildArticle(link):
        get = urlopen(link)
        html = get.read()
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
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

        return UVANewsArticle(author=author,email=email,date=date, link=link, 
                              title=title, text=text,category= category), num_exceptions

    @staticmethod
    def __getAuthor(soup,link):
        did_exception_happen = 0
        

        #stopped here

        author_email_tag = soup.find("li", class_ = "author list").find_all("a") #new web page version
        if author_email_tag == None:
            author_email_tag= soup.find("li", class_ = "author").find_all("a") #old web page version
        if author_email_tag == None:
            did_exception_happen = 1
        else:
            author = author_email_tag[0].string
        return author, did_exception_happen
    
    @staticmethod
    def __getEmail(soup):
        did_exception_happen = 0
        try:
            author_email_tag= soup.find("li", class_ = "author list").find_all("a")
            email = author_email_tag[1].string
        except AttributeError:
            author_email_tag= soup.find("li", class_ = "author").find_all("a")
            email = author_email_tag[1].string
        except:
            email = None
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
    article_list_link = "https://news.virginia.edu/content/all-news?page={}"

    def getAll(self):
        page_num = 0

        finishedScraping = False
        list_of_articles = self.__getArticles(self.article_list_link.format(page_num))

        all_articles = []
        total_exceptions = 0

        while(not finishedScraping):
            for article_link in list_of_articles:
                built_article, num_exceptions = UVANewsArticleBuilder.buildArticle(article_link)
                total_exceptions += num_exceptions
                all_articles.append(built_article)
            
            page_num += 1
            list_of_articles = self.__getArticles(self.article_list_link.format(page_num))
            if list_of_articles == None or len(list_of_articles) == 0:
                finishedScraping = True

        print(self.commandLineReturnArticles(all_articles))
        print(f"number of exceptions while scraping: {num_exceptions}")
        
        

    def __getArticles(self,link):
        root_link = "https://news.virginia.edu"
        get = urlopen(link)
        html = get.read()
        soup = BeautifulSoup(html, 'html.parser')
        list_of_articles = soup.find_all("div", class_ = "uva-today-news-item-title")

        article_links = []

        for article_link in list_of_articles:
            article_links.append(root_link + article_link.a['href'])
        
        return article_links
    
    def commandLineReturnArticles(self, list_of_articles):
        list_to_str = u'{\n"posts": ['
        for count,article in enumerate(list_of_articles):
            if not count == len(list_of_articles)-1:
                list_to_str += str(article) + ',\n'
            else:
                list_to_str += str(article) + '\n]\n}'

        return list_to_str

    
        

scraper = ScrapeUVANews()
scraper.getAll()
#output_json = 
from bs4 import BeautifulSoup
from urllib2 import urlopen

class UVANewsArticle():
    def __init__(self):
        self.postId = None
        self.postTitle = None
        self.postAuthor = None
        self.postEmail = None
        self.postDate = None
        self.postLink = None
        self.postText = None
        self.postCategory = None

    def __repr__(self):
        return '''{{
          "postId": "{}",
          "postTitle": "{}",
          "postAuthor": "{}",
          "postEmail": "{}",
          "postDate": "{}",
          "postLink": "{}",
          "postText": "{}",
          "postCategory": "{}"
        }'''.format(self.postId, self.postTitle, self.postAuthor,self.postEmail,
                    self.postDate,self.postLink, self.postText, self.postCategory)
    

class UVANewsArticleBuilder():

    def buil
    

class ScrapeUVANews:
    css_classifier_body_p = "paragraphs-item-body-text"
    css_classifier_intro_p = "paragraphs-item-intro-text"
    article_list_link = "https://news.virginia.edu/content/all-news?page={}"

    def getAll(self):
        page_num = 0

        UVANewsArticles = []
        
        finishedScraping = False

        while(not finishedScraping):
            list_of_articles = self.__getArticles(self.article_list_link.format(page_num))
            print list_of_articles
        

    def getRecent(self,num):
        pass

    def getByDate(self, date):
        pass
    def getByAuthor(self, author):
        pass

    def getByCategory(self, category):
        pass

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

    def __

    def __getText(self,html):
        pass
        

scraper = ScrapeUVANews()
scraper.getAll()
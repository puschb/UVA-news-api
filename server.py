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
    

class scrapeUVANews:
    css_classifier_body_p = "paragraphs-item-body-text"
    css_classifier_intro_p = "paragraphs-item-intro-text"

    def get():
        

'''example = UVANewsArticle()
example.postId = "1"
example.postAuthor = "Ben Pusch"
example.postEmail = "bhx5gh@virginia.edu"
example.postDate = "6/23/23"
example.postLink = "www.example.com"
example.postText = "This article is awesome"
example.postCategory = "Business"

print example'''
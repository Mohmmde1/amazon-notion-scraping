import requests
from bs4 import BeautifulSoup
from objs.book import Book

class AmazonScraper:
    url = None
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = None
    soup = None
    
    @classmethod
    def initialize(cls, url):
        cls.url = url
        cls.page = requests.get(url, headers=cls.headers)
        print(cls.page)
        cls.soup = BeautifulSoup(cls.page.content, "html.parser")
    
    @classmethod
    def scrape(cls):
        stars_emjos = {1:"⭐️", 2:"⭐️⭐️", 3:"⭐️⭐️⭐️", 4:"⭐️⭐️⭐️⭐️", 5:"⭐️⭐️⭐️⭐️⭐️"}
        book = Book(score=stars_emjos[int(round(float(cls.get_score()[0])))], 
                    link=cls.url, author=cls.get_author(),
                    page_count=cls.get_page_count(), name=cls.get_name(), 
                    puplisher=cls.get_puplisher())
        return book
    
    @classmethod
    def get_score(cls):
        score = cls.soup.find("span", {"class": "a-icon-alt"})
        return score.getText()

    @classmethod
    def get_link(cls):
        return cls.url

    @classmethod
    def get_author(cls):
        name = cls.soup.find("a", {"class" : "a-size-base a-link-normal a-text-normal"})
        return name.getText()
        

    @classmethod
    def get_page_count(cls):
        div = cls.soup.find("div", {"class":"a-section a-spacing-none a-text-center rpi-attribute-value"})
        page_count = div.findChild("span")
        return int(page_count.getText().split()[0])

    @classmethod
    def get_name(cls):
        title = cls.soup.findAll("span", {"id":"productTitle"})[0]
        return title.get_text()


    @classmethod
    def get_type(cls):
        return "book"

    @classmethod
    def get_puplisher(cls):
        div = cls.soup.findAll("div", {"class":"a-section a-spacing-none a-text-center rpi-attribute-value"})[2]
        puplisher = div.findChild("span")
        return puplisher.getText()


    @classmethod
    def get_release_date(cls):
        div = cls.soup.findAll("div", {"class":"a-section a-spacing-none a-text-center rpi-attribute-value"})[3]
        release_date = div.findChild("span")
        return release_date.getText()

    
        
        

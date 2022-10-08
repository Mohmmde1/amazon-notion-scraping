from objs.notion import Notion
from utils.utils import fill_prop
from objs.book import Book
from objs.amazon import AmazonScraper

# url = input("Insert the book's url=> ")
file_name = "./json/files/db_create.json"
URL = "https://www.amazon.com/Zero-One-Notes-Startups-Future-ebook/dp/B00J6YBOFQ/ref=sr_1_1?crid=FUJBV9FJYCE9&keywords=zero+to+one&qid=1665234827&qu=eyJxc2MiOiIyLjAzIiwicXNhIjoiMS44NCIsInFzcCI6IjIuMDUifQ%3D%3D&s=digital-text&sprefix=zero+to+one%2Cdigital-text%2C596&sr=1-1"

# initiolize the url
AmazonScraper.initialize(URL)
book = AmazonScraper.scrape()

# AmazonScraper.scrape(url)
data_dict = fill_prop(file_name, book)

# add a record
Notion.create(data=data_dict)
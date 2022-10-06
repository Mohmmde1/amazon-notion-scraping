from objs.notion import Notion
from utils.utils import fill_prop
from objs.Book import Book
from objs.amazon import AmazonScraper
from pprint import pprint

# url = input("Insert the book's url=> ")
file_name = "./json/files/db_create.json"

# AmazonScraper.scrape(url)
data_dict = fill_prop(file_name, Book())
Notion.create(data=data_dict)
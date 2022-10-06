import json
from objs.notion import Notion

from helper_func import fill_prop
        
file_name = "./json/files/db_create.json"
Notion.create(data=fill_prop(file_name)
)
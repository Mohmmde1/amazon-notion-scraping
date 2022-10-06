from objs.notion import Notion
from utils.utils import fill_prop
        
file_name = "./json/files/db_create.json"
data_dict = fill_prop(file_name)
Notion.create(data=data_dict)
import json
from objs.notion import Notion
def fill_prop(json_file_name, score="null", link='"https://amazon.com"', 
                    author='', page_count=0, name='', status='Ready to Start', 
                    type='book', puplisher="", 
                    release_date="2021-05-11T11:00:00.000-04:00"
        ):
        with open(json_file_name, 'r', encoding='utf8') as f:
            data = f.read()
            data_dict = json.loads(data)
            data_dict["properties"]["Name"]["title"][0]['text']['content'] = name
            data_dict["properties"]["Page count"]["number"] = page_count
            data_dict["properties"]["Status"]["select"]["name"] = status
            data_dict["properties"]["Score 5"]["select"]["name"] = score
            data_dict["properties"]["Type"]["select"]["name"] = type
            data_dict["properties"]["Author"]["rich_text"][0]['text']['content'] = author
            data_dict["properties"]["Publisher"]["rich_text"][0]['text']['content'] = puplisher
            data_dict["properties"]["Publishing/Release Date"]["date"]['start'] = release_date
            data_dict["properties"]["Link"]["url"] = link

            return data_dict
file_name = "./json/files/db_create.json"
Notion.create(data=fill_prop(file_name)
)
import json

def fill_prop(json_file_name, book, database_id):
        with open(json_file_name, 'r', encoding='utf8') as f:
            data = f.read()
            data_dict = json.loads(data)
            data_dict["parent"]["database_id"] = database_id
            data_dict["properties"]["Name"]["title"][0]['text']['content'] = book.get_name()
            data_dict["properties"]["Page count"]["number"] = book.get_page_count()
            data_dict["properties"]["Status"]["select"]["name"] = book.get_status()
            data_dict["properties"]["Score 5"]["select"]["name"] = book.get_score()
            data_dict["properties"]["Type"]["select"]["name"] = book.get_type()
            data_dict["properties"]["Author"]["rich_text"][0]['text']['content'] = book.get_author()
            data_dict["properties"]["Publisher"]["rich_text"][0]['text']['content'] = book.get_puplisher()
            data_dict["properties"]["Publishing/Release Date"]["date"]['start'] = book.get_release_date()
            data_dict["properties"]["Link"]["url"] = book.get_link()
            return data_dict
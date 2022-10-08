from dotenv import load_dotenv
from pprint import pprint
from utils.exceptions import ERORR_400
import requests
import json
import os 


class Notion:
    # Notion's CRUD
    load_dotenv()
    token = os.environ.get('token')
    database_id = os.environ.get('database_id')
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    url = f'https://api.notion.com/v1/databases/{database_id}'
    

    @staticmethod
    def read(headers):
        res = requests.request("GET", Notion.url, headers=headers)
        data = res.json()
        pprint(res.text)
        with open('./json/files/db_read.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)


    @staticmethod
    def update(headers):
        json_file = open('db_update.json')
        data = json.loads(json_file.read())
        data = json.dumps(data)
        res = requests.request("PATCH", Notion.url, headers=headers, data=json_file.read())
        print(res.status_code)
        print(res.text)

    @staticmethod
    def create(data):
        createUrl = 'https://api.notion.com/v1/pages'
        
        data = json.dumps(data)
        try:
            res = requests.request("POST", createUrl, headers=Notion.headers, data=data)
            if res.status_code == 400:
                raise ERORR_400
            if res.status_code == 200:
                print("Record has been added")
                
        except(ERORR_400):
            pprint(json.loads(res.text))






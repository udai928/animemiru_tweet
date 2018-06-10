#-*- codinf:urf-8 -*-
# https://gspread.readthedocs.io/en/latest/
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

API_KEYS_JSON = "./config/animemirutweetbot-d7fc72419d5a.json"
SHEET_NAME = "twitterbotsheet"

class Spreadsheet:
    def __init__(self,when):
        scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(API_KEYS_JSON, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(SHEET_NAME).sheet1
        # スプレッドシートの1行目はヘッダー行
        if when == "morning":
            self._texts = worksheet.row_values(1)
        elif when == "noon":
            self._texts = worksheet.row_values(2)
        elif when == "night":
            self._texts = worksheet.row_values(3)
        else:
            self._texts = worksheet.row_values(random.randint(1,3))
        self._text_cnt = len(self._texts)
        self._search_words = worksheet.row_values(4)
        self._search_words_cnt = len(self._search_words)

    @property
    def texts(self):
        return self._texts

    @property
    def text_cnt(self):
        return self._text_cnt

    @property
    def search_words(self):
        return self._search_words
    
    @property
    def search_words_cnt(self):
        return self._search_words_cnt

def main():
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(API_KEYS_JSON, scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open(SHEET_NAME).sheet1
    print(worksheet.row_values(1))

if __name__ == '__main__':
    main()

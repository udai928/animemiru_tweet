#-*- codinf:urf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def main():
scope = ['https://spreadsheets.google.com/feeds']
#ダウンロードしたjsonファイルを同じフォルダに格納して指定する
credentials = ServiceAccountCredentials.from_json_keyfile_name('XXXXXXXXX.json', scope)
gc = gspread.authorize(credentials)
# 共有設定したスプレッドシートの名前を指定する
worksheet = gc.open("YYYYYYYYY").sheet1
#以下、動作テスト
# A1セルの値を取得
print worksheet.cell(1,1)
# A1セルを更新
worksheet.update_cell(1,1, u'Hello, gspread.')


if __name__ == '__main__':
    main()

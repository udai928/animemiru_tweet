#-*- coding:utf-8 -*-
import re
import os
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup

IMAGE_COUNT = 10

class ImageUrl:
    def __init__(self,search_word):
        self._image_urls = get_image_urls_from_google(search_word)
        self._image_urls_cnt = IMAGE_COUNT
    
    @property
    def image_urls(self):
        return self._image_urls

    @property
    def image_urls_cnt(self):
        return self._image_urls_cnt


def get_image_urls_from_google(searchword):
    url_keyword = urllib.parse.quote(searchword)
    search_url = 'https://www.google.com/search?hl=jp&q=' + url_keyword + '&btnG=Google+Search&tbs=0&safe=off&tbm=isch'

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    headers = {'User-Agent': user_agent }
    req = urllib.request.Request(search_url, None, headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    a_tags_filtered_jsname = soup.find_all("div", attrs={"class": "rg_meta notranslate"}, limit=IMAGE_COUNT)
    image_urls = []
    for a_tag_filtered_jsname in a_tags_filtered_jsname:
        json_str = str(a_tag_filtered_jsname).replace("<div class=\"rg_meta notranslate\" jsname=\"ik8THc\">", "").replace("</div>", "")
        json_obj = json.loads(json_str)
        image_urls.append(json_obj["ou"])

    return image_urls
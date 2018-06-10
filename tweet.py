#-*- cofing:utf-8 -*-
import twitter
import yaml
import sys
import random
import Spreadsheet
import ImageUrl

DEFAULT_TEXT_MORNING = "おはよー！朝だよー"
DEFAULT_TEXT_NOON = "お昼だね！何食べるー？"
DEFAULT_TEXT_NIGHT = "今日もお疲れ様っ！"

# python tweet.py [when(morning/noon/night)]
# 例：python tweet.py morning
def main():
    when = sys.argv[1]
    spreadsheet = Spreadsheet.Spreadsheet(when)
    tweet_text = get_tweet_text(spreadsheet)
    image_url = get_tweet_image_url(spreadsheet)

    CONFIGS = load_config()
    api = twitter.Api(consumer_key=CONFIGS["CONSUMER_KEY"]
                  ,consumer_secret=CONFIGS["CONSUMER_SECRET"]
                  ,access_token_key=CONFIGS["ACCESS_TOKEN_KEY"]
                  ,access_token_secret=CONFIGS["ACCESS_TOKEN_SECRET"]
                  )
    
    post_tweet(api, tweet_text, image_url)
    print(tweet_text,image_url)
    print(get_my_one_tweet(api).text)


def get_tweet_text(spreadsheet):
    return spreadsheet.texts[random.randint(1,spreadsheet.text_cnt - 1)]


def get_tweet_image_url(spreadsheet):
    search_word = "アニメ" + " " + spreadsheet.search_words[random.randint(1,spreadsheet.search_words_cnt - 1)]
    image_url = ImageUrl.ImageUrl(search_word)
    image_url = image_url.image_urls[random.randrange(image_url.image_urls_cnt)]
    if is_none_or_empty(image_url):
        return "http://animemiru.jp/"
    else:
        return image_url

def get_my_tweets(api,cnt):
    return api.GetUserTimeline(api.VerifyCredentials().id, count=cnt)

def get_my_one_tweet(api):
    tweet_list = api.GetUserTimeline(api.VerifyCredentials().id, count=1)
    return tweet_list[0]

def post_tweet(api, tweet_text, image_url):
    if is_none_or_empty(image_url):
        api.PostUpdate(tweet_text)
    else:
        api.PostUpdate(tweet_text, media=image_url)

def is_none_or_empty(str):
    if str == None or len(str) == 0:
        return True
    else:
        return False


def load_config():
    CONFIG_DIR = "./config/"
    f = open(CONFIG_DIR + "config.yaml",'r')
    configs = yaml.load(f)
    f.close()
    return configs


if __name__ == '__main__':
    main()

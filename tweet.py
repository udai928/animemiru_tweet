#-*- cofing:utf-8 -*-
import twitter
import yaml

DEFAULT_TEXT_MORNING = "おはよー！朝だよー"
DEFAULT_TEXT_NOON = "お昼だね！何食べるー？"
DEFAULT_TEXT_NIGHT = "今日もお疲れ様っ！"

# python tweet.py [when(morning/noon/night)]
# 例：python tweet.py morning
def main():
    CONFIGS = load_config()
    api = twitter.Api(consumer_key=CONFIGS["CONSUMER_KEY"]
                  ,consumer_secret=CONFIGS["CONSUMER_SECRET"]
                  ,access_token_key=CONFIGS["ACCESS_TOKEN_KEY"]
                  ,access_token_secret=CONFIGS["ACCESS_TOKEN_SECRET"]
                  )

    print(get_my_one_tweet(api).text)


def get_tweet_text(when):

def get_tweet_image_url():

def spredsheet_data():



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
    if str == None or len(str) = 0:
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
